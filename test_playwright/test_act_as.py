import time
from playwright.sync_api import Playwright, sync_playwright
from test_playwright.test_login import login_ariba

USERNAME = "spaudel_prem_admin"
PASSWORD = "Iam@Panda123"
user = "Subash Banjade"

def act_as(page, act_as_user):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()

    # login_ariba(page, USERNAME, PASSWORD)
    page.locator('img[alt="Company Logo"][title="Company Logo"]').click()
    time.sleep(5)
    page.get_by_role("button", name="Manage").click()
    page.get_by_role("menuitem", name="Core Administration").click()
    page.get_by_title("User Manager", exact=True).click()
    page.get_by_title("Users").click()
    page.get_by_role("textbox", name="Name:").click()
    page.get_by_role("textbox", name="Name:").fill(act_as_user)
    time.sleep(3)
    page.locator("button[title='Search']").click()
    page.get_by_role("button", name="Actions").click()
    page.get_by_role("menuitem", name="Act As").click()
