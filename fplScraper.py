#import beautifulSoup
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

#input the link that will provide the website to scrape
url_to_scrape="https://fantasy.premierleague.com/statistics"
#Set the headers
req=Request(url_to_scrape,headers={'User-Agent': 'Mozilla/5.0'})

#open the url and read it
page_html=urlopen(req).read()

#parse the html that has been read
html_soup=BeautifulSoup(page_html,'html.parser')

playerList=html_soup.findall('tr',class_="ElementTable__ElementRow-sc-1v08od9-3")

fileName='FPL_List.txt'

fd=open(fileName,'w')
header='FPL Season:21/22\n'
fd.write(header)

for player in playerList:
    name=player.find('div',class_='ElementInTable__Name-y9xi40-1 dwvEEF').text
    fd.write(name+'\n')

fd.close()
