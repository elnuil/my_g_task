from mygtask.src.pages.locators.CommitmentPageLocator import CommitmentPageLocator
from mygtask.src.SeleniumExtended import SeleniumExtended

class CommitmentPage(CommitmentPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def check_the_bar_links(self):
        self.sl.wait_and_click_visibility(self.PROTECTING_USERS)
        protecting_users_text = self.sl.wait_and_get_text(self.PROTECTING_USERS_TEXT)
        actual_protecting_text = "Protecting users"
        if protecting_users_text != actual_protecting_text:
           raise AssertionError(f"Texts are not matching. Please check again. Expected Text: {actual_protecting_text} but Actual Text: {protecting_users_text}")

        self.sl.wait_and_click_visibility(self.EXP_OPPORTUNITY)
        exp_opportunity_text = self.sl.wait_and_get_text(self.EXP_OPPORTUNITY_TEXT)
        actual_opportunity_text = "Expanding opportunity"
        if exp_opportunity_text != actual_opportunity_text:
            raise AssertionError(f"Texts are not matching. Please check again. Expected Text: {actual_opportunity_text} but Actual Text:{exp_opportunity_text} ")

        self.sl.wait_and_click_visibility(self.ALL_INVOICES)
        all_invoices_text = self.sl.wait_and_get_text(self.ALL_INVOICES_TEXT)
        actual_all_invoices_text = "Including all voices"
        if all_invoices_text != actual_all_invoices_text:
            raise AssertionError(f"Texts are not matching. Please check again. Expected Text: {actual_all_invoices_text} but Actual Text:{all_invoices_text} ")

        self.sl.wait_and_click_visibility(self.RESPONDING)
        responding_text = self.sl.wait_and_get_text(self.RESPONDING_TEXT)
        actual_responding_text = "Responding to crises"
        if responding_text != actual_responding_text:
            raise AssertionError(f"Text are not matching. Please check again. Expected Text: {responding_text} but Actual Text: {actual_responding_text}")

        self.sl.wait_and_click_visibility(self.SUSTAINABILITY)
        sustainability_text = self.sl.wait_and_get_text(self.SUSTAINABILITY_TEXT)
        actual_sustainability_text = "Advancing sustainability"
        if sustainability_text != actual_sustainability_text:
            raise AssertionError(f"Texts are not matching. Please check again. Expected Text: {sustainability_text} but Actual Text: {actual_sustainability_text}")