from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse


options = webdriver.ChromeOptions()
# options.add_argument('headless')

chrome_driver = webdriver.Chrome('C:/chromedriver.exe')
# chrome_driver = webdriver.Chrome('chrome/chromedriver', options=options)

chrome_driver.implicitly_wait(3)
# 중고나라 URL
url = 'https://cafe.naver.com/joonggonara'
# 중고나라 네이버 카페 아이디
joonggonara_id = 10050146
# 검색어
search_keyword = '로말레오'.encode('cp949')
# url 인코딩 진행
encode_search_keyword = parse.quote(search_keyword)

full_url = f'{url}?iframe_url=/ArticleSearchList.nhn?search.clubid={10050146}%26search.searchBy=0%26search.query={encode_search_keyword}'

chrome_driver.get(full_url)
# iframe으로 변경
chrome_driver.switch_to.frame("cafe_main")

html = chrome_driver.page_source
bs = BeautifulSoup(html, 'lxml')

# 검색 결과 리스트에 해당되는 태그들만 추출
td_results = bs.find_all('td', class_='td_article')

print(td_results)
