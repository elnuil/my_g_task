from selenium.webdriver.common.by import By

class CommitmentPageLocator:
    # Bar Link Locators
    PROTECTING_USERS = (By.XPATH, '//*[@id="page-content"]/section[3]/nav/ul/li[1]/a/span')
    EXP_OPPORTUNITY = (By.XPATH, '//*[@id="page-content"]/section[3]/nav/ul/li[2]/a/span')
    ALL_INVOICES = (By.XPATH, '//*[@id="page-content"]/section[3]/nav/ul/li[3]/a/span')
    RESPONDING = (By.XPATH, '//*[@id="page-content"]/section[3]/nav/ul/li[4]/a/span')
    SUSTAINABILITY = (By.XPATH, '//*[@id="page-content"]/section[3]/nav/ul/li[5]/a/span')

    # Link Text Locators
    PROTECTING_USERS_TEXT = (By.XPATH, '//*[@id="protecting_users"]/div[1]/div[2]/h2')
    EXP_OPPORTUNITY_TEXT = (By.XPATH, '//*[@id="expanding_opportunity"]/div[1]/div[2]/h2')
    ALL_INVOICES_TEXT = (By.XPATH, '//*[@id="including_all_voices"]/div[1]/div[2]/h2')
    RESPONDING_TEXT = (By.XPATH, '//*[@id="responding_to_crises"]/div[1]/div[2]/h2')
    SUSTAINABILITY_TEXT = (By.XPATH, '//*[@id="advancing_sustainability"]/div[1]/div[2]/h2')

    LOCATIONS_ARRAY = (By.CLASS_NAME, 'modules-lib__doorway-tile__paragraph glue-mod-spacer-2-top glue-body')