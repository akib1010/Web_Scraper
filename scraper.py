#import beautifulSoup and urlOpen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
#input the link that needs to be scraped
url_to_scrape= "https://www.trustpilot.com/categories/car_dealer"

req=Request(url_to_scrape, headers={'User-Agent': 'Mozilla/5.0'})

#open the url, read it
page_html=urlopen(req).read()


#parse the html that has been read so that we can go through the file
html_soup=BeautifulSoup(page_html,'html.parser')
#The location of the titles in HTML
dealerList=html_soup.find_all('div',class_="styles_businessUnitCardHeader__22L0A")

#open the file
fileName='CarDealers.txt'

fd=open(fileName,'w')
header='Car Dealers, Trust Score\n'
fd.write(header)
#get the name and score of the dealer and write to the file
for dealer in dealerList:
    title=dealer.find('div',class_='styles_businessTitle__1IANo').text
    score=dealer.find('div',class_='styles_textRating__19_fv').text
    fd.write(title+', '+score+'\n')
#close the file
fd.close()
