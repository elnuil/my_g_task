from mygtask.src.pages.locators.GooglePageLocator import GooglePageLocator
from mygtask.src.SeleniumExtended import SeleniumExtended
import random
import string

class GooglePage(GooglePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_main_page(self):
        main_url = "https://www.google.co.uk/webhp"
        self.driver.get(main_url)


    def create_random_string_text(self):
        random_email_string_length = 25
        random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
        return random_string

    def enter_irrelevant_text(self, text):
        self.sl.wait_and_input_text(self.SEARCH_BAR, text)
        self.sl.wait_and_click(self.GOOGLE_SEARCH_C)

    def check_error_message(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERROR_MSG, exp_err)

    def go_to_about_page(self):
        base_url = "https://about.google/intl/en-GB/"
        self.driver.get(base_url)

    def go_to_commitment_page(self):
        self.sl.wait_and_click(self.COMMITMENTS)


