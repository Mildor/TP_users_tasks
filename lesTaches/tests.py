import time

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(service=ChromeService("C:/chromedriver/chromedriver.exe"))
browser.get('http://127.0.0.1:8000/')
time.sleep(5)
htmlSource = browser.page_source

#assert 'Que souhaitez vous faire ?' in browser.title

elem = browser.find_element("id", "lien_to_users")

if elem is not None:
    elem.click()
    print(elem)

