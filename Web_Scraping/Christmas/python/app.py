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
# and "beautifulsoup4"
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

    # the content of web pages are expected to change. This code will likely not run
    # after a period of time. The path to the title, price, and link will need to be
    # updated
    ul = soup.find(id="g-items")
    for li in ul.find_all("li"):
        title = re.sub(r'\s\s+', '', li.h3.a.string)
        price = li.find("span", {"class": "a-offscreen"}).string
        href = f"https://amazon.com{li.h3.a.get('href')}"

        data.append({"title": title, "price": price, "href": href})

    # format plain and rich text variables for the email
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

    # use regular expressions to replace the double spacing
    # (/s/s+) = new line followed by new line
    # with the <br> tag used in html for line breaks
    htmlText = re.sub(r'\s\s+', '<br>', htmlText)

    # you need to include the path to your .env file containing your usernam and
    # password. In my case (relative to the GitHub) my .env file would be in the
    # "Web Scraping" folder so I use "../../" to specify two levels up from this
    # folder: "Web_Scraping/Travel/python/"
    # "./" means current folder, "../" means parent folder
    username, password = getAccount('../../.env')
    emailUpdate('Wishlist Updates', username, 'your_email@villanova.edu',
                password, text, htmlText)


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
        raise Exception("Bad request:", response.status_code)
    return response.text

# these functions can be found in the "email_python.py" file in the Web_Scraping
# folder with comments on how they work


def getAccount(dotenv_path=''):
    if dotenv_path:
        load_dotenv(dotenv_path=dotenv_path)
    else:
        load_dotenv()
    return (os.getenv('GM_USERNAME'), os.getenv('GM_PASSWORD'))


def emailUpdate(subject, from_email, to_email, password, text, htmlText=''):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    msg.set_content(text)
    if htmlText:
        msg.add_alternative(htmlText, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(from_email, password)
        smtp.send_message(msg)


asyncio.run(main())
