import os
import time
import sys
from variables import Variables
from selenium import webdriver
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
        self.screenshot_dir = 'reports/screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def test_search_car_ads(self):
        driver = self.driver
        driver.get(HostName.stage_host)

        # Finding menu and click on first menu item to show car ads list
        driver.find_element(By.CLASS_NAME, Variables.menu).click()
        driver.find_element(By.XPATH, Variables.menu_item).click()

        # Scroll down to find special word
        elem = driver.find_element(By.ID, Variables.special_word)
        driver.execute_script("arguments[0].scrollIntoView();", elem)
        time.sleep(3)
        self.assertEqual(elem.text, 'موارد خاص')

        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")

        # Search on search bar and click on first item to show brand ads list
        driver.find_element(By.CLASS_NAME, Variables.search_icon).click()
        search_bar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, Variables.search_input))
        )
        search_bar.click()
        search_bar.send_keys("پژو ۲۰۶")

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
        if sys.exc_info()[0] is not None:
            # Take a screenshot if the test case fails
            screenshot_name = f'TestResults___main__.CarAdsTest_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved at: {screenshot_path}')

        else:
            # Take a screenshot regardless of the test case result
            screenshot_name = f'TestResults___main__.CarAdsTest_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved at: {screenshot_path}')
        # Close the browser
        self.driver.quit()


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
