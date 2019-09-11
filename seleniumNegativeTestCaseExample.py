from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#print statement for console
print("Starting test case")

#locate driver file
driver = webdriver.Chrome(executable_path="C:\dev\webdriverFiles\chromedriver")

#navigate to github 
driver.get("https://github.com/")

#verify properly landed on page by verifying text on landing page
landingPageText = driver.find_element_by_css_selector("body > div.application-main > main > div.py-6.py-sm-8.jumbotron-codelines > div > div > div.col-md-7.text-center.text-md-left > h1")
verificationString = "Built for developers"

if landingPageText.text == verificationString:
    print("Found verification text: " + verificationString)
else:
    print("Error: could not find verification string.")

#click sign in to get to login page
signInBtn = driver.find_element_by_css_selector("body > div.position-relative.js-header-wrapper > header > div > div.HeaderMenu.HeaderMenu--logged-out.position-fixed.top-0.right-0.bottom-0.height-fit.position-lg-relative.d-lg-flex.flex-justify-between.flex-items-center.flex-auto > div.d-lg-flex.flex-items-center.px-3.px-lg-0.text-center.text-lg-left > a.HeaderMenu-link.no-underline.mr-3").click()

#use ID to assign username input to variable 
usernameInput = driver.find_element_by_id("login_field")

#user ID to assign password input to variable
passwordInput = driver.find_element_by_id("password")

#send a text to UN/PW fields
usernameInput.send_keys("Lorem Ipsum")
time.sleep(1) #adding waits to be able to properly input and verify visually when writing scripts
passwordInput.send_keys("Lorem Ipsum")
time.sleep(2) #adding waits to be able to properly input and verify visually when writing scripts

#equivalent to hitting "enter" to hit enter with focus in input (try to log in)
passwordInput.send_keys(Keys.RETURN)


#next step: verify that the credentials are invalid
errorMsg = driver.find_element_by_css_selector("#js-flash-container > div > div")
errorVerification = "Incorrect username or password."

if errorMsg.text == errorVerification:
    print("Found verification text: " + errorVerification)
else:
    print("Error: could not find verification string.")

#explicit wait / make driver sleep for specified amount of time
time.sleep(3)

#close driver / browser. End of this script
print("closing driver, ending script")
driver.close()
