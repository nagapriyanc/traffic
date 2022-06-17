from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

url = input("enter your site url :")
key = input("enter your keyword :")


def run(z, i):
    req = Request(z, headers=headers)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    d = 0

    for link in links:
        if(link is not None) and (url in link):
            d = 1

    if d == 1:
        print("found in", i, "page")
        time.sleep(5)
        exit()

    else:
        print("not found", i,"page")


x = 'https://www.google.com/search?q=' + key + \
    '&rlz=1C1CHBD_enIN1003IN1003&ei=GzasYtHqK9DSz7sP3KSooAE&start='

b = 'https://www.google.com/search?q=' + key

if __name__ == '__main__':
    run(b, 1)

    for i in range(1, 10):
        g = str(i) + '0'
        z = x + g
        i += 1
        run(z, i)
        time.sleep(5)

