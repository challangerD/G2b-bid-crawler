from selenium import webdriver
import datetime
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome('c:/users/chromedriver.exe')

#검색기간3일
toD = datetime.date.today().strftime('%Y%m%d')
d = datetime.datetime.timedelta(days = 3)
fromD = toD - d

#공종 코드 입력
indstCd = '0001'

url = 'http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&searchDtType=1&fromBidDt={fromD}&toBidDt={toD}&area=11&industryCd={indstCd}'

driver.get(url)
time.sleep(10)
