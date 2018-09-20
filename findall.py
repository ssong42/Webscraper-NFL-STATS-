from requests import get
from bs4 import BeautifulSoup

url = "https://www.49ers.com/team/players-roster/"

response = get(url)
nfl = BeautifulSoup(response.content, 'html.parser')

nfl_main = nfl.find(id="main-content")
print(nfl_main.prettify())
