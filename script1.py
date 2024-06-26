import time
from variables import Variables
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Host import HostName

# Initialize the Chrome driver (make sure you have the ChromeDriver installed and its path set in the system PATH)
driver = webdriver.Chrome()

# Open a website and maximize
driver.maximize_window()
driver.get(HostName.host)
driver.find_element('class name', Variables.menu).click()
driver.find_element('xpath', Variables.menu_item).click()
elem = driver.find_element('id', Variables.special_word)
driver.execute_script("arguments[0].scrollIntoView();", elem)

assert elem.text == 'موارد خاص'

# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
driver.find_element(By.CLASS_NAME, Variables.search_icon).click()
driver.find_element(By.ID, Variables.search_input).click()
driver.find_element(By.ID, Variables.search_input).send_keys("پژو ۲۰۶")

# Wait for the search result to be present and clickable, then click it
search_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, Variables.result_one))
)
search_result.click()

time.sleep(5)
# Print the title of the page
print(driver.title)
# Close the browser
driver.quit()
