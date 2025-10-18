from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

service =Service("/snap/bin/geckodriver")  
driver = webdriver.Firefox(service=service)
driver.get("https://www.youtube.com")
driver.title
'Welcome to Python.org'
driver.quit()
