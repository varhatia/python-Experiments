#!/usr/bin/env python
# coding: utf-8

# In[53]:


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c=r.content

soup=BeautifulSoup(c,"html.parser")

all=soup.find_all("div",{"class":"propertyRow"})

all[0].find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ","")
page_nr=soup.find_all("a", {"class":"Page"})[-1].text

l = []

base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
for page in range(0,int(page_nr)*10,10):
    print(base_url+str(page))
    r=requests.get(base_url+str(page), headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    #print(soup.prettify())
    
    for item in all:
        d={}
        d["Address"]=item.find_all("span", {"class":"propAddressCollapse"})[0].text
        d["Locality"]=item.find_all("span", {"class":"propAddressCollapse"})[1].text
        d["Price"]=item.find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ","")
        try:
            d["Bed"]=item.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Bed"]=None

        try:
            d["SqFt"]=item.find("span", {"class":"infoSqFt"}).find("b").text
        except:
            d["SqFt"]=None

        try:
            d["Bath"]=item.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
            d["Bath"]=None

        try:
            d["Half Bath"]=item.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
            d["Half Bath"]=None

        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
                #print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    d["Lot Size"]=feature_name.text

        l.append(d)
l

import pandas
df=pandas.DataFrame(l)
df
#df.to_csv("Output.csv")    


# In[ ]:




