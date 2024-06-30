import os
from database import init_db

DB_INIT_FLAG = 'db_initialized.flag'

def initialize_database():
    if not os.path.exists(DB_INIT_FLAG):
        print("Initializing database...")
        init_db()
        # Create a flag file to indicate that the DB has been initialized
        with open(DB_INIT_FLAG, 'w') as f:
            f.write('Database initialized')
        print("Database initialization complete.")
    else:
        print("Database already initialized. Skipping initialization.")

if __name__ == '__main__':
    initialize_database()