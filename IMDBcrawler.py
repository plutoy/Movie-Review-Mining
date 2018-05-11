import requests
from bs4 import BeautifulSoup
import re
import sqlite3
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")


#DateConverter
def ConvertDate(date):
    datelist={"January":"01","February":"02","March":"03","April":"04","May":"05","June":"06","July":"07","August":"08","September":"09","October":"10","November":"11","December":"12"}
    mon=re.sub(r'\d|\s', "", date)
    date2=re.sub("\s","",re.sub(mon,datelist[mon],date))
    if len(date2)==7:
        date2="0"+date2
    date3=re.sub('(\d{2})(\d{2})(\d{4})',r"\3\2\1",date2)
    return date3
    
import time
drive=webdriver.Chrome()

drive.get("https://www.imdb.com/title/tt5580390/reviews?ref_=tt_ql_3")
element=drive.find_element_by_id("load-more-trigger")
time.sleep(5)
for i in range(39):
    element.click()
    time.sleep(2)
    
#extract the normal review from IMDB and save into sqliteDB
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")

redic={}
r=drive.page_source
soup=BeautifulSoup(r,'xml')

#print(soup)
review=soup.find_all("div",class_="lister-item mode-detail imdb-user-review  collapsable")

sql3="""INSERT INTO IMDBsow (username,date,content,rating)
        VALUES (:username,:date,:content,:rating)"""

for i in review:
    
    redic["username"]=i.a.get_text()
    i.find("span",class_="review-date").get_text()
    redic["date"]=ConvertDate(i.find("span",class_="review-date").get_text())
    rating=i.find('span').get_text()
    try:
        rating2=re.search("\d{1,2}",rating).group()
        redic["rating"]=rating2
    except:
        redic["rating"]=10 #please input the rating
    try:
        redic["content"]=i.find('div',class_="text show-more__control").get_text()
    except:
        redic["content"]=i.find('div',class_="text show-more__control clickable").get_text()
    
    c.execute(sql3,{"username":redic["username"],"date":redic["date"],"content":redic["content"],"rating":redic["rating"]})
    conn.commit()
    
#Spoil review crawler
review2=soup.find_all("div",class_="lister-item mode-detail imdb-user-review  with-spoiler")
for i in review2:
    
    redic["username"]=i.a.get_text()
    i.find("span",class_="review-date").get_text()
    redic["date"]=ConvertDate(i.find("span",class_="review-date").get_text())
    rating=i.find('span').get_text()
    try:
        rating2=re.search("\d{1,2}",rating).group()
        redic["rating"]=rating2
    except:
        pass
    try:
        redic["content"]=i.find('div',class_="text show-more__control").get_text()
    except:
        redic["content"]=i.find('div',class_="text show-more__control clickable").get_text()

    c.execute(sql3,{"username":redic["username"],"date":redic["date"],"content":redic["content"],"rating":redic["rating"]})
    conn.commit()


conn.close()
