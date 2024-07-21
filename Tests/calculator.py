import os
import time
import sys
from Model.variables import Variables
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Model.Host import HostName
import unittest


class CarCalTest(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.screenshot_dir = '../reports/screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def test_cal_car_price(self):
        driver = self.driver
        driver.get(HostName.stage_host + "calculator")

        wait = WebDriverWait(driver, 10)
        calculator_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, Variables.cal_button))
        )
        calculator_button.click()
        driver.find_element(By.CSS_SELECTOR, Variables.car_brand).click()
        driver.find_element(By.CSS_SELECTOR, Variables.remove_brand).click()
        time.sleep(2)

        # Print the title of the page
        print(driver.title)
        pass

    def tearDown(self):
        if sys.exc_info()[0] is not None:
            # Take a screenshot if the test case fails
            screenshot_name = f'Exc_Err.CarAdsTest_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved at: {screenshot_path}')

        else:
            # Take a screenshot regardless of the test case result
            screenshot_name = f'TestResults.CarAdsTest_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved at: {screenshot_path}')
        # Close the browser
        self.driver.quit()


if __name__ == '__main__':
    # Specify the output directory for the HTML report
    output_dir = '../reports'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a test suite
    suite = unittest.TestSuite()
    suite.addTest(CarCalTest('test_cal_car_price'))

    # Generate the HTML report
    with open(os.path.join(output_dir, 'TestResults.html'), 'w', encoding='utf-8') as report_file:
        runner = unittest.TextTestRunner(
            stream=report_file,
            verbosity=2,
            resultclass=unittest.TextTestResult
        )
        runner.run(suite)
