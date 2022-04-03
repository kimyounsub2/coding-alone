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


link = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[6]")
html = driver.page_source
soup = BeautifulSoup(html)
    
for property_books in link:
    images = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div/div[2]/div/div/div[2]/div/div/div[6]/div/div[2]')
    driver.execute_script("arguments[0].click();", images)
    time.sleep(4)

    details = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[6]/div/div[1]/div[1]")
    driver.execute_script("arguments[0].click();", details)
    time.sleep(3)

    #soup.select('상위태그명.클래스명 > 하위태그명.클래스명') 
    #soup.select('#아이디명 > 태그명.클래스명)
    price = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(2) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(2) > div > div.css-1dbjc4n.r-19yat4t.r-qi0n3.r-c9eks5.r-1qxgc49 > div.css-1dbjc4n.r-glunga > div:nth-child(1)")
    address = soup.select_one('#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(1) > div.css-1563yu1.css-vcwn7f')
    park = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(1) > div > div:nth-child(2) > div")
    Elevator = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div")
    move_in_date = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div")
    administration_cost = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(3) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(4) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div")

    Structure = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[5]/div[2]/div[2]/div")
    extent = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[6]/div[2]/div[2]/div")
    Direction = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[8]/div[2]/div[2]/div")
    completion_date = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[9]/div[2]/div[2]/div")
    floor = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[10]/div[2]/div[2]/div")
    type_building = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[4]/div/div[1]/div[2]/div/div/div[11]/div[2]/div[2]/div")
    subway = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(7) > div > div.css-1dbjc4n.r-14lw9ot > div:nth-child(2) > div > div > div")
    img = soup.select_one("#__next > div._app__Body-sc-1jr99cl-0.bQXLct > div > div.AptMapOfferLayoutStyle__DetailArea-sc-10mw0f7-2.RnHiG > div > div:nth-child(2) > div:nth-child(2) > div.css-1dbjc4n.r-150rngu.r-eqz5dr.r-16y2uox.r-1wbh5a2.r-11yh6sk.r-1rnoaur.r-1sncvnh > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div > img")
# for imgurl in img:
#     imgurl['src']

# imgurl = img.get_attribute("src")
    property_books = [
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
    
with open("property.csv", mode="w", encoding='UTF-8') as file:
    for property in property_books:
        file.write(f"{property}\n")