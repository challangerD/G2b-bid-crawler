from selenium import webdriver

driver = webdriver.Chrome('c:/users/chromedriver.exe')
url = 'www.g2b.go.kr:8101/ep/tbid/tbidFwd.do?bidSearchType=1'

driver.get(url)
time.sleep(5)

def industry():
    i_search = dirver.find_element_by_name('industryCd')
    i_search.send_key('0001')

def area():
    a_search = driver.find_element_by_id('area')
    for option in a_search.find_elements_by_tag_name('option')
        if option.text == '서울'
            option.click()
            break

def click_search():
    Search = driver.find_element_by_xpath('//div[@class="button4"]/a[@class="btn_mdl",contains(text(),"검색")]')
    Search.click()

industry()
area()
click_search()
