import pytest
from mygtask.src.pages.GooglePage import GooglePage
from mygtask.src.pages.CommitmentPage import CommitmentPage

@pytest.mark.usefixtures("init_driver")
class TestGooglePageBarLinks:

# Check the Commitments Page bar links and confirm the titles

    @pytest.mark.gcheck
    @pytest.mark.tcid111
    def test_google_page_bar_links(self):
        print("*******")
        print("TEST STARTED")
        print("*******")

        google_page = GooglePage(self.driver)
        commitment_page = CommitmentPage(self.driver)

        # Go to About Page
        google_page.go_to_about_page()

        # Go to commitment Page
        google_page.go_to_commitment_page()

        # Check the links
        commitment_page.check_the_bar_links()

        print("*******")
        print("TEST FINISHED")
        print("*******")