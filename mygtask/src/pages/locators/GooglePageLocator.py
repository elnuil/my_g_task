from selenium.webdriver.common.by import By

class GooglePageLocator:
    COMMITMENTS = (By.CSS_SELECTOR, '#list-1 > li:nth-child(4)')
    G_IN_UK = (By.XPATH, '//*[@id="list-1"]/li[2]/a')
    SEARCH_BAR = (By.XPATH, '//*[@id="APjFqb"]')
    ERROR_MSG = (By.XPATH, '//*[@id="botstuff"]/div/div[2]/div/p[1]')
    GOOGLE_SEARCH_C = (By.CLASS_NAME, 'gNO89b')
