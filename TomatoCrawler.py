import sqlite3
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")


#DateConverter
import re
def ConvertDate(date):
    datelist={"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    mon=re.sub(r'\d|\s|,', "", date)
    print(mon)
    date2=re.sub("\s|,","",re.sub(mon,datelist[mon],date))
    if len(date2)==7:
        date2="0"+date2
    date3=re.sub('(\d{2})(\d{2})(\d{4})',r"\3\1\2",date2)
    return date3
    
    
#Mutipage mining of tomatoes
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")

sql3="""INSERT INTO Tomatosow (username,date,content,rating)
        VALUES (:username,:date,:content,:rating)"""

import requests
from bs4 import BeautifulSoup
import time
url="https://www.rottentomatoes.com/m/the_shape_of_water_2017/reviews/?type=user"

for i in range(95):
    if i==0:
        r=requests.get(url,timeout=5).text
    else:
        a=i+1
        page="page={}&".format(a)
        url2="https://www.rottentomatoes.com/m/the_shape_of_water_2017/reviews/?{}type=user".format(page)
        r=requests.get(url2,timeout=5).text
    
    soup=BeautifulSoup(r,'lxml')
    review=soup.find_all("div",class_="row review_table_row")
    for i in review:
        redic={}
        redic["username"]=i.find("a",class_="bold unstyled articleLink").get_text()
        redic["date"]=ConvertDate(i.find("span",class_="fr small subtle").get_text())
        redic["content"]=i.find("div",class_="user_review").get_text()
        try:
            star=i.find("span",class_="fl")
            try:
                starcounts=star.find_all("span",class_="glyphicon glyphicon-star")
                rating=0
                for i in starcounts:
                    rating+=1
            except:
                rating=0
            if "½" in star.get_text():
                rating+=0.5
        except:
            rating=0
        redic["rating"]=rating
        c.execute(sql3,{"username":redic["username"],"date":redic["date"],"content":redic["content"],"rating":redic["rating"]})
        conn.commit()
        time.sleep(2)
        
conn.close()
print("insert finished")
