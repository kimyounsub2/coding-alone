from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time 
from bs4 import BeautifulSoup



chrome_driver_path = 'C:/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://realty.daum.net/home/villa/map")


search = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[1]/input')
search.send_keys("광명시")
time.sleep(4)
button = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/div/div[2]/button')
button.click()
time.sleep(4)


images = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div[2]')
driver.execute_script("arguments[0].click();", images)
time.sleep(4)

html = driver.page_source
soup = BeautifulSoup(html)

# imgurl = driver.find_element_by_class_name("css-9pa8cd")

#price = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]")
price = soup.select_one('#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(1) > div.css-1563yu1.css-vcwn7f').text
# soup.select('상위태그명.클래스명 > 하위태그명.클래스명') 
#soup.select('#아이디명 > 태그명.클래스명)
print(price)



propertys = {
    "주소" : f"{price}",
    "이미지" :
    "매매" 
    "주차" 
    "엘리베이터"
    "입주가능일"
    "관리비"
    "구조"
    "면적(공급/전용)"
    "방향"
    "중공날짜"
    "층/건물층수"
    "건물종류"
    "주소"
    
}
print(propertys)
# with open("property.txt", mode="w", encoding='UTF-8') as file:
#     for property in propertys:
#         file.write(f"{property}\n")