from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import csv
from bs4 import BeautifulSoup


browser = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(browser)
driver.get("https://realty.daum.net/home/villa/map")
html = driver.page_source
soup = BeautifulSoup(html)


search = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/input')
name = search.send_keys("광명시")
time.sleep(4)


button = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/button')
button.click()
time.sleep(4)



link = driver.find_elements_by_css_selector(".css-1dbjc4n.r-14lw9ot.r-eqz5dr")


for property_books in link:
    driver.execute_script("arguments[0].click();", property_books)
    time.sleep(4)

    details = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[6]/div/div[1]/div[1]")
    driver.execute_script("arguments[0].click();", details)
    time.sleep(3)

    # 여기서 for문 다음것을 가져오지 못함
    price_titel = driver.find_element_by_class_name("#css-1dbjc4n r-14lw9ot r-eqz5dr").text 
    print(price_titel)
# for imgurl in img:
#     imgurl['src']

# imgurl = img.get_attribute("src")
    # a = {}
    # propertys_all = {
    #     "매매" : price_titel
    # }
    
    
            
    # with open("property.csv", mode="a", encoding='UTF-8') as file:
    #     for propertys in propertys_all:
    #         file.write(f"{propertys}\n")

            
    
# with open("property.csv", mode="w", encoding='UTF-8') as file:
#     for propertys in property_books:
#         file.write(f"{propertys}\n")
