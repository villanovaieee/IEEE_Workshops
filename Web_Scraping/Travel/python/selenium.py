import requests
from selenium import webdriver

def main():
    flights = "https://www.google.com/_/TravelFrontendUi/data/batchexecute"
    driver = webdriver.Chrome()

    driver.request()

main()