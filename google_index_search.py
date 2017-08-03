from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import time

def search():
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    start = 0
    searchword = input('Enter the word(s) to search for: ')
    if ' ' in searchword: searchword = searchword.split()
    searchaddress = input('Enter the address to search for: ')
    url = 'http://www.google.com/search?q='+'+'.join(searchword)
    position = 0
    while True:
        print('Retrieving',url)
        print('Checking from article',start+1)
        try:
            req = Request(url, headers=headers)
            html = urlopen(req).read().decode()
        except Exception as e:
            print(str(e))
            return
        soup = BeautifulSoup(html, "html.parser")
        tags = soup('cite')
        for tag in tags:
            position += 1
            if searchaddress in str(tag):
                print('Address found:')
                print(str(tag.string))
                print('in position',position,'of Google.com index')
                return
        start += 10
        url = 'http://www.google.com/search?q='+'+'.join(searchword) +'&start='+ str(start)
        time.sleep(2)

if __name__ == '__main__':
    search()
