import time
from playwright.sync_api import sync_playwright
from test_playwright.test_login import login_ariba

# Parameters for test case
USERNAME = "spaudel_prem_admin"
PASSWORD = "Iam@Panda123"
SEARCH_ITEM = "book bins"
QUANTITY = "10"
REQUISITION_TITLE = "Test PR 06 GB"
GUIDED_BUYING_URL = "https://s1.au.cloud.ariba.com/gb/?realm=PREMIKATI-DEMODSAPP-1-T&locale=en_US"

def test_create_pr():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(5)

        # Navigate to Guided Buying
        page.get_by_role("tab", name="Home").click()
        page.get_by_role("link", name="Guided Buying Redirect Link").click()
        page.goto(GUIDED_BUYING_URL)

        # Search for an item
        search_box = page.get_by_role("textbox", name="Find goods and services")
        search_box.click()
        search_box.fill(SEARCH_ITEM)
        page.get_by_role("button", name="Find goods and services").click()

        # Select and add item to cart
        page.hover('div.thumbnail.result-item-with-image')
        qty_box = page.get_by_role("textbox", name="Change quantity each")
        qty_box.click()
        qty_box.fill(QUANTITY)
        page.get_by_role("button", name="Add to cart").click()

        # Proceed to checkout
        page.get_by_role("button", name="Go to checkout").click()

        # Update requisition title
        req_title_box = page.get_by_role("textbox", name="Requisition title Required")
        req_title_box.click()
        req_title_box.fill(REQUISITION_TITLE)

        # Submit PR
        page.get_by_role("button", name="Submit").click()
        page.get_by_role("button", name="Done").click()

        # Cleanup
        context.close()
        browser.close()
