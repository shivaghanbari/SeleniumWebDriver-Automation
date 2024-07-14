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


class BamaLargeSearch(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.screenshot_dir = 'reports/screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def test_search_by_large_search_bar(self):
        driver = self.driver
        driver.get(HostName.stage_host)

        # Checks if new brand's ads are added to search list or not
        wait = WebDriverWait(driver, 10)
        search_bar = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, Variables.large_search_bar))
        )

        search_bar.click()
        global_search_input = driver.find_element(By.ID, Variables.search_input)
        global_search_input.send_keys("هونگچی")

        hongqi = wait.until(
            EC.element_to_be_clickable((By.XPATH, Variables.search_result))
        )

        hongqi.click()
        time.sleep(5)

        # Print the title of the page
        print(driver.title)
        pass

    def tearDown(self):
        if sys.exc_info()[0] is not None:
            # Take a screenshot if the test case fails
            screenshot_name = f'Exc_Err.LargeSearch_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved at: {screenshot_path}')

        else:
            # Take a screenshot regardless of the test case result
            screenshot_name = f'TestResults.LargeSearch_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
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
    suite.addTest(BamaLargeSearch('test_search_by_large_search_bar'))

    # Generate the HTML report
    with open(os.path.join(output_dir, 'TestResults.html'), 'w', encoding='utf-8') as report_file:
        runner = unittest.TextTestRunner(
            stream=report_file,
            verbosity=2,
            resultclass=unittest.TextTestResult
        )
        runner.run(suite)
