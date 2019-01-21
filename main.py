#coding: utf-8

from year import setYear
from city import setCity
from gu import setGu

# 광역시/도 목록 : 서울특별시, 부산광역시, 대구광역시, 인천광역시, 울산광역시, 대전광역시, 광주광역시, 세종특별자치시, 강원도, 경기도, 경상남도, 경상북도, 충청남도, 충청북도, 전라남도, 전라북도, 제주특별자치도

Year = '2017'
City = '서울특별시'

setYear(Year)
setCity(City)
result_df = setGu(City)