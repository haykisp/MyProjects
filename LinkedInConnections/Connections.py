from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

login = ""
password = ""

field_email = "//input[@name=\"session_key\"]"
field_password = "//input[@name=\"session_password\"]"
button_login = "//button[@type=\"submit\"]"
text_connections = "//header[@class=\"mn-connections__header\"]/h1"
connections = "//div[@class=\"mn-connection-card ember-view\"]/a[@data-control-name=\"connection_profile\"]"
button_seeMore = "//a[@data-control-name=\"contact_see_more\"]"
connection_Name = "//h1[@class=\"pv-top-card-section__name inline t-24 t-black t-normal\"]"
connection_Email = "//section[@class=\"pv-contact-info__contact-type ci-email\"]/div/a"
connection_Location = "//h3[@class=\"pv-top-card-section__location t-16 t-black--light t-normal mt1 inline-block\"]"
connetction_CurrJob = "//h2[@class=\"pv-top-card-section__headline mt1 t-18 t-black t-normal\"]"
connection_PrevJobs = "//span[@class=\"pv-entity__secondary-title\"]"

driver = WebDriver("chromedriver.exe")
driver.maximize_window()
driver.get("https://www.linkedin.com/login")
driver.find_element_by_xpath(field_email).send_keys(login)
driver.find_element_by_xpath(field_password).send_keys(password)
driver.find_element_by_xpath(button_login).click()
driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
count = driver.find_element_by_xpath(text_connections).text
count = int(count.split()[0])

connections_list = []
i = 0
while i != len(driver.find_elements_by_xpath(connections)):
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN)
    connections_list.append(driver.find_elements_by_xpath(connections)[i].get_attribute("href"))
    i += 1

f = open('Connections.csv', 'w', encoding="utf-8")
f.write("Name, Email, Location, Current_job, Previous_companies \n")
for connection in connections_list:

    Email = ""
    Previous_companies = ""

    driver.get(connection)

    Name = driver.find_element_by_xpath(connection_Name).text.replace(",", " ")
    Location = driver.find_element_by_xpath(connection_Location).text.replace(",", " ")
    Current_job = driver.find_element_by_xpath(connetction_CurrJob).text.replace(",", " ")
    for company in driver.find_elements_by_xpath(connection_PrevJobs):
        Previous_companies += company.text.replace(",", "") + "; "

    driver.find_element_by_xpath(button_seeMore)
    driver.get(connection + "detail/contact-info/")
    try:
        Email = driver.find_element_by_xpath(connection_Email).get_attribute("href")
    except NoSuchElementException:
        pass
    f.write(Name + ',' + Email + ',' + Location + ',' + Current_job + "," + Previous_companies + '\n')

f.close()
driver.close()
driver.quit()
