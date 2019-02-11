#coding: utf-8

### 동/읍/면 선택, 시/군/구 단위로 모은 table 반환

from connect import driver
import pandas as pd
import time

def setdong(cityvalue, guvalue):
    
    donglist = []
    index = ''
    
    dongname = driver.find_element_by_xpath("//select[@name='area3']")
    donglist = dongname.text.split()[1:]
    
    labels = ['시/도','시/군/구','동/읍/면','서비스사업자','전송속도d','전송속도u','접속성공율d','접속성공률u','전송성공율d','전송성공율u','지연','손실율']
    dongtable = pd.DataFrame(columns=labels)
    
    for index in donglist:
        dong = driver.find_element_by_xpath("//option[@value='" + index + "']")
        dong.click()
        #print(dong.text, '클릭됨') 동 클릭이 잘 됐는지 확인
        time.sleep(1)
        
        driver.find_element_by_id('areaBtnSearch').click()
        #print('검색 클릭됨') 검색버튼이 잘 클릭됐는지 확인
        time.sleep(1)
        
        dongtable = pd.concat([dongtable, gettable(cityvalue, guvalue, index)])
        
    df = dongtable
    return(df)