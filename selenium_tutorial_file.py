from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\dev\webdriverFiles\chromedriver")
driver.get("http://www.python.org")

element = driver.find_element_by_name("q")
element.clear
element.send_keys("pycon")
element.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()
