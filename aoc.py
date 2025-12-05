from requests import get
from bs4 import BeautifulSoup

r = get('https://adventofcode.com/2025/day/2')
s = BeautifulSoup(r.text, 'html.parser')

for a in s.find_all('article', class_='day-desc'):
    print(a.get_text())
