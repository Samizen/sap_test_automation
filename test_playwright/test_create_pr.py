import time
from playwright.sync_api import Playwright, sync_playwright
from test_playwright.test_login import login_ariba

# Parameters for test case
USERNAME = "spaudel_prem_admin"
PASSWORD = "Iam@Panda123"
SEARCH_ITEM = "book bins"
QUANTITY = "3"
PR_TITLE = "Test PR - E2E5"
DELIVERY_DATE = "22" 

def test_create_pr():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(10)

        # Navigate to Catalog
        page.get_by_role("button", name="More...").click()
        page.get_by_role("menuitem", name="Catalog").click()
        time.sleep(5)

        # Search for item
        page.get_by_role("textbox").click()
        time.sleep(5)
        page.get_by_role("textbox").fill(SEARCH_ITEM)
        time.sleep(10)
        page.locator("//span[@class='a-cat-srch-submit-icn']").click()

        # Set quantity
        page.locator("[id=\"_klrnhb\"]").click()
        page.locator("[id=\"_klrnhb\"]").fill(QUANTITY)
        page.locator("[id=\"_nmscpc\"]").click()

        # Proceed to checkout
        page.get_by_role("button", name="Proceed to Checkout").click()

        # Fill PR details
        page.get_by_role("textbox", name="Title:").fill(PR_TITLE)
        page.get_by_role("button", name="Select Date").click()
        page.get_by_role("link", name=DELIVERY_DATE).click()

        time.sleep(3)

        # Submit PR
        page.get_by_role("button", name="Submit").first.click()
        page.get_by_role("button", name="View Requisition").click()
        page.get_by_role("link", name="Company Logo").click()

        # Cleanup
        context.close()
        browser.close()
