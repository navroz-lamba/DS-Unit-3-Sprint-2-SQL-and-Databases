import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd

load_dotenv() # Loading the content of .env file

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

#creating a connection  
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

# creating a cursor
cur = conn.cursor()

# creating a table 
cur.execute(""" DROP TABLE IF EXISTS titanic;
            CREATE TABLE titanic(
            Survived  BOOLEAN,
            Pclass INTEGER,
            Name VARCHAR,
            Sex VARCHAR,
            Age FLOAT,
            Sib_Spouse INTEGER,
            Par_Child INTEGER,
            Fare FLOAT) """)
# Coomit the changes
conn.commit()

# Using copy_from method load a csv into the table 
with open('titanic.csv', 'r') as f:
    next(f) # skip the header row
    cur.copy_from(f,'titanic', sep=',')
# Coomit the changes
conn.commit()


cur.close()
conn.close()