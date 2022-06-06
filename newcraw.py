from urllib import response
import requests
import re
from urllib.parse import urljoin, urlparse

# def request(url):
#     try:
#         return requests.get("http://"+url)
#     except requests.exceptions.ConnectionError:
#         pass

targer_url ="flipkart.com"

def extract(url):
    response =requests.get(url)
    return re.findall('(?:href=")(.*?)"',response.content.decode('utf-8'))


hrf_link =extract(targer_url)
# print(hrf_link)
for link in hrf_link:
    link=urljoin(targer_url,link)
    print(link)
