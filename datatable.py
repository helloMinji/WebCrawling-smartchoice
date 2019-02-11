#coding: utf-8

from connect import driver
from bs4 import BeautifulSoup
import pandas as pd

def gettable(cityvalue, guvalue, dongvalue):
    labels = ['시/도','시/군/구','동/읍/면','서비스사업자','전송속도d','전송속도u','접속성공율d','접속성공률u','전송성공율d','전송성공율u','지연','손실율']

    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    table = soup.find('div', class_="databoard")
    
    existData = soup.find('td', class_="nodata")
    if existData!=None :
        nodata = [cityvalue, guvalue, dongvalue, 'NAN', 0, 0, 0, 0, 0, 0, 0, 0]
        temp = pd.DataFrame([nodata], columns=labels)
        
    else:    
        tbody = table.tbody
        body = str(tbody.get_text()).split()
        body.remove('전체')
        
        if len(body)<32 :
            total = [cityvalue, guvalue, dongvalue,'전체'] + body[5:]
            temp = pd.DataFrame([total], columns=labels)
            
        else:
            skt = body[5:13]
            kt = body[13:21]
            lg = body[21:29]
            total = body[29:]
    
            skt = [cityvalue, guvalue, dongvalue,'skt'] + skt
            kt = [cityvalue, guvalue, dongvalue,'kt'] + kt
            lg = [cityvalue, guvalue, dongvalue,'lg'] + lg
            total = [cityvalue, guvalue, dongvalue,'전체'] + total
    
            temp = pd.DataFrame([skt,kt,lg,total], columns=labels)
    
    #print(temp) temp가 잘 들어갔는지 확인
    
    return(temp)