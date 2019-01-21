#coding: utf-8

### 년도 선택

from connect import driver

def setYear(y):
    year = driver.find_element_by_xpath("//option[@value='" + y + "']") # 파라미터에 접근
    year.click() # 클릭 -> 박스의 내용이 바뀐다