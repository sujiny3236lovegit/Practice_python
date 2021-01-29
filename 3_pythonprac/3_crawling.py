import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
#
# print(title.text)
# print(title['href'])

# old_content > table > tbody > tr:nth-child(2)
# old_content > table > tbody > tr:nth-child(3)
# old_content > table > tbody > tr

trs = soup.select('#old_content > table > tbody > tr')

# old_content > table > tbody > tr:nth-child(4) > td.title > div > a

for tr in trs:
    a_tag = tr.select_one('td.title > div > a')
    if a_tag is not None:
        # print(a_tag)
        title = a_tag.text
        print(title)
