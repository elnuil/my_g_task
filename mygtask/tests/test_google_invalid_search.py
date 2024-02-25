import pytest
from mygtask.src.pages.GooglePage import GooglePage
from mygtask.src.pages.CommitmentPage import CommitmentPage


@pytest.mark.usefixtures("init_driver")
class TestGoogleInvalidSearch:

# Check the invalid search message for EN

    @pytest.mark.gcheck
    @pytest.mark.tcid112
    def test_google_invalid_search(self):
        print("*******")
        print("TEST STARTED")
        print("*******")

        google_page = GooglePage(self.driver)
        commitment_page = CommitmentPage(self.driver)

        google_page.go_to_main_page()
        random_text = google_page.create_random_string_text()
        google_page.enter_irrelevant_text(random_text)
        expected_msg = f"Your search - {random_text} - did not match any documents."
        google_page.check_error_message(expected_msg)

        print(expected_msg)
        print("*******")
        print("TEST FINISHED")
        print("*******")