import os
from app import create_app, db

app = create_app()

# Ensure the directory for the database file exists
BASEDIR = os.path.abspath(os.path.dirname(__file__))
db_path = f'{os.path.join(BASEDIR, "data", "upkeephub.db")}'
db_dir = os.path.dirname(db_path)
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
