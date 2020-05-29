from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
driver.get("https://formy-project.herokuapp.com/form")
fname = driver.find_element_by_id("first-name")
fname.send_keys("Nicolae")
lname = driver.find_element_by_id("last-name")
lname.send_keys("Scoarta")
job = driver.find_element_by_id("job-title")
job.send_keys("Engineer")

radioButon = driver.find_element_by_id('radio-button-1')
radioButon.click()
checkbox = driver.find_element_by_id('checkbox-2')
checkbox.click()

select = Select(driver.find_element_by_id('select-menu'))
select.select_by_visible_text("5-9")
datepicker = driver.find_element_by_id('datepicker')
datepicker.send_keys('05/30/2020')
datepicker.send_keys((Keys.RETURN))
time.sleep(1)

buton = driver.find_element_by_css_selector("a.btn.btn-lg.btn-primary")
buton.click()
time.sleep(1)
driver.quit()
