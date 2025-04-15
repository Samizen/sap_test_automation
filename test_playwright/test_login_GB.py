from test_playwright.config import User_details
from playwright.sync_api import sync_playwright
from test_playwright.test_login import login_ariba
import time


USERNAME = User_details.user
PASSWORD = User_details.password

def login_GB():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Reuse the login function
        login_ariba(page, USERNAME, PASSWORD)
        page.get_by_role("tab", name="Home").click()

        # Go to Guided Buying directly after login
        with page.expect_popup() as new_page:
            page.locator("text=Guided Buying Redirect Link").click()
        guided_buying_page = new_page.value
        guided_buying_page.goto("https://s1.au.cloud.ariba.com/gb/?realm=PREMIKATI-DEMODSAPP-1-T&locale=en_US")
        browser.close()
    
