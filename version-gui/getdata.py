from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
#from collections import OrderedDict
import time

driver = webdriver.Chrome('chromedriver의 주소')
driver.get('http://www.smartchoice.or.kr/smc/smartreport/evaluatePage.do')


### 년도 선택
def setYear(y):
    year = driver.find_element_by_xpath("//option[@value='" + y + "']")  # 파라미터에 접근
    year.click()  # 클릭 -> 박스의 내용이 바뀐다


### 광역시/도 선택
def setCity(v):
    city = driver.find_element_by_xpath("//option[@value='" + v + "']")  # 파라미터에 접근
    city.click()  # 클릭 -> 박스의 내용이 바뀐다
    time.sleep(1)


### 시/군/구 선택, 최종결과 반환
def setGu(cityvalue):
    guname = driver.find_element_by_xpath("//select[@name='area2']")  # 모든 구 이름 가져오기
    gulist = guname.text.split()[1:]

    labels = ['시/도', '시/군/구', '동/읍/면', '서비스사업자', '전송속도d', '전송속도u', '접속성공율d', '접속성공률u', '전송성공율d', '전송성공율u', '지연', '손실율']
    result = pd.DataFrame(columns=labels)

    for index in gulist:
        gu = driver.find_element_by_xpath("//option[@value='" + index + "']")
        gu.click()
        # print('>',gu.text) 구 클릭이 잘 됐는지 확인
        time.sleep(1)

        gutable = setdong(cityvalue, index)
        result = pd.concat([result, gutable])

    result = result.reset_index(drop=True)

    return (result)


### 동/읍/면 선택, 시/군/구 단위로 모은 table 반환
def setdong(cityvalue, guvalue):
    donglist = []
    index = ''

    dongname = driver.find_element_by_xpath("//select[@name='area3']")
    donglist = dongname.text.split()[1:]

    labels = ['시/도', '시/군/구', '동/읍/면', '서비스사업자', '전송속도d', '전송속도u', '접속성공율d', '접속성공률u', '전송성공율d', '전송성공율u', '지연', '손실율']
    dongtable = pd.DataFrame(columns=labels)

    for index in donglist:
        dong = driver.find_element_by_xpath("//option[@value='" + index + "']")
        dong.click()
        # print(dong.text, '클릭됨') 동 클릭이 잘 됐는지 확인
        time.sleep(1)

        driver.find_element_by_id('areaBtnSearch').click()
        # print('검색 클릭됨') 검색버튼이 잘 클릭됐는지 확인
        time.sleep(1)

        dongtable = pd.concat([dongtable, gettable(cityvalue, guvalue, index)])

    df = dongtable
    return (df)


### 결과 table 크롤링
def gettable(cityvalue, guvalue, dongvalue):
    labels = ['시/도', '시/군/구', '동/읍/면', '서비스사업자', '전송속도d', '전송속도u', '접속성공율d', '접속성공률u', '전송성공율d', '전송성공율u', '지연', '손실율']

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('div', class_="databoard")

    existData = soup.find('td', class_="nodata")
    if existData != None:
        nodata = [cityvalue, guvalue, dongvalue, 'NAN', 0, 0, 0, 0, 0, 0, 0, 0]
        temp = pd.DataFrame([nodata], columns=labels)

    else:
        tbody = table.tbody
        body = str(tbody.get_text()).split()
        body.remove('전체')

        if len(body) < 32:
            total = [cityvalue, guvalue, dongvalue, '전체'] + body[5:]
            temp = pd.DataFrame([total], columns=labels)

        else:
            skt = body[5:13]
            kt = body[13:21]
            lg = body[21:29]
            total = body[29:]

            skt = [cityvalue, guvalue, dongvalue, 'skt'] + skt
            kt = [cityvalue, guvalue, dongvalue, 'kt'] + kt
            lg = [cityvalue, guvalue, dongvalue, 'lg'] + lg
            total = [cityvalue, guvalue, dongvalue, '전체'] + total

            temp = pd.DataFrame([skt, kt, lg, total], columns=labels)

    # print(temp) temp가 잘 들어갔는지 확인

    return (temp)


def startpr(inputyear, inputcity, address):
    Year = inputyear
    City = inputcity

    setYear(Year)
    setCity(City)
    result_df = setGu(City)

    result_df.to_csv(address + "/" + Year + City + ".csv", mode='w', encoding='UTF-8')
    return 'ok'
