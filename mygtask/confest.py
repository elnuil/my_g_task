import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = ['chrome', 'safari']
    browser = os.environ.get('BROWSER', None)

    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")

    #export BROWSER=chrome --> Run the code in the terminal

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' is not one of the supported."
                        f"Supported are: {supported_browsers}")

    if browser in ('chrome'):
        driver = webdriver.Chrome()

    elif browser in ('safari'):
        driver = webdriver.Safari()

    request.cls.driver = driver
    driver.maximize_window()
    yield
    driver.quit()
