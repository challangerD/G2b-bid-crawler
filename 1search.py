from selenium import webdriver

driver = webdriver.Chrome('c:/users/chromedriver.exe')
url = 'www.g2b.go.kr:8101/ep/tbid/tbidFwd.do?bidSearchType=1'

driver.get(url)
time.sleep(5)

def industry():
    i_search = dirver.find_element_by_name('industryCd')
    i_search.send_key('0001')

def area():
    a = driver.find_element_by_id('area')
    a_remove_onchange = driver.excute_script('arguments[0].removeAttribute("onchange")',a)
    a_remove_onchange.send_keys('11')

def click_search():
    Search = driver.find_element_by_xpath('//div[@class="button4"]/a[@class="btn_mdl",contains(text(),"검색")]')
    Search.click()

industry()
area()
click_search()
