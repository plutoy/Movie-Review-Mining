import sqlite3
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")


c.execute("DROP TABLE IF EXISTS IMDBsow")
sql="""CREATE TABLE IMDB (
       id INTEGER PRIMARY KEY,
       username CHAR(10),
       date CHAR(10) NOT NULL,
       content TEXT NOT NULL,
       rating CHAR(2))"""

c.execute(sql)
print("table OK!")
conn.commit()

c.execute("DROP TABLE IF EXISTS Metasow")
sql="""CREATE TABLE Metasow (
       id INTEGER PRIMARY KEY,
       username CHAR(10),
       date CHAR(10) NOT NULL,
       content TEXT NOT NULL,
       rating CHAR(2))"""

c.execute(sql)
print("table OK!")
conn.commit()



c.execute("DROP TABLE IF EXISTS Tomatosow")
sql="""CREATE TABLE Tomatosow (
       id INTEGER PRIMARY KEY,
       username CHAR(10),
       date CHAR(10) NOT NULL,
       content TEXT NOT NULL,
       rating CHAR(2))"""

c.execute(sql)
print("table OK!")
conn.commit()




conn.close()
