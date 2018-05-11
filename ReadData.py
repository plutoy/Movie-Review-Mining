#connect to the DB
import sqlite3
import re
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")

#DateConverter for Meta
import re
def ConvertDateT(date):
    datelist={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
    mon=re.sub(r'\d|\s|,', "", date)
   
    date2=re.sub("\s|,","",re.sub(mon,datelist[mon],date))
    if len(date2)==7:
        date2=re.sub('(\d{2})(\d{1})(\d{4})',r"\2\1\3",date2)
        date2="0"+date2
    date3=re.sub('(\d{2})(\d{2})(\d{4})',r"\3\1\2",date2)
    return date3
    
#Read MetaData
metalis=[]
cursor = c.execute("""SELECT id,username,date,content,rating
                      FROM Metasow
                      ORDER BY date""")
for row in cursor:
    redic={}
    d=ConvertDateT(row[2])
    redic={"id":row[0],"username":row[1],"date":d,"content":row[3],"rating":row[4]}
    metalis.append(redic)

conn.close()
print(metalis[0:3])

#DateConverter for Tomato
import re
def ConvertDate(date):
    datelist={"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    mon=re.sub(r'\d|\s|,', "", date)
   
    date2=re.sub("\s|,","",re.sub(mon,datelist[mon],date))
    if len(date2)==7:
        date2="0"+date2
    date3=re.sub('(\d{2})(\d{2})(\d{4})',r"\3\1\2",date2)
    return date3
    
#Read TomatoData
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")

metalis=[]
cursor = c.execute("""SELECT id,date,content,rating
                      FROM Tomatosow""")
for row in cursor:
    redic={}
    d=ConvertDate(row[1])
    redic={"id":row[0],"date":d,"content":row[2],"rating":row[3]}
    metalis.append(redic)

conn.close()
print(metalis[0:3])


#Read IMDB
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")

imdblis=[]
cursor = c.execute("""SELECT id,date,content,rating
                      FROM IMDBsow""")
for row in cursor:
    redic={}
    redic={"id":row[0],"date":row[1],"content":row[2],"rating":row[3]}
    imdblis.append(redic)

conn.close()
print(imdblis[0:3])

