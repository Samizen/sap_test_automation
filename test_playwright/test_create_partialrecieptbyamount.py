from playwright.sync_api import sync_playwright
import time
from test_playwright.config import User_details
from test_playwright.test_login import login_ariba

# Parameters for test case
USERNAME = "spandey_prem_admin"
PASSWORD = "@Blessedbe678@"
PO_NUMBER = "PO196"  # Changed from PR_TITLE to reflect the search term
AMOUNT_TO_RECEIVE = "$100" # Added a parameter for the quantity

def test_create_receipt_from_po():
    with sync_playwright() as p:
        # Launch browser with slow_mo for debugging
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(5)

        # Navigate to Receive
        page.get_by_role("button", name="Manage").click()
        page.get_by_role("menuitem", name="Receive").click()
        time.sleep(3)

        # Search for Purchase Order
        page.locator("input[name=\"_zso4ld\"]").click()
        page.locator("input[name=\"_zso4ld\"]").fill(PO_NUMBER)   
        page.get_by_title("Search for the type of").click()
        time.sleep(3)

        # Enter quantity to receive
        page.locator("input[name=\"_bpyoi\"]").fill(AMOUNT_TO_RECEIVE)
        page.locator("input[name=\"_bpyoi\"]").click()
        time.sleep(3)

        # Submit the receipt
        page.get_by_label("Step Navigation Buttons").get_by_role("button", name="Submit").click()
        time.sleep(5) # Give some time for submission

        # Clean up
        page.close()
        browser.close()

if __name__ == "__main__":
    test_create_receipt_from_po()