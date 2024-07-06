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


class LoginPageUser(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.screenshot_dir = 'reports/screenshots'
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)

    def test_login_to_Bama_user(self):
        driver = self.driver
        driver.get(HostName.stage_host)
        wait = WebDriverWait(driver, 10)
        driver.find_element(By.ID, Variables.profile).click()
        login_to_profile = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, Variables.auth_login))
        )
        login_to_profile.click()
        time.sleep(2)

        iframe = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Variables.iFrame)))
        driver.switch_to.frame(iframe)

        phone_number_element = wait.until(EC.element_to_be_clickable(
            (By.XPATH, Variables.phone_number)
        )
        )

        phone_number_element.click()
        phone_number_element.send_keys("09128164696")

        continue_button = driver.find_element(By.CLASS_NAME, Variables.continue_button)
        continue_button.click()
        enter_otp = driver.find_element(By.ID, Variables.otp_one)
        enter_otp.click()
        enter_otp.send_keys("9")
        driver.find_element(By.ID, Variables.otp_two).send_keys("9")
        driver.find_element(By.ID, Variables.otp_three).send_keys("9")
        driver.find_element(By.ID, Variables.otp_four).send_keys("9")

        continue_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, Variables.continue_button))
        )
        # continue_button = driver.find_element(By.CLASS_NAME, Variables.continue_button)
        continue_button.click()
        time.sleep(5)

        # Print the title of the page
        print(driver.title)
        pass

    def tearDown(self):
        if sys.exc_info()[0] is not None:
            # Take a screenshot if the test case fails
            screenshot_name = f'Exc_Err.LoginUser_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
            screenshot_path = os.path.join(self.screenshot_dir, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            print(f'Screenshot saved at: {screenshot_path}')

        else:
            # Take a screenshot regardless of the test case result
            screenshot_name = f'TestResults.LoginUser_{time.strftime("%Y-%m-%d_%H-%M-%S")}.png'
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
    suite.addTest(LoginPageUser('test_login_to_Bama_user'))

    # Generate the HTML report
    with open(os.path.join(output_dir, 'TestResults.html'), 'w', encoding='utf-8') as report_file:
        runner = unittest.TextTestRunner(
            stream=report_file,
            verbosity=2,
            resultclass=unittest.TextTestResult
        )
        runner.run(suite)
