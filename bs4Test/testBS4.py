import urllib.request
from bs4 import BeautifulSoup

URL = "https://www.reddit.com/r/depression/new/"
# URL = "https://www.geeksforgeeks.org/implementing-web-scraping-python-scrapy/"

source = urllib.request.urlopen(URL).read()
soup = BeautifulSoup(source, 'lxml')
# ---
div_class_mainFrame = "rpBJOHq2PR60pnwJlUyP0"



strsd = "_1oQyIsiPHYt6nx7VOmd1sz" + " " + "_1RYN-7H8gYctjOQeL8p2Q7"
class_ids = ["_1oQyIsiPHYt6nx7VOmd1sz",
             "_1RYN-7H8gYctjOQeL8p2Q7",
             "scrollerItem",
             "_3Qkp11fjcAw9I9wtLo8frE",
             "_1qftyZQ2bhqP62lbPjoGAh",
             "Post t3_dndr2h"]

div = soup.findAll('div', class_=class_ids[0])
div[1]['id']

div = []
for classId in class_ids:
    if len(div) == 0:
        tempDiv = soup.findAll('div', class_=class_ids[0])
        div.append(temp.div)
    else:
        continue

tempDiv[1].decompose()


id_ = 
class_id = """"""

div = soup.findAll('div', class_=class_id)

div[0]
div[1].findAll('p')
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
