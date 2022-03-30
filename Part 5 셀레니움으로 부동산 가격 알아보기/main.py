from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import urllib.request

chrome_driver_path = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://realty.daum.net/home/villa/map")

search = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/input')
search.send_keys("광명시")
time.sleep(5)
button = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/button')
button.click()
time.sleep(5)


images = driver.find_element_by_class_name("css-1dbjc4n r-633pao")
images.click()
time.sleep(5)
# imgurl = driver.find_element_by_class_name("css-9pa8cd")
# price = driver.find_element_by_class_name("css-1563yu1")

time.sleep(60)