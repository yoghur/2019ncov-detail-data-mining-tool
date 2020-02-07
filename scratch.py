import time
import json
import requests
from datetime import datetime
import pandas
import numpy as np
from lxml import etree
import xlwt
def catch_data():
    url = 'http://ncov.html5.qq.com/api/getCommunity'
    reponse = requests.get(url = url).json()
    
    data = reponse['community']
    return data

temp = catch_data()
adresses = []
 



# for j in temp['安徽省']['滁州市'].keys():
#     print(j)
#     for k in temp['安徽省']['滁州市'][j]:
#             print(k['show_address'])



for province in temp.keys():
    workbook = xlwt.Workbook()
    for i in temp[province].keys():
        worksheet = workbook.add_sheet(i,cell_overwrite_ok=True)
        numofstate=0
        for j in temp[province][i].keys():
            for k in temp[province][i][j]:
                    adresses.append(k['show_address'])
            worksheet.write(0,numofstate,label='%s(%s个)'%(j,len(adresses)))
            for numofxiaoqu in range(len(adresses)):
                worksheet.write(numofxiaoqu+1,numofstate,label=adresses[numofxiaoqu])
            adresses=[]
            numofstate+=2
    workbook.save('%s.xls'%province)

       
