from selenium import webdriver

driver = webdriver.Chrome('c:/users/chromedriver.exe')
url = 'www.g2b.go.kr:8101/ep/tbid/tbidFwd.do?bidSearchType=1'

driver.get(url)
time.sleep(5)

def industry ():
    industry_search = dirver.find_element_by_id('')
#industry()


def area ():
    area_search = driver.find_element_by_id('area')
    area_search.select_by_index(11)
area()
