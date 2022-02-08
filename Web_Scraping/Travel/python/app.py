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
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import re
# these imports come from the "email_python.py" file in the Web_Scraping folder
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import time

# must include steps on downloading chrome driver and including the path or pointing to it with service

flights = []
properties = []

googleFlights = "https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAhIJL20vMDJfMjg2EgoyMDIyLTAyLTIycgwIAxIIL20vMGYydGoaKWoMCAMSCC9tLzBmMnRqEgoyMDIyLTAyLTI2cg0IAhIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQE&tfu=EgYIARABGAA"
airBnB = "https://www.airbnb.com/s/New-Orleans--LA/homes?adults=2&place_id=ChIJZYIRslSkIIYRtNMiXuhbBts&checkin=2022-02-22&checkout=2022-02-26"

# this makes it so that the chrome window does not appear
options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')

# you must specify the path to the chromedriver on your system. View the README
# for instructions on installing the chromedriver
service = Service(r'C:\Users\davis\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

driver.get(googleFlights)

# the xpath and CSS selectors used in this code are specific to the urls used
# you will need to do the work finding the xpath or selectors for your own

timeout = 5
try:
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.XPATH, '//*[@role="listitem"]'))
    )
except TimeoutException:
    print("Timed out")

best_flights = driver.find_element(By.XPATH, '//div[@role="list"]')
listings = best_flights.find_elements(
    By.XPATH, 'div')

for flight in listings:
    flights.append({
        "airline": flight.find_element(
            By.XPATH, 'div/div[1]/div[2]/div[2]/div[2]/div[2]/span').get_attribute('innerText'),
        "departure": flight.find_element(
            By.XPATH, 'div/div[1]/div[2]/div[4]').get_attribute('innerText'),
        "duration": flight.find_element(
            By.XPATH, 'div/div[1]/div[2]/div[2]/div[3]/div').get_attribute('innerText'),
        "stops": flight.find_element(
            By.XPATH, 'div/div[1]/div[2]/div[2]/div[4]/div[1]/span').get_attribute('innerText'),
        "price": flight.find_element(
            By.XPATH, 'div/div[1]/div[2]/div[2]/div[6]/div[1]/div[2]/span').get_attribute('innerText')
    })

driver.get(airBnB)
# the "try except" method used previously is the proper way to await elements on
# a page, but alternatively you can just use a delay since we're only accessing
# two web pages
time.sleep(5)

lodgings = driver.find_elements(
    By.CSS_SELECTOR, 'div._8ssblpx')

for lodging in lodgings:
    rooms_ameneties = lodging.find_elements(
        By.CSS_SELECTOR, 'div.i4phm33.dir.dir-ltr')
    rooms = rooms_ameneties[0].get_attribute('innerText')
    ameneties = rooms_ameneties[1].get_attribute('innerText')
    img = lodging.find_element(By.CSS_SELECTOR, 'picture').find_element(
        By.CSS_SELECTOR, 'source').get_attribute('srcset')  # img[:len(img)-3]

    properties.append({
        "name": lodging.find_element(By.CSS_SELECTOR, 'meta[itemprop="name"]').get_attribute('content'),
        "href": lodging.find_element(By.CSS_SELECTOR, 'meta[itemprop="url"]').get_attribute('content'),
        "price_per": lodging.find_element(By.CSS_SELECTOR, 'span._tyxjp1').get_attribute('innerText'),
        "price_total": lodging.find_element(By.CSS_SELECTOR, 'div._tt122m').get_attribute('innerText'),
        "rooms": rooms,
        "amenities": ameneties,
        "img": img[:len(img)-3]
    })

# You can find these functions (getAccount and emailUpdate) in the
# email_python.py file in the Web_Scraping folder with comments on how they
# work


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


# We will build the plain text and rich text (htmlText) to be included in our
# automatic email
# Wrapping a string in three quotations in python allows you to actual "enter"
# between new lines, and prefixing with "f" makes it a formatted string and
# allows you to use curly braces to include variables in-line
text = 'These are the latest best flights for your trip:\n'

for flight in flights:
    text += f'''
Airline: {flight['airline']}
Departure: {flight['departure']}, Duration: {flight['duration']}, Stops: {flight['stops']}
Price: {flight['price']}
'''

text += '\nThese are the available rooms\n'
htmlText = text

# if you would prefer to sort the properties by increasing price and email,
# let's say the top 5, use this for loop:
# for property in sorted(properties, key=lambda x: x['price_total'])[:5]

for property in properties:
    text += f'''
{property['name']}
{property['rooms']}
{property['amenities']}
Price/night: {property['price_per']}, Total: {property['price_total']}
'''
    htmlText += f'''
<b>{property['name']}</b>
{property['rooms']}
{property['amenities']}
Price/night: {property['price_per']}, Total: {property['price_total']}
<img src={property['img']} />
'''

# use regular expressions to replace new lines
# with the <br> tag used in html for line breaks
# (/n) = match every new line character
htmlText = re.sub(r'\n', '<br>', htmlText)

# you need to include the path to your .env file containing your usernam and
# password. In my case (relative to the GitHub) my .env file would be in the
# "Web Scraping" folder so I use "../../" to specify two levels up from this
# folder: "Web_Scraping/Travel/python/"
# "./" means current folder, "../" means parent folder. This must be in
# reference to the folder your terminal is running from
username, password = getAccount(dotenv_path='../../.env')
emailUpdate('Travel Updates', username, 'your_email@villanova.edu',
            password, text, htmlText)

driver.close()
