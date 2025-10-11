DROP TABLE IF EXISTS submissions;

CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        dev_type TEXT NOT NULL,
        property_address TEXT NOT NULL,
        answers_json TEXT NOT NULL,
        reference_no TEXT NOT NULL,
        timestamp TEXT NOT NULL
)