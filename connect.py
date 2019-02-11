#coding: utf-8

from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe가 있는 주소')

driver.get('http://www.smartchoice.or.kr/smc/smartreport/evaluatePage.do')