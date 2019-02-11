#coding: utf-8

### 광역시/도 선택

from connect import driver

def setCity(v):
    city = driver.find_element_by_xpath("//option[@value='" + v + "']") # 파라미터에 접근
    city.click() # 클릭 -> 박스의 내용이 바뀐다