from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.apple.com/retail/internationalplaza/")

relative_hours_path = '//div[@class="time column large-2 large-pull-9 medium-3 medium-pull-7 small-12 small-pull-0"]'
elems = driver.find_elements_by_xpath(relative_hours_path)
for elem in elems:
    print elem.text
driver.close()