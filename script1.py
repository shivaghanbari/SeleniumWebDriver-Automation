import os
import time
from variables import Variables
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Host import HostName
import unittest


class CarAdsTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        pass

    def test_search_car_ads(self):
        driver = self.driver
        driver.get(HostName.stage_host)

        # Finding menu and click on first menu item to show car ads list
        driver.find_element(By.CLASS_NAME, Variables.menu).click()
        driver.find_element(By.XPATH, Variables.menu_item).click()

        # Scroll down to find special word
        elem = driver.find_element(By.ID, Variables.special_word)
        driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.assertEqual(elem.text, 'موارد خاص')

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
        pass

    def tearDown(self):
        # Close the browser
        self.driver.quit()
        pass


if __name__ == '__main__':
    # Specify the output directory for the HTML report
    output_dir = 'reports'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a test suite
    suite = unittest.TestSuite()
    suite.addTest(CarAdsTest('test_search_car_ads'))

    # Generate the HTML report
    with open(os.path.join(output_dir, 'TestResults.html'), 'w', encoding='utf-8') as report_file:
        runner = unittest.TextTestRunner(
            stream=report_file,
            verbosity=2,
            resultclass=unittest.TextTestResult
        )
        runner.run(suite)
