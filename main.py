import requests
from bs4 import BeautifulSoup

chiaogoo_result = requests.get('https://search.shopping.naver.com/search/all.nhn?query=%EB%9C%A8%EA%B0%9C%EC%8B%A4&cat_id=&frm=NVSHATC')

chiaogoo_soup = BeautifulSoup(chiaogoo_result.text, 'html.parser')

pagination = chiaogoo_soup.find('div', {
    'id': '_result_paging'
})

links = pagination.find_all('a');

pages = []
for link in links[:-1]:
    pages.append(int(link.string))
    
max_page = pages[-1]
print(max_page)