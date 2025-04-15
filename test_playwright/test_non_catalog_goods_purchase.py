from test_playwright.config import User_details
from playwright.sync_api import sync_playwright
from test_playwright.test_login import login_ariba
import time

USERNAME = User_details.user
PASSWORD = User_details.password

def test_example():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Step 1 - Login to "Advanced B&I"
        login_ariba(page, USERNAME, PASSWORD)
        page.wait_for_load_state("networkidle")
        time.sleep(10)

        # Navigate to Catalog Tab
        page.get_by_role("button", name="More...").click()
        page.get_by_role("menuitem", name="Catalog").click()
        page.wait_for_load_state("networkidle")
        time.sleep(10)

        # Click Add Non-Catalog Item button
        page.get_by_role("button", name="Add Non-Catalog Item").click()

        page.get_by_role("textbox", name="Full Description:").fill("Blah...Blah...Blah...")
        page.get_by_role("combobox", name="Commodity Code:").click()
        page.get_by_role("combobox", name="Commodity Code:").fill("Drugs and Pharmaceutical Products")
        # page.get_by_role("combobox", name="Commodity Code:").press("Enter")
        page.locator("[id=\"_ibdxyc\"]").get_by_role("link").click()
        page.get_by_role("option", name="DEFAULT ERP Commodity Code").dblclick()
        page.get_by_role("combobox", name="Account Type:").locator("span").nth(1).click()
        page.get_by_role("option", name="Expense").click()
        page.get_by_role("textbox", name="Quantity:").click()
        page.get_by_role("textbox", name="Quantity:").fill("10")
        page.get_by_role("textbox", name="Price:").click()
        page.get_by_role("textbox", name="Price:").fill("$50")
        page.get_by_role("button", name="Update Amount").click()

        time.sleep(50)
        