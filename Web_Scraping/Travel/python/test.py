import requests
import sys
from bs4 import BeautifulSoup as soup

response = requests.get('https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAhIJL20vMDJfMjg2EgoyMDIyLTAyLTA3cgwIAxIIL20vMGYydGoaKWoMCAMSCC9tLzBmMnRqEgoyMDIyLTAyLTExcg0IAhIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQE')
html = soup(response.content, 'html.parser')

# string = html.prettify().encode(sys.stdout.encoding, errors='replace')
# string = string.decode(sys.stdout.encoding)
# print(string)

# with open('flights.html', 'w') as out:
#     string = html.prettify().encode(sys.stdout.encoding, errors='replace')
#     string = string.decode(sys.stdout.encoding)
#     print(string)
#     out.write(string)
    
listings = html.find('div', {'jsname': 'AqkRyc'})
print(listings)