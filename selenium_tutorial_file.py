from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#locate driver file
driver = webdriver.Chrome(executable_path="C:\dev\webdriverFiles\chromedriver")

#navigate to google 
driver.get("https://www.google.com/")

#use css selector to assign google's input text field to searchInput varbiable
searchInput = driver.find_element_by_css_selector("#tsf div:nth-child(2) div div.RNNXgb div div.a4bIc input")

#send a string to the search bar
searchInput.send_keys("This search is automated with python & selenium")
#equivalent to hitting "enter" to start the search
searchInput.send_keys(Keys.RETURN)

#explicit wait / make driver sleep for specified amount of time
time.sleep(3)

#close driver / browser. End of this script
driver.close()
