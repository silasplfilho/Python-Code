import requests
from bs4 import BeautifulSoup
import html.parser

URL = "https://www.reddit.com/r/depression/new/"
# URL = "https://www.geeksforgeeks.org/implementing-web-scraping-python-scrapy/"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

body = soup.find('body')
div = []
div = body.findAll('div', class_='Chtkt3BCZQruf0LtmFg2c')
div[0]
div[1]
# ---
# ignorar esse bloco
div_root = []
div_Root_Class1 = body.findAll(attrs={'class': '_1poyrkZ7g36PawDueRza-J'})
div_Root_Class2 = body.findAll(attrs={'class': '_11R7M_VOgKO1RJyRSRErT3'})

div_root = body.find('div', class_= '_1poyrkZ7g36PawDueRza-J._11R7M_VOgKO1RJyRSRErT3')
div_root = body.find('div', class_=div_Root_Class1+div_Root_Class2)
div_root

# --- 
div_links = []
div_links = body.findAll('a', class_='_3jOxDPIQ0KaOWpzvSQo-1s') # div_links possui os links de cada post numa pagina de um canal do reddit

div_links[0].text

for i in range(len(div_links)):
    print(div_links[i]['href']+ ': ' + div_links[i].text)
