
import sqlite3
from bs4 import BeautifulSoup
import re,lxml
connective =sqlite3.connect('extraction.db')
access=connective.cursor()
try :
    access.execute("CREATE TABLE EXTRACTION ( ID INTEGER PRIMARY KEY, Posologie CHAR(50) )")
except : 
    access.execute("DROP TABLE EXTRACTION;")
    access.execute("CREATE TABLE EXTRACTION ( ID INTEGER PRIMARY KEY, Posologie CHAR(50) )")
html = open("corpus-medical_snt\concord.html","r",encoding="utf-8")
id=1
soup = BeautifulSoup(html,'lxml')
Posologie = soup.find_all("a")
#Posologie =re.findall('href="(([0-9]+) )+[0-9]*">(\w*)',soup.contents)
for href in Posologie:
    print(href)
    href_1=re.split(r">|<",str(href))
    
    poso=href_1[2]
    print(str(id)+" adding to the database :"+poso)
    try:
        
        access.execute("INSERT INTO EXTRACTION VALUES ("+str(id)+","+" \' "+str(poso).replace("'","''")+" \' "+")")
        id=id+1
    except:
        print("couldn't add to the data base ")
        input("there was an error while trying to add : "+str(poso)+" !!! press on any key to get to the other line")




req="select * from EXTRACTION"
result = access.execute(req)



connective.commit()
access.close()
connective.close()
