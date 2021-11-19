# all of these are standard libraries save dotenv "python-dotenv" and "requests"
import smtplib
import os
import re
import requests
import asyncio
from time import gmtime, strftime
from dotenv import load_dotenv
from email.message import EmailMessage
from bs4 import BeautifulSoup

load_dotenv(dotenv_path="../.env")
wishlist = 'https://www.amazon.com/hz/wishlist/ls/2J6XL0418J2Y9?ref_=wl_share'

async def main():
    """
    Extract and email pertinent info from an Amazon wishlist
    """
    html = await fetchHtml()
    soup = BeautifulSoup(html, 'html.parser')
    data = []
 
    ul = soup.find(id="g-items")
    for li in ul.find_all("li"):
        title = re.sub(r'\s\s+', '', li.h3.a.string)
        price = li.find("span", {"class": "a-offscreen"}).string
        href = f"https://amazon.com{li.h3.a.get('href')}"

        data.append({"title": title, "price": price, "href": href})
    emailUpdate(data)

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