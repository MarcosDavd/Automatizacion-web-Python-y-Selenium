from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

service =Service("/snap/bin/geckodriver")  
driver = webdriver.Firefox(service=service)
driver.implicitly_wait(20)
driver.get("https://bandcamp.com/discover/")

pagination_button = driver.find_element(By.ID,"view-more")
print(pagination_button.accessible_name)
pagination_button.click()
driver.quit()
