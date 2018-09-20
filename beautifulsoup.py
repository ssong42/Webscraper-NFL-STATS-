from requests import get
from bs4 import BeautifulSoup

url = "https://www.49ers.com/team/players-roster/"

response = get(url)
nfl = BeautifulSoup(response.content, 'html.parser')

# 1) parsing a page with hierarchical structure

#print(nfl.a)
#print(nfl.p)

nfl_body = nfl.body

a = list(nfl_body.contents[0].next_sibling.next_sibling.next_sibling.contents[5])
print(a)
