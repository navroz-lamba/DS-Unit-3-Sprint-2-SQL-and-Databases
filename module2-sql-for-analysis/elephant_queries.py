import os
from dotenv import load_dotenv
import psycopg2

load_dotenv() # Loads content of the env

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

print(DB_NAME, DB_HOST, DB_PASSWORD, DB_USER)

exit()

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
### A "cursor", a structure to iterate over db records to perform queries
c = conn.cursor()
### An example query
c.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
print(c.fetchall())
