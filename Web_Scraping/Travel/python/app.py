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
import requests
import asyncio
from time import gmtime, strftime
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
    html = await fetchGoog() #fetchTravelocity()
    # print(html)

    # soup = BeautifulSoup(html, 'html.parser')
    # data = []

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

async def fetchGoog():
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

    fData = {
        "f.req": '[[["H028ib","[\"New Orlean\",[1,2,3,5,4],null,[1,1],1]",null,"generic"]]]',
        'at': 'ABrGKkR9jw_HA1rHlyy2lgzwGXA8:1642224490509',
    }

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
        # "cookie": "CONSENT=YES+US.en+201909; ANID=AHWqTUkH25er2oRz7Qcv9QhEm7B170WryLgqXSYz9L9GucunPMeM9Z-Lecjp2vik; OGPC=19023976-1:19022591-1:19026101-2:; SID=FQjvKLM7qABJr8WfJfkKOVkeQ2RviQdXhhqbmEJtaSZhYMNHqfFBfXeEe-XXKL7NTZPIKw.; __Secure-1PSID=FQjvKLM7qABJr8WfJfkKOVkeQ2RviQdXhhqbmEJtaSZhYMNHNNjQIAgJSWc_fOelUISUHQ.; __Secure-3PSID=FQjvKLM7qABJr8WfJfkKOVkeQ2RviQdXhhqbmEJtaSZhYMNHhuJCcOylpcOoAcBp6U3HXA.; HSID=AM3NaqYaPI7bflRHy; SSID=AR3DOh58hzP_RDJDl; APISID=RyI_-tEolq_miDkK/Axw9rZjnmH-CqfbZb; SAPISID=Zyn6B3aZyvcA7qS8/Are23evT-vAdD3ppA; __Secure-1PAPISID=Zyn6B3aZyvcA7qS8/Are23evT-vAdD3ppA; __Secure-3PAPISID=Zyn6B3aZyvcA7qS8/Are23evT-vAdD3ppA; OTZ=6317485_76_76_104100_72_446760; 1P_JAR=2022-01-11-14; SIDCC=AJi4QfH2f1jP6ZxAgu57N223q8LUYaIJZwH1YdKEni1zwjmtEqYhb3LhzImf86EOON8Qp4Chaw; __Secure-3PSIDCC=AJi4QfEcJOJO2EJb3WqmMy5ZeQGzKAPhF1o7m7ARFlIeo2hLXFpTgB6m5z2SNGZJhuCgQwUN4LfR; NID=511=nIh92D1iormki3qxLQ7_5vRn5p9MoV3vPOXW_hiL3z9Ml3OunD84fRafIDNXoLzmqcfhXCuEY8q_oBlsZhuXUHkFOsZy35T2Y47FUpGBsoGaNacfIL_9U0eiZs5PJQ74BnlI2aT2QjfKqqaw7vbUkNL8LMhXjmRT-Le8qzJM1tWYS33w8PWdZXVa8hszFp3Ou7YO8l2XN18n6NuUbuiZtk87wjgePEUBo3zJCan8Lse1JchM0l7Ws2okbZdRKg",
        # "origin": "https://www.google.com",
        # "referer": "https://www.google.com/",
        # "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
        # "sec-ch-ua-mobile": "?0",
        # "sec-ch-ua-platform": '"Windows"',
        # "sec-fetch-dest": "empty",
        # "sec-fetch-mode": "cors",
        # "sec-fetch-site": "same-origin",
        # "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        # "x-goog-ext-190139975-jspb": '["US","ZZ","mWgjRA=="]',
        # "x-goog-ext-259736195-jspb": '["en-US","US","USD",2,null,[300],null,[[47805254,47805218,45848307,47878017,47872143,47805230,47805250,47805226,47837317,47879090,45847647,4645803,47805238,47805234,45847663,47839141,45847655,47805242,47805258,47805222,47805246]],7,[]]',
        # "x-same-domain": "1"
    }

    # fData = (
    #     ('f.req', (None, '[[["H028ib","[\"New Orlean\",[1,2,3,5,4],null,[1,1],1]",null,"generic"]]]'))
    # )

    response = requests.post(airsites[0], data=q, json=fData)
    print(response.content)
    if response.status_code != 200:
        raise Exception("bad request")
    
    return response.content

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