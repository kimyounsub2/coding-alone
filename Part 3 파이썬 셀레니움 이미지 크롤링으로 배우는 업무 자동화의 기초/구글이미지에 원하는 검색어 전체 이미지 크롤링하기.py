from matplotlib import image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 해당사이트에서 검색 입력후 앤터기능을 하기위해
import time # 조회 후 로딩시간을 기다려주기 위해
import urllib.request # 이미지 주소를 받기 위해

driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver')
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("아스날")
elem.send_keys(Keys.RETURN)

# 구글 이미지에서 스크롤을 최대한으로 내려 이미지를 가져올수 있게 하는 코드
SCROLL_PAUSE_SEC = 1

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 1초 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
           break
    last_height = new_height
#############################################

# driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click() 사진 한장을 가져오기 위해서 
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
    except:
        pass
driver.close()