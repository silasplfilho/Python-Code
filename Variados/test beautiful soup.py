import bs4 as bs
import urllib.request

# VIDEO 1
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup)
print(sauce)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.text)

print(soup.p)
print(soup.find_all('p'))

print('######### STARTS HERE ##########')
for paragraph in soup.find_all('p'):
    print(paragraph.string)

print('######### STARTS HERE ##########')
for paragraph in soup.find_all('p'):
    print(paragraph.text)

print('######### STARTS HERE ##########')
print(soup.get_text())

print('######### STARTS HERE ##########')
for url in soup.find_all('a'):
    print(url)


# VIDEO 2
sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print('######### STARTS HERE ##########')
nav = soup.nav
for url in soup.find_all('a'):
    print(url.get('href'))

print('######### STARTS HERE ##########')
body = soup.body
for paragraph in body.find_all('p') :
    print(paragraph.text)

print('######### STARTS HERE ##########')
for div in soup.find_all('div', class_='body'):
    print(div.text)

# VIDEO 3
import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

table = soup.table
table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)
