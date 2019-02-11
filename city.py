#coding: utf-8

### 광역시/도 선택

from connect import driver

def setCity(year):
    citylist = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '울산광역시', '대전광역시', '광주광역시', '세종특별자치시', '강원도', '경기도', '경상남도', '경상북도', '충청남도', '충청북도', '전라남도', '전라북도', '제주특별자치도']
    
    for index in citylist:
        city = driver.find_element_by_xpath("//option[@value='" + index + "']") # 파라미터에 접근
        city.click() # 클릭 -> 박스의 내용이 바뀐다
        time.sleep(1)
        
        result_df = setGu(index)
        result_df.to_csv(year + index + ".csv", mode='w', encoding='UTF-8')
