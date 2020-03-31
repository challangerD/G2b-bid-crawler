from selenium import webdriver

driver = webdriver.Chrome('c:/users/chromedriver.exe')
url = 'http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidFwd.do?bidSearchType=1'

def industry ():
    driver.get(url)
    time.sleep(5)
    industry_search = driver.find_element_by_class_name('f1').find_element_by_class_name('btn_finder')
    industry_search.excute_script('script')
industry()
