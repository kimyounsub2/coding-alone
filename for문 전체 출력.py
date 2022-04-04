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

click = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[5]/div/div/div/div")

link = driver.find_elements_by_css_selector(".css-1dbjc4n.r-14lw9ot.r-eqz5dr")

for property_books in link:
    driver.execute_script("arguments[0].click();", property_books)
    time.sleep(4)

    details = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[6]/div/div[1]/div[1]")
    driver.execute_script("arguments[0].click();", details)
    time.sleep(3)

    #soup.select('상위태그명.클래스명 > 하위태그명.클래스명') 
    #soup.select('#아이디명 > 태그명.클래스명)
    price = driver.find_element_by_css_selector(".css-1dbjc4n.r-glunga").text
    address = soup.select_one('#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(1) > div.css-1563yu1.css-vcwn7f')
    park = driver.find_element_by_css_selector(".css-1dbjc4n.r-13awgt0.r-1mlwlqe.r-eqz5dr").text
    Elevator = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div")
    move_in_date = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div")
    administration_cost = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div")

    Structure = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[5]/div[2]/div[2]/div").text
    extent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[6]/div[2]/div[2]/div").text
    Direction = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[8]/div[2]/div[2]/div").text
    completion_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[9]/div[2]/div[2]/div").text
    floor = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[10]/div[2]/div[2]/div").text
    type_building = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[11]/div[2]/div[2]/div").text
    subway = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(7) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div")
    img = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(2) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div > img")
# for imgurl in img:
#     imgurl['src']

# imgurl = img.get_attribute("src")
 
    property_all = [
        {
        "매매" : price,
        "주소" : address,
        "주차" : park,
        "엘리베이터" : Elevator,
        "입주가능일" : move_in_date,
        "관리비" : administration_cost,
        "구조" : Structure,
        "면적(공급/전용)" : extent,
        "방향" : Direction,
        "중공날짜" : completion_date,
        "층/건물층수" : floor,
        "건물종류" : type_building,
        "인근전철역" : subway,
        "이미지URL" : img,
        }
    ]
    
            
    with open("property.csv", mode="a", encoding='UTF-8') as file:
        for propertys in property_all:
            file.write(f"{propertys}\n")

            
    
# with open("property.csv", mode="w", encoding='UTF-8') as file:
#     for propertys in property_books:
#         file.write(f"{propertys}\n")
