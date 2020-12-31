#http://py4e-data.dr-chuck.net/known_by_Fikret.html
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
times = int(input('Repeat: '))
position = int(input('Position: '))
for i in range(times):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    number = 0
    for tag in tags:
        link = tag.get('href', None)
        print(link)
        number = number+1
        if number==position:
            url = link
            break
print(re.findall('known_by_(\S+).html', url)[0])
