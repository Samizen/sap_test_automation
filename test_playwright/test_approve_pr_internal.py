import time, re, os
from playwright.sync_api import Playwright, sync_playwright, expect
from test_playwright.test_act_as import act_as
from test_playwright.test_login import login_ariba
from test_playwright.config import User_details

USERNAME = User_details.user
PASSWORD = User_details.password
PR_TITLE = "AT-31"


def test_approve_pr_internal():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(10)

        page.get_by_role("tab", name="Home").click()

        # Search and Open Requisition 
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
        time.sleep(10)

        # Get PR_number for the requisition for later search 
        element = page.locator(".pageHead.w-page-head")
        full_text = element.text_content().strip()
        full_text = re.sub(r'\s*-\s*', ' - ', full_text)  # normalise spacing around hyphen
        PR_number = full_text.split(" - ")[0].strip()
        print("Extracted PR Number:", PR_number)
        
        # page.get_by_role("cell", name="Active SG_DEMO_USER_1", exact=True).locator("span").click()
        # page.get_by_role("button", name="OK").click()
        # page.get_by_role("cell", name="Active Finance", exact=True).locator("span").click()
        # page.get_by_role("button", name="OK").click()
        # page.get_by_role("tab", name="Orders").click()

        count = page.locator('div.w-approval-state >> span.w-apv-delete-icon').count()
        print(f"Found {count} approval boxes to process.")

        for _ in range(count):
            # Always get the *first* one available (they reflow)
            delete_icon = page.locator('div.w-approval-state >> span.w-apv-delete-icon').first
            delete_icon.click()
            page.get_by_role("button", name="OK").click()
            time.sleep(2)