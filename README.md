# 스마트초이스 국내 품질평가 결과 웹 크롤링

스마트초이스(www.smartchoice.or.kr)의 국내 품질평가 데이터 크롤링 프로그램입니다.     
2017년, 2016년 LTE 전체 데이터를 선택했을 경우에 대해 테스트가 완료되었습니다.     

<br>
<br>
                                  
               
---------------------------------------------------------------

### > How to Use

#### Setup

(이 코드는 python 3.6.5 에서 작성되었습니다.)<br>
다음을 미리 설치해주세요.
- chromewebdriver.exe (경로를 알아두세요!)
- selenium
- pandas
- bs4

<br>
<br>

                              
---------------------------------------------------------------

### > 코드 설명

connect.py : chromedriver를 이용하여 크롤링할 화면을 확인할 수 있다.<br>
   <br>
year.py : 년도 선택. 실행 시 박스의 내용이 바뀐다. 직접 수정을 통해 연도 변경 가능.<br>
   <br>
city.py : 광역시/도 선택. 실행 시 박스의 내용이 바뀐다. 직접 수정을 통해 광역시/도 변경 가능.<br>
   <br>
gu.py : 시/군/구 선택, 최종결과 테이블 반환. 해당 광역시/도의 모든 시/군/구를 차례대로 모두 선택하고 setdong을 실행한다.<br>
   <br>
dong.py : 동/읍/면/ 선택, 시/군/구 단위로 모은 테이블 반환. 해당 시/군/구의 모든 동/읍/면을 차례대로 모두 선택하고 gettable을 실행한다.<br>
   <br>
datatable.py : 결과 테이블을 크롤링.<br>
   <br>
main.py

<br>
<br>

                                                 

---------------------------------------------------------------

### > 시행 착오


![image](https://user-images.githubusercontent.com/41939828/51453655-051a2980-1d84-11e9-9fd5-0926407562cf.PNG)
> 실행되다가 중간쯤 멈춰버리는 일이 계속 발생했다.
> 검색해보니 화면이 전환되는데 delay가 있기 떄문에 명령의 element가 변환되기 전의 페이지에는 존재하지 않으니까 element가 없다고 하는 오류라고 한다.
>   
> :arrow_right: .click() 뒤에는 무조건 time.sleep(1)을 넣어서 화면이 전환되는 것을 기다리게 했다.
           
<br>
<br>
<br>
<br>

                                              
![image](https://user-images.githubusercontent.com/41939828/51453680-2c70f680-1d84-11e9-8478-56d52f515e28.png)
> 데이터가 없는 지역이 있다.
> 이 경우 datatable.py 에서 크롤링한 데이터에서 '전체'라는 단어를 삭제하게끔 해놓았는데 이 부분에서 오류가 발생한다.
>  
> :arrow_right: 코드를 다음과 같이 수정하였다.
```python
 existData = soup.find('td', class_="nodata")
    if existData!=None :
        nodata = [cityvalue, guvalue, dongvalue, 'NAN', 0, 0, 0, 0, 0, 0, 0, 0]
        temp = pd.DataFrame([nodata], columns=labels)
        
    else:    
        ### 기존과 같은 내용
```

<br>
<br>
<br>
<br>

                                                    
![image](https://user-images.githubusercontent.com/41939828/51453695-414d8a00-1d84-11e9-8aac-75bef9aa3a1b.png)
> 데이터가 전체 데이터만 있는 지역이 있다.
> 이 경우 skt로 데이터가 들어가고 나머지 부분은 nan 처리가 된다.
>  
> :arrow_right: 코드를 다음과 같이 수정하였다.
```python
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
```
