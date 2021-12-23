import requests
from bs4 import BeautifulSoup

data=requests.get("https://sfbay.craigslist.org/")

#data is a html response object



soup=BeautifulSoup(data.content,"html.parser")


#print(soup)

print([x for x in soup.descendants])
