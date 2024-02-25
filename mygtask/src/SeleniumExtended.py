from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import time

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        ).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(5)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            ).click()

    def wait_and_click_visibility(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(5)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def get_actual_error_message(self, locator):
        try:
            element = self.driver.find_element(*locator)
            actual_message = element.text
            return actual_message
        except:
            return "The same Error message not found!"

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            # Check if the expected text is present in the element
            element = self.driver.find_element(*locator)
            actual_text = element.text
            if text not in actual_text:
                raise AssertionError(f"Expected text '{text}' not found in the element")
        except TimeoutException:
            actual_message = self.get_actual_error_message(locator)
            raise AssertionError(
                f"Timeout waiting for element {locator} to contain text '{text}'. Actual message: '{actual_message}'")


