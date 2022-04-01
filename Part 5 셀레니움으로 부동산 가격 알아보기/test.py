from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
import urllib.request

chrome_driver_path = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://realty.daum.net/home/villa/items/30792877")

imgurl = driver.find_element_by_class_name("css-9pa8cd")
price = driver.find_element_by_class_name('css-1dbjc4n r-glunga')
print(price)

