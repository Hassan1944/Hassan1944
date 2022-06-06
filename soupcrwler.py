from urllib import response
from urllib.parse import urljoin
from bs4 import BeautifulSoup

import requests
url =input("Enter the url : ")
response =requests.get("http://"+url)
data =response.text
soup =BeautifulSoup(data)
for link in soup.find_all('a'):
    # print(link.get("href"))
    test =link.get("href")
    link =urljoin(url,test)
    print(link)