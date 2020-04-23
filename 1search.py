from selenium import webdriver
import datetime
import requests
from bs4 import BeautifulSoup
driver = webdriver.Chrome('c:/users/chromedriver.exe')

#검색기간설정,2020%2F04%2F15
ToD = datetime.today().strftime('%Y%m%d')
d = datetime.timedelta(days = 3)
FromD = ToD - d

#토목,조경 공종 코드 입력
IndstCd = input('토목: 0001, 조경:0005')

url = 'http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?searchType=1&bidSearchType=1&searchDtType=1&fromBidDt={FromD}&toBidDt={ToD}&area=11&industryCd={IndstCd}'

driver.get(url)
