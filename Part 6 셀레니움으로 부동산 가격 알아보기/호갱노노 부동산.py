from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import csv
from bs4 import BeautifulSoup



browser = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(browser)
driver.get("https://hogangnono.com/")
html = driver.page_source
soup = BeautifulSoup(html)



search = driver.find_element_by_class_name("keyword")
name = search.send_keys("광명시")
time.sleep(2)


button = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/div[3]/div/div[2]/fieldset/div/div[1]/button")
link = driver.execute_script("arguments[0].click();", button)
time.sleep(4)

# 상위클래스를 찾고 하위 태그로 연결 
parentElement = driver.find_element_by_css_selector(".search-list.apt-list")
elementList = parentElement.find_elements_by_tag_name("a")



for property_book in elementList:
    driver.execute_script("arguments[0].click();", property_book)
    time.sleep(4)
    
    
    pricetitle = driver.find_element_by_class_name("price-group")
    price = pricetitle.find_element_by_tag_name("div").text
    addresstitle = driver.find_element_by_class_name("address-info")
    address = addresstitle.find_element_by_tag_name('h2').text
    
 
    property_all = [
        {
        "최근 실거래 기준 1개월 평균" : price,
        "주소" : address,
        }
    ]
    
            
    with open("property.csv", mode="a", encoding='UTF-8') as file:
        for propertys in property_all:
            file.write(f"{propertys}\n")
    time.sleep(4)
    
    
    
    
    # backtitle = driver.find_element_by_class_name("btn-back")
    # back = backtitle.find_element_by_tag_name("span")
    # driver.execute_script("arguments[0].click();", back)
            