from flask import Flask, request, jsonify, render_template, send_from_directory, current_app, g 
from datetime import datetime 
import json
import sqlite3
import click 

import os 

# initialize a flask instance 
app = Flask(__name__, instance_path=os.path.join(os.path.dirname(__file__), 'instance'))

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

init_app(app)

