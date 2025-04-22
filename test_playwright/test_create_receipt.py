from playwright.sync_api import sync_playwright
import time
from test_playwright.test_login import login_ariba
from test_playwright.config import User_details

# Parameters for test case
USERNAME = User_details.user
PASSWORD = User_details.password
PR_TITLE = "AT-18"
# PR_LINK_NAME = "Test PR - E2E2"
COMMENT = "Test Comment"

def test_create_receipt():
    with sync_playwright() as p:
        # Launch browser with slow_mo for debugging
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(5)

        # Navigate to Requisition search
        page.locator('span.a-no-wrap span.a-srch-portlet-category-dropdown').click()
        page.get_by_role("menuitem", name="Requisition").click()
        time.sleep(3)

        # Search for PR
        page.locator("[id=\"_4opwwd\"]").click()
        page.get_by_role("textbox", name="Title:").fill(PR_TITLE)
        time.sleep(3)
        page.locator('//button[@id="_5z$ioc" and @title="Run this search"]').click()

        # Select PR
        page.locator("[id=\"_4ztpcb\"]").get_by_role("link", name=PR_TITLE).click()
        page.locator('a', has_text=PR_TITLE)

        # Receive items
        time.sleep(3)
        page.get_by_role("button", name="Receive").click()
        time.sleep(3)
        page.get_by_role("button", name="Accept All").click()
        page.locator("[id=\"_5avxf\"]").click()

        # Add comments and submit
        page.get_by_role("textbox", name="Comments:").fill(COMMENT)
        page.get_by_label("Step Navigation Buttons").get_by_role("button", name="Submit").click()

        # Clean up
        page.close()
        browser.close()
