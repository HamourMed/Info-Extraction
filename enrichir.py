import re,sys

abc='abcdefghijklmnopqrstuvwxyz'
SubListCorp=[]
Corps=sys.argv[1]
Corpus=open(Corps,'rt', encoding='utf-8')

for i in Corpus.readlines():
    SubCorp=re.search('^[-*Ø]?\s?(\w{4,})\s:?\s?(\d+|,|\d+.\d)+\s?:?(\s(mg\s|MG|UI|ml|mcg|amp|iu|flacon|g|sachet|cc|cp|un\s|1/j|/j)(.+|\n)|(g|/j)\n|(mg)\s.+)',i,re.I)
    if SubCorp:
        if  SubCorp.group(1).lower() != 'vichy' \
            and SubCorp.group(1).lower() != 'foldine' \
            and SubCorp.group(1).lower() != 'hémoglobine' \
            and SubCorp.group(1).lower() != 'aspégic'  \
            and SubCorp.group(1).lower() != 'posologie'  \
            and SubCorp.group(1).lower() != 'puis':
                SubListCorp.append(SubCorp.group(1).lower()) 
                print(str(len(SubListCorp))+' : '+SubCorp.group(1).lower())
Corpus.close()
####################################################################################################

SubstCorp=open('subst_corpus.dic','wt', encoding='utf-16le')
SubstCorp.write('\ufeff')
for i in SubListCorp :
    SubstCorp.write(i+',.N+subst\n')
SubstCorp.close()    
######################################################################################################

info2=open('infos2.txt','wt', encoding='utf-8')
SubList=sorted(list(dict.fromkeys(SubListCorp)))
for i in abc :
    cp=0
    for j in SubList:
        if j[0]==i :
            cp+=1
            info2.write(j+',.N+subst\n')
    info2.write("-------------------Le nombre d'entités pour la lettre "+i.upper()+" est : "+str(cp)+"--------------------------------\n\n")

info2.write("---------------Le nombre total d'entités est "+str(len(SubList)))
info2.close()
######################################################################################################

info3=open('infos3.txt','wt', encoding='utf-8')
dic=open('subst.dic','rt',encoding='utf-16le')
temp=dic.readlines()
dic.close()
SubListEr=[]
SubListDic=[]
temp[0]=temp[0].replace("\ufeff",'')

for i in temp :
        SubListDic.append(i.replace(',.N+subst\n',''))

for i in SubList : 
    if not i in SubListDic :
        SubListEr.append(i)


for i in abc :
    cp=0
    for j in SubListEr:
        if j[0]==i :
            cp+=1
            info3.write(j+',.N+subst\n')
    info3.write("-------------------Le nombre d'entités pour la lettre "+i.upper()+" est : "+str(cp)+"--------------------------------\n\n")

info3.write("---------------Le nombre total d'entités est "+str(len(SubListEr)))
info3.close

dic=dic=open('subst.dic','wt',encoding='utf-16le')
dic.write('\ufeff')
for i in sorted(SubListDic+SubListEr) :
    dic.write(i+',.N+subst\n')

dic.close()

print("Done")