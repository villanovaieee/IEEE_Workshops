from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# must include steps on downloading chrome driver and including the path or pointing to it with service

flights = []
properties = []

googleFlights = "https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAhIJL20vMDJfMjg2EgoyMDIyLTAyLTIycgwIAxIIL20vMGYydGoaKWoMCAMSCC9tLzBmMnRqEgoyMDIyLTAyLTI2cg0IAhIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQE&tfu=EgYIARABGAA"
airBnB = "https://www.airbnb.com/s/New-Orleans--LA/homes?adults=2&place_id=ChIJZYIRslSkIIYRtNMiXuhbBts&checkin=2022-02-22&checkout=2022-02-26"

options = Options()
options.add_argument('--headless')

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

lodgings = driver.find_elements(
    By.XPATH, '//div[@class="_8ssblpx"]')

for lodging in lodgings:
    # properties.append({
    try:
        print(lodging.find_element(
            By.XPATH, 'div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/span').get_attribute('innerText'))
    except:
        print(lodging.find_element(
            By.XPATH, 'div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/span').get_attribute('innerText'))
    print(lodging.find_element(
        By.XPATH, 'div/div/div[2]/div/meta[3]').get_attribute('content'))
    try:
        print(lodging.find_element(
            By.XPATH, 'div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[1]/span').get_attribute('innerText'))
    except:
        print(lodging.find_element(
            By.XPATH, 'div/div/div[2]/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div/div[1]/div/span[2]').get_attribute('innerText'))
    try:
        print(lodging.find_element(
            By.XPATH, 'div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[2]/button/div/span').get_attribute('innerText'))
    except:
        print(lodging.find_element(
            By.XPATH, 'div/div/div[2]/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div/div[1]/div/span[2]').get_attribute('innerText'))
    print(lodging.find_element(
        By.XPATH, 'div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[1]/span/span[2]').get_attribute('innerText'))
    print(lodging.find_element(
        By.XPATH, 'div/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/span/div/div/div/div/picture/source[1]').get_attribute('srcset'))
    # })

print(properties)

# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1] # item
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/span # name
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[1]/span/span[2] # rating
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[1]/span # price per night
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[5]/div[2]/div/div/div[2]/button/div/span # total price
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/meta[3] # link
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/span/div/div/div/div/picture/source[1] # img

# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[1]/div/div[2]/span # name
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[5]/div[1]/span/span[2] # rating
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div/div[1]/div/span[2] # price per night with a price change
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div[5]/div[2]/div/div/div[2]/button/div/span # total price
# //*[@id="site-content"]/div[4]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/meta[3] # link
#

# can break down getting attributes via element properties in inspection window
# span.text or get_attribute('innerHtml') will fail, not sure why
# print(span.get_attribute('innerText'))

driver.close()
