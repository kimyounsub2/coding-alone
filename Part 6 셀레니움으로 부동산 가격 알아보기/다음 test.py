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



link = driver.find_element_by_css_selector(".css-1dbjc4n.r-14lw9ot.r-eqz5dr")

driver.execute_script("arguments[0].click();", link)
time.sleep(4)

details = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[6]/div/div[1]/div[1]")
driver.execute_script("arguments[0].click();", details)
time.sleep(3)

    #soup.select('상위태그명.클래스명 > 하위태그명.클래스명') 
    #soup.select('#아이디명 > 태그명.클래스명)
# price_title = driver.find_element_by_css_selector(".css-1dbjc4n.r-glunga").text
price_titel = driver.find_element_by_css_selector(".css-1dbjc4n.r-19yat4t.r-qi0n3.r-c9eks5.r-1qxgc49").text
price = driver.find_element_by_css_selector(".css-1dbjc4n.r-glunga").text
    

# for imgurl in img:
#     imgurl['src']

# imgurl = img.get_attribute("src")
print(price_titel)
print(price)
