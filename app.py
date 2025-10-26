from flask import Flask, request, jsonify, render_template, send_from_directory, current_app, g 
from datetime import datetime 
import json
import sqlite3
import click 

import os 

# initialize a flask instance 
app = Flask(
    __name__,
    instance_path=os.path.join(os.path.dirname(__file__), 'instance'),
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static'))

# Configure the database
app.config['DATABASE'] = os.path.join(app.instance_path, 'logs.db')

# Ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass 

# Create a single db connection per request
def get_db():
    # g - special flask obj with temporary storage space during a request
    if 'db' not in g: 
        g.db = sqlite3.connect(
            # get db file path
            current_app.config['DATABASE'],
            # parse declared types: INTEGER, TEXT, etc
            detect_types = sqlite3.PARSE_DECLTYPES
        )
        # change how query results are returned 
        g.db.row_factory = sqlite3.Row
    return g.db 

# Check if a connection was created by checking if g.db was set. if so, close db properly after each request 
def close_db(e=None):
    db = g.pop('db', None)
    
    if db is not None:
        db.close()

# Get db connection, recreate the db structure based on 'schema.sql'
def init_db():
    db = get_db ()
    
    with current_app.open_resource('schema.sql') as f: 
        db.executescript(f.read().decode('utf8'))

# define a new command that can be run in terminal
@click.command('init-db')
def init_db_command():
    # clear existing data and create new tables 
    init_db()
    click.echo('Initialized the database')
    
# interpret timestamp values in db, convert to datetime
sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)
# Register with the application instance 
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def get_all_submissions():
    db = get_db()
    c = db.cursor() # create cursor obj to execute sql queries 
        
    # select all submissions ordered by newest first - READ only
    c.execute('''SELECT id, timestamp, development_type, property_address, answers_json, reference_no 
              FROM submissions
              ORDER BY timestamp DESC''')
    
    # get all matching rows returned by queries
    submissions = c.fetchall() 
    
    # convert list of tuples from sqlite into a list of dictionaries 
    result = []
    
    for s in submissions: 
        result.append({
            # extract using row factory
            'id': s['id'],
            'timestamp': s['timestamp'],
            'development_type': s['development_type'],
            'property_address': s['property_address'],
            'answers_json': json.loads(s['answers_json']) if s['answers_json'] else {}, # convert answers json string to python lst
            'reference_no': s['reference_no']
        })
    
    return result
    
# Routes

# main route
@app.route('/')
def home():
    return send_from_directory(app.template_folder, 'index.html')

# # serve frontend static files 
# @app.route('/<path:filename>')
# def serve_frontend_files(filename):
#     try:
#         return send_from_directory(app.static_folder, filename)
#     except FileNotFoundError:
#         return "File not found", 404
    
# admin-dahsboard 
@app.route('/admin')
def admin():
    try: 
        submissions = get_all_submissions()
        
        stats = {
            'total_submissions': len(submissions),            
            'exempt_count': len([s for s in submissions if s.get('answers_json', {}).get('exemption_status') == 'exempt']),
            'not_exempt_count': len([s for s in submissions if s.get('answers_json', {}).get('exemption_status') == 'not_exempt']),
            'incomplete_count': len([s for s in submissions if s.get('answers_json', {}).get('exemption_status') == 'incomplete']),
            'dev_types': {}  # will store count by development type
        }
        
        # calculate submissions per dev type
        for s in submissions:
            dev_type = s.get('development_type', 'Unknown')
            stats['dev_types'][dev_type] = stats['dev_types'].get(dev_type, 0) + 1 # running count
        return render_template('/admin/admin_dashboard.html', stats=stats)
    except Exception as e:
        return f'Error loading dashboard: {str(e)}', 500
    
# display all logs as json
@app.route('/logs-viewer')
def log_viewer():
    return render_template('/admin/logs.html')

# render map
@app.route('/maps')
def maps():
    return render_template('maps.html')
    
# api endpoint to get all logs
@app.route('/logs')
def get_logs():
    try:
        db = get_db()
        c = db.cursor()
        
        c.execute('''SELECT id, timestamp, development_type, property_address, answers_json, reference_no  
                  FROM submissions
                  ORDER BY timestamp DESC''')
        
        submissions = c.fetchall()
        
        result = []
        for s in submissions:
            result.append({
                'id': s['id'],
                'timestamp': s['timestamp'],
                'dev_type': s['development_type'],
                'property_address': s['property_address'],
                'answers_json': json.loads(s['answers_json']) if s['answers_json'] else {},
                'reference_number': s['reference_no']  # Add this field as expected by frontend
            })
        
        return jsonify({
            'submissions': result,
            'total_count': len(result)
        })
    except Exception as e:
        return jsonify({'error': f'Failed to fetch logs: {str(e)}'}), 500

# api endpoint to search logs
@app.route('/logs/search')
def search_logs():
    try:
        dev_type = request.args.get('dev_type', '').strip()
        address = request.args.get('address', '').strip()
        
        db = get_db()
        c = db.cursor()
        
        # dynamic query based on search parameters
        query = '''SELECT id, timestamp, development_type, property_address, answers_json 
                  FROM submissions WHERE 1=1'''
        params = []
        
        if dev_type:
            query += ' AND LOWER(development_type) LIKE LOWER(?)'
            params.append(f'%{dev_type}%')
            
        if address:
            query += ' AND LOWER(property_address) LIKE LOWER(?)'
            params.append(f'%{address}%')
            
        query += ' ORDER BY timestamp DESC'
        
        c.execute(query, params)
        submissions = c.fetchall()
        
        result = []
        for s in submissions:
            result.append({
                'id': s['id'],
                'timestamp': s['timestamp'],
                'dev_type': s['development_type'],
                'property_address': s['property_address'],
                'answers_json': json.loads(s['answers_json']) if s['answers_json'] else {},
                'reference_number': s['reference_no']  
            })
        
        return jsonify({
            'submissions': result,
            'total_count': len(result)
        })
    except Exception as e:
        return jsonify({'error': f'Failed to search logs: {str(e)}'}), 500

# api endpoint to receive and store form submissions
@app.route('/submit', methods=['POST'])
def submit_log():
    try:
        # only accept json data 
        data = request.get_json()
        # extract info 
        development_type = data.get('development_type', '')
        property_address = data.get('property_address', '')
        answers = data.get('answers', {})
        submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reference_no = data.get('reference_no', '')
        
        # validate all required fields are not null
        if not development_type or not property_address or not answers:
            return jsonify({"error": "Development type or property address or answers is missing."}), 400
        # jsonify: convert python dicts and objs into json response objs
        
        # convert python obj into json string
        answers_json = json.dumps(answers)
        
        # insert new submission into db
        # conn = sqlite3.connect('/instance/logs.db')
        db = get_db()
        c = db.cursor() 
        
        c.execute('''
            INSERT INTO submissions (development_type, property_address, answers_json, timestamp, reference_no ) VALUES (?, ?, ?, ?, ?)''', (development_type, property_address, answers_json, submission_time, reference_no))
        # use ? as parameters placeholders to bind data to query => avoid SQL injection
        
        submission_id = c.lastrowid # generated value for autoincrement id col
        db.commit()
        # db.close()
        
        return jsonify({
            'message': 'Log stored successfully',
            # 'submission_id': submission_id,
            'reference_no': reference_no,
            'timestamp': submission_time
        })
    except Exception as e:
        return jsonify({'error': f'Failed to store log: {str(e)}'}), 500


init_app(app)
    
if __name__ == "__main__":
    app.run(debug=True)
