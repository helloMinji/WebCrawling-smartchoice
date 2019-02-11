#coding: utf-8

### 시/군/구 선택, 최종결과 반환

from connect import driver
from dong import setdong
import pandas as pd
import time

def setGu(cityvalue):
    guname = driver.find_element_by_xpath("//select[@name='area2']") # 모든 구 이름 가져오기
    gulist = guname.text.split()[1:]
    
    labels = ['시/도','시/군/구','동/읍/면','서비스사업자','전송속도d','전송속도u','접속성공율d','접속성공률u','전송성공율d','전송성공율u','지연','손실율']
    result = pd.DataFrame(columns=labels)
    
    for index in gulist:
        gu = driver.find_element_by_xpath("//option[@value='" + index + "']")
        gu.click()
        #print('>',gu.text) 구 클릭이 잘 됐는지 확인
        time.sleep(1)
    
        gutable = setdong(cityvalue, index)
        result = pd.concat([result, gutable])
    
    result = result.reset_index(drop=True)
        
    return(result)