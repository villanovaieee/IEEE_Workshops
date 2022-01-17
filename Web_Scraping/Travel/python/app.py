"""
Copyright 2021 The Villanova Chapter of the Institute of Electrical and
Electronics Engineers (IEEE)
This file is part of the IEEE_Workshops library.

The IEEE_Workshops libary is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

The IEEE_Workshops libary is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along with
the IEEE_Workshops library. If not, see <https://www.gnu.org/licenses/>.
"""

# all of these are standard libraries save dotenv "python-dotenv" and "requests"
import smtplib
import os
import re
import json
import requests
import asyncio
from time import gmtime, strftime
from urllib.parse import urlencode
# from dotenv import load_dotenv
from email.message import EmailMessage
from bs4 import BeautifulSoup

# load_dotenv(dotenv_path="../.env")
housingsites = [
    "https://www.airbnb.com/",
    "https://www.vrbo.com/"
]

airsites = [
    "https://www.google.com/_/TravelFrontendUi/data/batchexecute",
    "https://www.travelocity.com/Flights-Search",
    "https://www.southwest.com/",
    "https://www.tripadvisor.com/",
    "https://www.united.com/en/us",
    "https://www.kayak.com/"
]

async def main():
    """
    Extract and email pertinent info from an Amazon wishlist
    """
    # html = await fetchGoog("Philadelphia", "New Orleans", "2022-01-24", "2022-02-24") #fetchTravelocity()
    response = requests.get('https://www.google.com/travel/flights/search?tfs=CBwQAhooagwIAhIIL20vMGRjbGcSCjIwMjItMDEtMzFyDAgDEggvbS8wZjJ0ahooagwIAxIIL20vMGYydGoSCjIwMjItMDItMjRyDAgCEggvbS8wZGNsZ3ABggELCP___________wFAAUgBmAEB&tfu=EgYIAhABGAA')
    start = response.content.decode('utf-8').find('role="list">')
    soup = BeautifulSoup(response.content, 'html.parser')
    listings = soup.find_all('div', {'role': 'list'})
    print(soup.prettify()[start:start+100000])
    print(start)
    # print(html)

    # soup = BeautifulSoup(html, 'html.parser')
    # data = []

    # listings = soup.find_all('div', {'role': 'list'})
    # print(soup.prettify())

    # listings = soup.find_all('ul')
    # print(len(listings))
    # print(soup.prettify())
    # for li in listings.find_all("li"):
    #     price_section = li.find("section")
    #     price = price_section.span[0].text
    #     print(price)
 
    # ul = soup.find(id="g-items")
    # for li in ul.find_all("li"):
    #     title = re.sub(r'\s\s+', '', li.h3.a.string)
    #     price = li.find("span", {"class": "a-offscreen"}).string
    #     href = f"https://amazon.com{li.h3.a.get('href')}"

    #     data.append({"title": title, "price": price, "href": href})
    # emailUpdate(data)
#AQrAAwqqA3Y1LXNvcy03MjViYzViZWMyODlmMDEwMTVmODFjMjI4ZGFiZWFiYi0wLTItc3QtdjUtc29zLTE5ZTIzNjQ0MTY4MzdhY2QwZDgxNjBhMTQ0MmEyZTZlLTUtMX4yLlN-QVFvRUNJSHhCQklIQ05RRUVBY1lHeWdDV0FKd0FIQUF-QVFwRENoOEl4bklTQkRFeE5qVVk3MWtnekhBb2xQS0NBakMzODRJQ09GcEFBRmdCQ2lBSXhuSVNCREV4TXprWXpIQWd6TVFCS0xUMWdnSXdxZmFDQWpoYVFBRllBUklLQ0FJUUFSZ0NLZ0pHT1JnQklnUUlBUkFCS0FJb0F5Z0VNQUUuQVFwZENpMEl4SmdCRWdReU9UVTBHTXpFQVNEanRBRW9sSUtEQWpDb2c0TUNPRVZBQUZnQmFnbENRVk5KUTBWRFQwNEtMQWpFbUFFU0JERXpNREVZNDdRQklPOVpLTS1EZ3dJd3RvU0RBamhGUUFGWUFXb0pRa0ZUU1VORlEwOU9FZ29JQVJBQkdBRXFBa1JNR0FFaUJBZ0JFQUVvQWlnREtBUXdBURGamZmZmdFjQCIBASoFEgMKATESPwoWCgoyMDIyLTAxLTI0EgNQSEwaA01TWQoWCgoyMDIyLTAxLTI1EgNNU1kaA1BITBIHEgVDT0FDSBoCEAEgAg\=\= > div > div > div > div > div.uitk-flex.uitk-flex-justify-content-space-between.uitk-flex-gap-six.uitk-flex-nowrap.uitk-layout-grid-item > div.uitk-flex-item.uitk-flex-shrink-1 > div > div.uitk-price-lockup.right-align > section > span.uitk-lockup-price
async def fetchHtml():
    """
    Fetch a url and return its html body if there are no errors.
    Returns
    -------
    response.text : str
        Html body of the fetched page
    """
    response = requests.get(wishlist)
    if response.status_code != 200:
        raise Exception("Bad request")
    return response.text

