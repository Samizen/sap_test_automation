import time
from playwright.sync_api import sync_playwright
from test_playwright.test_login import login_ariba

# Parameters for test case
USERNAME = "spandey_prem_admin"
PASSWORD = "@Blessedbe678@"
PR_ID = "PR351"  # Enter the PR ID to copy
SHIP_TO_NAME = "Ariba - Pittsburgh"
NEED_BY_DATE = "03/20/2025"  # Set this dynamically if needed

def test_copy_pr():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(10)

        # Navigate to Requisition search
        page.get_by_role("tab", name="Home").click()
        time.sleep(10)
        page.get_by_label("Search and Command Bar").get_by_role("link", name="Requisition").click()   
        time.sleep(10)

        # Search for PR
        page.wait_for_selector("input[name=\"_icg\\$nd\"]", state="visible")
        page.locator("input[name=\"_icg\\$nd\"]").click()
        page.locator("input[name=\"_icg\\$nd\"]").fill(PR_ID)
        time.sleep(10)
        page.locator("[id=\"_4opwwd\"]").click()  # Search button

        # Select PR and copy it
        page.get_by_role("link", name=PR_ID).click()
        time.sleep(10)
        page.get_by_role("button", name="Copy").click(force=True)

        # Set shipping details
        page.get_by_role("combobox", name="Ship To:").click(force=True)
        page.locator("[id=\"_bjabzb\"]").get_by_role("link").click(force=True)
        page.get_by_role("option", name=SHIP_TO_NAME).click(force=True)
        time.sleep(10)

        # Set need-by date
        page.get_by_role("textbox", name="Need-by Date:").fill(NEED_BY_DATE)
        time.sleep(10)

        # Submit
        page.get_by_role("button", name="Submit").click(force=True)
        time.sleep(10)

        # Cleanup
        context.close()
        browser.close()
