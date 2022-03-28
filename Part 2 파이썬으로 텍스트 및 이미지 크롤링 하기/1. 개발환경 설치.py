# 크롤링을 하기 위해서는 Beautiful Soup이라는 패키지 라이브러리를 사용해야한다.
# Beautiful Soup은 HTML 및 XML 구문을 분석하기 위한

from bs4 import BeautifulSoup
from urllib.request import urlopen


# response = urlopen("https://en.wikipedia.org/wiki/main_page") 아래줄과 같은 의미이다.
with urlopen("https://en.wikipedia.org/wiki/main_page") as response:
    soup = BeautifulSoup(response, "html.parser")
    for anchor in soup.find_all("a"):
        print(anchor.get("href","/"))