import os
import sys
import logging
from flask import Flask, request, jsonify
import psycopg2

#Create a logger
logger = logging.getLogger("ideaBox")

# Setup flask application.
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# PostgreSQL connection settings here
def create_db_connection_string_from_env_vars() -> str:
    """read environment variables and build libpq connection string"""
    # read each env var and check that it gets a value, otherwise print a message to user and exit
    db_host = os.getenv("DB_HOST", None)
    if not db_host:
        print("ERROR: 'DB_HOST' env var not set.")
        sys.exit(1)

    db_name = os.getenv("DB_NAME", None)
    if not db_name:
        print("ERROR: 'DB_NAME' env var not set.")
        sys.exit(1)

    db_user = os.getenv("DB_USER", None)
    if not db_user:
        print("ERROR: 'DB_USER' env var not set.")
        sys.exit(1)

    db_password = os.getenv("DB_PASSWORD", None)
    if not db_password:
        print("ERROR: 'DB_PASSWORD' env var not set.")
        sys.exit(1)

    db_port = os.getenv("DB_PORT", None)
    if not db_port:
        print("ERROR: 'DB_PORT' env var not set.")
        sys.exit(1)

    connection_string = f"host={db_host} port={db_port} user={db_user} password={db_password} dbname={db_name}"
    print(connection_string)
    return connection_string


DB_CONNECTION_STRING = create_db_connection_string_from_env_vars()


def create_connection():
    """Function establishing connection to database"""
    conn = None
    try:
        conn = psycopg2.connect(DB_CONNECTION_STRING)
    except psycopg2.DatabaseError as err:
        print(err)
    return conn

@app.route('/submit_idea', methods=['POST'])
def submit_idea():
    try:
        idea = request.json['idea']
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ideas (content) VALUES (%s)",(idea,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message':'Idea submitted succesfully'}), 201
    except Exception as e:
        return jsonify({'error':str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)