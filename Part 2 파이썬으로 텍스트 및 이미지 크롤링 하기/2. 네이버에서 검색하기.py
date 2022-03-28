from bs4 import BeautifulSoup
from urllib.request import urlopen




# response = urlopen("https://www.naver.com/") 아래줄과 같은 의미이다.
with urlopen("https://comic.naver.com/index") as response: # 검색할 홈페이지명
    soup = BeautifulSoup(response, "html.parser")
    i = 1
    for article in soup.select( "a.nclk_v2"):
        print(str(i)+ "위 : " + article.get_text)
