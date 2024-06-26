import time
from variables import Variables
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Host import HostName

# Initialize the Chrome driver
driver = webdriver.Chrome()

#  Maximize and open a website
driver.maximize_window()
driver.get(HostName.host)

# Finding menu and click on first menu item to show car ads list
driver.find_element('class name', Variables.menu).click()
driver.find_element('xpath', Variables.menu_item).click()

# Scroll down to find special word
elem = driver.find_element('id', Variables.special_word)
driver.execute_script("arguments[0].scrollIntoView();", elem)
assert elem.text == 'موارد خاص'

# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")

# Search on search bar and click on first item to show brand ads list
driver.find_element(By.CLASS_NAME, Variables.search_icon).click()
driver.find_element(By.ID, Variables.search_input).click()
driver.find_element(By.ID, Variables.search_input).send_keys("پژو ۲۰۶")

# Wait for the search result to be present and clickable, then click it
search_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, Variables.result_one))
)
search_result.click()

time.sleep(2)
# Print the title of the page
print(driver.title)
# Close the browser
driver.quit()
