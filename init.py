from selenium import webdriver
from selenium.webdriver.remote.webdriver import (WebDriver, WebElement)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

web_page = webdriver.Chrome()
web_page.get("https://google.com.br")

input_q: WebElement = web_page.find_element_by_css_selector("input.gLFyf")
input_q.send_keys("tempo agora")
input_q.send_keys(Keys.ENTER)

city: WebElement = web_page.find_element_by_id("wob_loc")
temperature: WebElement = web_page.find_element_by_id("wob_tm")

print(city.text)
print(temperature.text + "°C")