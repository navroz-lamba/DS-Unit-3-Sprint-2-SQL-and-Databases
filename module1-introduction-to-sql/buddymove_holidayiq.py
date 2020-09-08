import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')
# Fill in the blank spaces with '_'
df = df.rename(columns=lambda x: x.replace(" ","_"))
# connecting the file 
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
# Making a cursor 
c = conn.cursor()

# insert the values from df into sql 
df.to_sql('review', conn, if_exists='replace')
# print(c.execute("SELECT * FROM review").fetchall())

""" Count how many rows you have - it should be 249! """
def count_rows():
    print(c.execute("SELECT COUNT(*) FROM review").fetchall())


""" How many users who reviewed at least 100 `Nature` in the category also
  reviewed at least 100 in the `Shopping` category? """
def atleast_100_reviews():
    c.execute(""" SELECT COUNT(DISTINCT USER_ID) AS Total_Users FROM
            (SELECT User_Id ,Nature, Shopping FROM review
            WHERE Nature >=100
            AND Shopping >=100) """)
    print(c.fetchall())


""" What are the average number of reviews for each category? """
def avg_number_of_reviews():
    c.execute(""" SELECT round(AVG(Shopping),2) FROM review """)
                
    print(c.fetchall())


