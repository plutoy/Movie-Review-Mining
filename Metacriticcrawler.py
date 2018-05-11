from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
import sqlite3

#extract the normal review from IMDB and save into sqliteDB
conn=sqlite3.connect('MovieReview.db3')
c = conn.cursor()
print("connect successfully")

sql3="""INSERT INTO Metasow (username,date,content,rating)
        VALUES (:username,:date,:content,:rating)"""

d = webdriver.Chrome()
d.get('http://www.metacritic.com/movie/the-shape-of-water/user-reviews')

r=d.page_source
redic={}
soup=BeautifulSoup(r,'lxml')
review=soup.find_all("div",class_="review pad_top1")

for i in review:
    if i.find("div",class_="metascore_w user large movie negative indiv") is not None:
        redic["rating"]=i.find("div",class_="metascore_w user large movie negative indiv").get_text()
    elif i.find("div",class_="metascore_w user large movie mixed indiv") is not None:
        redic["rating"]=i.find("div",class_="metascore_w user large movie mixed indiv").get_text()
    elif i.find("div",class_="metascore_w user large movie positive indiv") is not None:
        redic["rating"]=i.find("div",class_="metascore_w user large movie positive indiv").get_text()
    else:
        redic["rating"]="10"
    redic["username"]=i.find("span",class_="author").a.get_text()
    redic["date"]=i.find("span",class_="date").get_text()
    j=i.find("div",class_="review_body")
    try:
        redic["content"]=j.find("span",class_="blurb blurb_expanded").get_text()
    except:
        redic["content"]=j.find("span").get_text()
    c.execute(sql3,{"username":redic["username"],"date":redic["date"],"content":redic["content"],"rating":redic["rating"]})
    conn.commit()
    
d = webdriver.Chrome()
d.get('http://www.metacritic.com/movie/the-shape-of-water/user-reviews?page=1')

r=d.page_source
redic={}
soup=BeautifulSoup(r,'lxml')
review=soup.find_all("div",class_="review pad_top1")

for i in review:
    if i.find("div",class_="metascore_w user large movie negative indiv") is not None:
        redic["rating"]=i.find("div",class_="metascore_w user large movie negative indiv").get_text()
    elif i.find("div",class_="metascore_w user large movie mixed indiv") is not None:
        redic["rating"]=i.find("div",class_="metascore_w user large movie mixed indiv").get_text()
    elif i.find("div",class_="metascore_w user large movie positive indiv") is not None:
        redic["rating"]=i.find("div",class_="metascore_w user large movie positive indiv").get_text()
    else:
        redic["rating"]="10"
    redic["username"]=i.find("span",class_="author").a.get_text()
    redic["date"]=i.find("span",class_="date").get_text()
    j=i.find("div",class_="review_body")
    try:
        redic["content"]=j.find("span",class_="blurb blurb_expanded").get_text()
    except:
        redic["content"]=j.find("span").get_text()
    c.execute(sql3,{"username":redic["username"],"date":redic["date"],"content":redic["content"],"rating":redic["rating"]})
    conn.commit()
conn.close()

