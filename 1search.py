from selenium import webdriver

driver = webdriver.Chrome('c:/users/chromedriver.exe')
url = 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do?bidSearchType=1'

driver.get(url)
time.sleep(5)

def industry ():
    industry_search = driver.find_element_by_xpath("*[@id='industryCd']")
    industry_search.sendKey('0001')

#industry()
