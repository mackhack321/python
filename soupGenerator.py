#This module takes a URL as an input and returns a variable 'urlsoup'
#The 'urlsoup' variable holds the URL's soup made with BeautifulSoup

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def makesoup(url):
    client = urlopen(url)
    html = client.read()
    client.close()
    urlsoup = soup(html, "html.parser")
    return urlsoup
