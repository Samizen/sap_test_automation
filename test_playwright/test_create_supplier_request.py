import time
from playwright.sync_api import sync_playwright
from test_playwright.test_login import login_ariba
from test_playwright.config import User_details

# Parameters for test case
USERNAME = User_details.user
PASSWORD = User_details.password
SUPPLIER_REQUEST_URL = User_details.bni_url
SUPPLIER_FULL_LEGAL_NAME = "Test for auto 2"
STREET = "Street"
HOUSE_NUMBER = "1"
STREET_2 = "4"
STREET_3 = "ggg"
DISTRICT = "ff"
POSTAL_CODE = "sss"
CONTACT_FIRST_NAME = "Subash"
CONTACT_LAST_NAME = "Subash"
CONTACT_EMAIL = "subash@gmail.com"
CONTACT_PHONE = "98713"
CONTACT_LANGUAGE = "Arabic"

def test_supplier_request():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(3)

        # Navigate to Supplier Request
        page.locator('//*[@id="_e80f4b"]').click()
        time.sleep(2)
        page.locator('a[role="menuitem"][title="Supplier Request"]').click()
        time.sleep(10)

        # Switch to iframe and fill out the form
        iframe = page.locator("iframe[name=\"SMFrame\"]").content_frame
        iframe.locator("textarea[type=\"textarea\"]").click()
        iframe.locator("textarea[type=\"textarea\"]").fill("Test")
        iframe.get_by_role("textbox", name="Supplier Full Legal Name").click()
        iframe.get_by_role("textbox", name="Supplier Full Legal Name").fill(SUPPLIER_FULL_LEGAL_NAME)
        iframe.get_by_role("textbox", name="Street", exact=True).click()
        iframe.get_by_role("textbox", name="Street", exact=True).fill(STREET)
        iframe.get_by_role("textbox", name="Street", exact=True).press("Tab")
        iframe.get_by_role("textbox", name="House Number").click()
        iframe.get_by_role("textbox", name="House Number").fill(HOUSE_NUMBER)
        iframe.get_by_role("textbox", name="Street 2").click()
        iframe.get_by_role("textbox", name="Street 2").fill(STREET_2)
        iframe.get_by_role("textbox", name="Street 3").click()
        iframe.get_by_role("textbox", name="Street 3").fill(STREET_3)
        iframe.get_by_role("textbox", name="District").click()
        iframe.get_by_role("textbox", name="District").fill(DISTRICT)
        iframe.get_by_role("textbox", name="Postal Code").click()
        iframe.get_by_role("textbox", name="Postal Code").fill(POSTAL_CODE)
        iframe.get_by_role("textbox", name="Contact First Name").click()
        iframe.get_by_role("textbox", name="Contact First Name").fill(CONTACT_FIRST_NAME)
        iframe.get_by_role("textbox", name="Contact First Name").press("Tab")
        iframe.get_by_role("textbox", name="Contact Last Name").fill(CONTACT_LAST_NAME)
        iframe.get_by_role("textbox", name="Contact Last Name").press("Tab")
        iframe.get_by_role("textbox", name="Contact Email").fill(CONTACT_EMAIL)
        iframe.get_by_role("textbox", name="Contact Email").click()
        iframe.get_by_role("textbox", name="Contact Email").fill(CONTACT_EMAIL)
        iframe.get_by_role("textbox", name="Contact Email").press("Tab")
        iframe.get_by_role("textbox", name="Contact Phone").fill(CONTACT_PHONE)
        iframe.get_by_role("textbox", name="Contact Location and").click()
        iframe.get_by_text(CONTACT_LANGUAGE).click()
        iframe.locator("body").press("Tab")
        iframe.get_by_role("button", name="toggle sectionEngagement").press("Tab")
        iframe.locator("smq-label-renderer").filter(has_text="4 Engagement Details (How do").press("Tab")
        iframe.get_by_role("combobox", name="Will this Supplier be on-site?").press("Tab")
        iframe.get_by_role("button", name="Submit").click()
        iframe.get_by_role("button", name="Ignore and submit request").click()
        time.sleep(2)
        iframe.get_by_role("button", name="Done").click()

        # Cleanup
        context.close()
        browser.close()