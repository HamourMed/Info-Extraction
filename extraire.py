import requests
import re
from bs4 import BeautifulSoup as bs
import sys
import codecs
abc='abcdefghijklmnopqrstuvwxyz'
url='http://127.0.0.1:'+sys.argv[2]+'/VIDAL/vidal-Sommaires-Substances-'

info1=open('infos1.txt', 'wt', encoding='utf-8')
dic=open('subst.dic', 'wt', encoding='utf-16le')
dic.write('\ufeff')

cp=0
for i in range(abc.find(sys.argv[1][0].lower()),abc.find(sys.argv[1][-1].lower())+1) :
    lettre=abc[i]
    res=requests.get(url+lettre+'.htm')
    soup=bs(res.content,'lxml')
    s=soup.prettify()    
    temp=re.search(r'<ul class="substances list_index has_children" id="letter.">[\s\S]*?</ul>',s)
    listSub=re.findall(r'<a href="Substance/.*?">\s*(.+)\s*</a>',temp.string)
    cpL=0
    for j in listSub:
        cpL+=1
        cp+=1
        dic.write(j+",.N+subst\n")
    info1.write("Le nombre d'entité pour la lettre "+lettre.upper()+" est : "+str(cpL)+"\n")

info1.write("Le nombre total d'entités est : "+str(cp))



info1.close()
dic.close()
print('Done')








