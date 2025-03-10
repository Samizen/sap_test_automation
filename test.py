import re
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in visible mode for debugging
        context = browser.new_context()
        page = context.new_page()

        # Open login page
        page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?realm=PREMIKATI-DEMODSAPP-1-T")

        # Login
        page.wait_for_selector("input[name='UserName']")
        page.fill("input[name='UserName']", "spandey_prem_admin")
        page.wait_for_selector("input[name='Password']")
        page.fill("input[name='password']", "@Blessedbe678@")
        page.click("button:has-text('Sign In')")

        # Navigate to Guided Buying
        page.wait_for_selector("a:has-text('Company Logo')")
        page.click("a:has-text('Company Logo')")

        with page.expect_popup() as popup_info:
            page.click("a:has-text('Guided Buying Redirect Link')")
        popup_page = popup_info.value

        # Search for "pen"
        popup_page.wait_for_selector("input[placeholder='Find goods and services']")
        popup_page.fill("input[placeholder='Find goods and services']", "pen")
        popup_page.press("input[placeholder='Find goods and services']", "Enter")

        # Add item to cart
        popup_page.wait_for_selector("button:has-text('Add to cart')")
        popup_page.click("button:has-text('Add to cart')")
        popup_page.click("button:has-text('Go to checkout')")

        # Select shipping and cost details
        popup_page.click("button:has-text('')")  # Make sure this selector is correct
        popup_page.click("button:has-text('19')")
        popup_page.click("select[name='Ship To']")
        popup_page.click("option:has-text('Ariba - St. Louis')")

        # Submit order
        popup_page.click("button:has-text('Submit')")
        popup_page.click("button:has-text('View requisition')")

        browser.close()
test_example()