async def fetchGoog(fLocation: str, tLocation: str, fDate: str, rDate: str):
    q = {
        "rpcids": "H028ib",
        "f.sid": "3524935585383552279",
        "bl": "boq_travel-frontend-ui_20220110.08_p0",
        "hl": "en",
        "soc-app": "162",
        "soc-platform": "1",
        "soc-device": "1",
        "_reqid": "1552277",
        "rt": "c"
    }

    # must use a "raw" string so that the back slashes are included in the encoding and not escaped
    fDataStr = r'[[["H028ib","[\"{location}\",[1,2,3,5,4],null,[1,1],1]",null,"generic"]]]'

    fData = {
        "f.req": fDataStr.format(location=fLocation),
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    }

    # [[["tDoGIe","[null,[[\"/m/0f2tj\",5]]]",null,"generic"]]]
    response = requests.post(url=airsites[0],
                            # params=urlencode(q), # not necessary in this case but can be necessary
                            data=urlencode(fData),
                            headers=headers)

    if response.status_code != 200:
        raise Exception("Bad Google Flights from request")
    fTemp = json.loads(response.text[6:])
    fCities = json.loads(fTemp[0][2])
    fCode = fCities[0][0][0][4]

    print(fCode)

    fData['f.req'] = fDataStr.format(location=tLocation)
    response = requests.post(url=airsites[0],
                            # params=urlencode(q), # not necessary in this case but can be necessary
                            data=urlencode(fData),
                            headers=headers)

    if response.status_code != 200:
        raise Exception("Bad Google Flights destination request")
    tTempt = json.loads(response.text[6:])
    tCities = json.loads(tTempt[0][2])
    tCode = tCities[0][0][0][4]

    print(tCode)

    url = 'https://www.google.com/_/TravelFrontendUi/data/travel.frontend.flights.FlightsFrontendService/GetShoppingResults'
    # fData = [[["WR9Xq",fr"[\"{fCode}\",[\"{tCode}\"],\"2022-01-31\",2]",null,"generic"]]]

    fData['f.req'] = fr'[null,"[[null,null],[null,null,1,null,[],1,[1,0,0,0],null,null,null,null,null,null,[[[[[\"{fCode}\",4]]],[[[\"{tCode}\",5]]],null,0,[],[],\"{fDate}\",null,[],[],[],null,null,[]],[[[[\"{tCode}\",5]]],[[[\"{fCode}\",4]]],null,0,[],[],\"{rDate}\",null,[],[],[],null,null,[]]],null,null,null,true,null,null,null,null,null,[],null,null,null,null],1,false,false]"]'
    response = requests.post(url=url,
                            data=urlencode(fData),
                            headers=headers)

    if response.status_code != 200:
        raise Exception("Bad Google Flights request")

    test = json.loads(response.text[6:])
    test1 = json.loads(test[0][2])
    flights = test1[2:]

    # for airline in flights:


    print(len(flights[0]))

    # with open('flights.json', 'w') as out:
    #     s = json.dumps(flights, indent=4)
    #     out.write(s)

    # print(json.dumps(flights[0], indent=4))

    # return response.content

async def fetchTravelocity():
    #departure:str, destination:str
    q = {
        "flight-type": "on",
        "mode": "search",
        "trip": "roundtrip",
        "leg1": "from:Philadelphia,+PA,+United+States+of+America+(PHL-All+Airports),to:New+Orleans,+Louisiana,+United+States+of+America,departure:1/24/2022TANYT",
        "options": "cabinclass:economy",
        "leg2": "from:New Orleans, Louisiana, United States of America,to:Philadelphia, PA, United States of America (PHL-All Airports),departure:1/25/2022TANYT",
        "passengers": "children:0,adults:1,seniors:0,infantinlap:Y",
        "fromDate": "1/24/2022",
        "toDate": "1/24/2022",
        "d1": "2022-01-24",
        "d2": "2022-01-25"
    }
    # requests.post
    response = requests.get(airsites[0], params=q)
    if response.status_code != 200:
        raise Exception("Bad request")
    return response.text

def emailUpdate(data):
    """
    Email data collected in the main function
    Parameters
    ----------
    data : dict[]
        List of dictionaries with title, link, and price of wishlist items
    """
    msg = EmailMessage()
    msg['Subject'] = f'Wishlist Updates {strftime("%a %b %d %Y", gmtime())}'
    msg['From'] = os.getenv('GM_USERNAME')
    msg['To'] = os.getenv('GM_RECIPIENT')
    text = ''
    htmlText = ''
    for item in data:
        text += '''
        {0}
        {1}
        {2}
        '''.format(item['title'], item['href'], item['price'])

        htmlText += '''
        <a href="{0}">{1}</a>
        {2}
        '''.format(item['href'], item['title'], item['price'])

    msg.set_content(text)
    msg.add_alternative(re.sub(r'\s\s+', '<br>', htmlText), subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv('GM_USERNAME'), os.getenv('GM_PASSWORD'))
        smtp.send_message(msg)

asyncio.run(main())