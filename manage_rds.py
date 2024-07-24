import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Database credentials
host = "prithesh-db01.cls8uu6iyupn.ap-northeast-1.rds.amazonaws.com"  # e.g. "your-db-instance.abcdefghijk.us-west-2.rds.amazonaws.com"
user = "admin"
password = "OIj9bqK8n0LCWQpEuhEm"
database = "prithesh-db01"

# Create connection
connection = create_connection(host, user, password, database)

# Create table
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
name TEXT NOT NULL,
age INT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB
"""
execute_query(connection, create_users_table)

# Insert data
insert_user = "INSERT INTO users (name, age) VALUES ('Alice', 30)"
execute_query(connection, insert_user)

insert_user2 = "INSERT INTO users (name, age) VALUES ('Bob', 25)"
execute_query(connection, insert_user2)

# Read data
select_users = "SELECT * FROM users"
users = read_query(connection, select_users)
for user in users:
    print(user)
