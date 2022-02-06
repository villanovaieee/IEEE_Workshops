from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# must include steps on downloading chrome driver and including the path or pointing to it with service

flights = "https://www.google.com/travel/flights/search?tfs=CBwQAhopag0IAhIJL20vMDJfMjg2EgoyMDIyLTAyLTA3cgwIAxIIL20vMGYydGoaKWoMCAMSCC9tLzBmMnRqEgoyMDIyLTAyLTExcg0IAhIJL20vMDJfMjg2cAGCAQsI____________AUABSAGYAQE"

# options = Options()
# options.add_argument('--headless')

# executable_path is deprecated, use a service
service = Service(r'C:\Users\davis\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get(flights)

# span = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[9]/div[2]/span')

timeout = 5
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@role="listitem"]'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out")

span = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[9]/div[2]/span')
listings = driver.find_elements(By.XPATH, '//div[@role="listitem"]')

//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div[1]
//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[9]/div[2]/span # price
//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[4] # departure
//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div/c-wiz/c-wiz/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[6] # arrival



# can break down getting attributes via element properties in inspection window
print(span.get_attribute('innerText')) # span.text or get_attribute('innerHtml') will fail, not sure why

driver.close()
