from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# must include steps on downloading chrome driver and including the path or pointing to it with service

flights = []
properties = []

googleFlights = "https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAhIJL20vMDJfMjg2EgoyMDIyLTAyLTIycgwIAxIIL20vMGYydGoaKWoMCAMSCC9tLzBmMnRqEgoyMDIyLTAyLTI2cg0IAhIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQE&tfu=EgYIARABGAA"
airBnB = "https://www.airbnb.com/s/New-Orleans--LA/homes?adults=2&place_id=ChIJZYIRslSkIIYRtNMiXuhbBts&checkin=2022-02-22&checkout=2022-02-26"

# this makes it so that the chrome window does not appear
options = Options()
options.add_argument('--headless')
options.add_argument('--log-level=3')

# executable_path is deprecated, use a service
service = Service(r'C:\Users\davis\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)

driver.get(googleFlights)

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
try:
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'meta[itemprop="name"]'))
    )
except TimeoutException:
    print("Timed out")

lodgings = driver.find_elements(
    By.CSS_SELECTOR, 'div._8ssblpx')

for lodging in lodgings:
    rooms_ameneties = lodging.find_elements(By.CSS_SELECTOR, 'div.i4phm33.dir.dir-ltr')
    rooms = rooms_ameneties[0].get_attribute('innerText')
    ameneties = rooms_ameneties[1].get_attribute('innerText')
    img = lodging.find_element(By.CSS_SELECTOR, 'picture').find_element(By.CSS_SELECTOR, 'source').get_attribute('srcset') # img[:len(img)-3]
    
    properties.append({
        "name": lodging.find_element(By.CSS_SELECTOR, 'meta[itemprop="name"]').get_attribute('content'),
        "href": lodging.find_element(By.CSS_SELECTOR, 'meta[itemprop="url"]').get_attribute('content'),
        "price_per": lodging.find_element(By.CSS_SELECTOR, 'span._tyxjp1').get_attribute('innerText'),
        "price_total": lodging.find_element(By.CSS_SELECTOR, 'div._tt122m').get_attribute('innerText'),
        "rooms": rooms,
        "amentities": ameneties,
        "rating": lodging.find_element(By.CSS_SELECTOR, 'span.r1g2zmv6.dir.dir-ltr').get_attribute('innerText'),
        "img": img[:len(img)-3]
    })



driver.close()
