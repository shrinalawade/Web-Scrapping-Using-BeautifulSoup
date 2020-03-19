print("Welcome to Scrapping data from http://code.highcharts.com/mapdata/")
print ("Main Menu\n 1).Custom\n 2).Countries\n 3).Canada Provinces Admin 2\n 4).France Regions Admin 2\n 5).Germany Bundeslander Admin 2\n 6).Germany Bundeslander Admin 3\n 7).Neatherland Provinces\n 8).Norway Countries\n 9).USA States\n 10). USA Congressional Districts (113th)\n 11).Historical: Countries\n 12).Historical Norway Counties(2019)\n 13).Historical:France Regions Admin 2 (2015)\n ") 
n = int(input("Enter your choice:"))
if(n not in range(1,14)):
    print("Invalid input, please re-enter again")
m = n-1

import pandas as pd
import requests
from bs4 import BeautifulSoup
import sys
import json
import time


try:
    wiki='http://code.highcharts.com/mapdata/'
    data=requests.get(wiki)
    data=BeautifulSoup(data.content,'html.parser')
    contData = data.find("div",{'id':'zt-mainframe'}).find("div",{'class':'container'})
    output1 = contData.find_all('ul')[m].find_all("li")
    for dt in output1:
        start = 'class="GeoJSON" href="'
        end = '"><span>GeoJSON<'
        url = str(dt).split(start)[1].split(end)[0]
        finalURL = "http://code.highcharts.com/mapdata/"+url
        jsonData1 = BeautifulSoup(requests.get(finalURL).content,"lxml").get_text()
        y = json.loads(jsonData1)
        name = y['title']+str(".json")
        with open(name, 'w') as fp:
            json.dump(y, fp)
    print("-------------------Scrapping completed--------------------------------------")    
except Exception as e:
    endDate = time.strftime("%Y-%m-%d %H:%M:%S")
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
    print(e)
    





