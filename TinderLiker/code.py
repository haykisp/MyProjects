fb_email = ""
fb_pass = ""

a = "Hello Hayk"
import time
from selenium.webdriver.chrome.webdriver import WebDriver

a = "Hello Sona"
driver = WebDriver("chromedriver.exe")
driver.get("https://tinder.com")

time.sleep(5)

login_button = driver.find_element_by_xpath("//button[@aria-label=\"Login with Facebook\"]")

window_tinder = driver.window_handles[0]

login_button.click()

while len(driver.window_handles) == 1:
    time.sleep(2)

window_facebook = driver.window_handles[1]

time.sleep(3)

driver.switch_to.window(window_facebook)

driver.find_element_by_xpath("//input[@name=\"email\"]").send_keys(fb_email)
driver.find_element_by_xpath("//input[@name=\"pass\"]").send_keys(fb_pass)
driver.find_element_by_xpath("//input[@name=\"login\"]").click()

time.sleep(5)

driver.switch_to.window(window_tinder)

time.sleep(3)

driver.find_element_by_xpath("//span[contains(text(), 'Allow')]").click()

time.sleep(3)

driver.find_element_by_xpath("//span[contains(text(), 'Not interested')]").click()

driver.execute_script(open("autolike.js").read())
