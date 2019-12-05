import requests, re
from bs4 import BeautifulSoup
print("Enter the IP or Domain you want to scan: ")
ip=input()
url = 'https://viewdns.info/whois/?domain='+str(ip)
user_agent = {'User-agent': 'Mozilla/5.0'}
r = requests.get( url, headers=user_agent )
soup = BeautifulSoup( r.text, 'html.parser' )
tags = soup.find_all('font')[2]
s = re.sub('<br/>', '\n', str(tags))
s=BeautifulSoup( s, 'html.parser' )
print(s.get_text())
