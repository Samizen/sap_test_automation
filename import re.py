import time
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGN4TmpZeU1qazBOalU0TlE9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3AMegtIfsrz8OB62dn0rQZYiGAHao%3D&awsso_ap=Buyer&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0")
    page.get_by_role("textbox", name="User Name").fill("spaudel_prem_admin")
    page.get_by_text("Password", exact=True).click()
    page.get_by_role("textbox", name="Password").fill("Iam@Panda123")
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)
    page.get_by_role("button", name="More...").click()
    page.get_by_role("menuitem", name="Catalog").click()
    time.sleep(10)
    page.get_by_role("textbox").click()
    page.get_by_role("textbox").fill("book bins")
    page.get_by_role("textbox").press("Enter")
    page.locator("[id=\"_klrnhb\"]").click()
    page.locator("[id=\"_klrnhb\"]").fill("20")
    page.locator("[id=\"_nmscpc\"]").click()
    page.get_by_role("button", name="Proceed to Checkout").click()
    time.sleep(10)
    page.get_by_role("textbox", name="Title:").fill("Test PR 02")
    page.get_by_role("button", name="Select Date").click()
    page.get_by_role("link", name="12").click()
    page.get_by_label("Wizard Action Buttons").get_by_role("button", name="Submit").click()
    page.get_by_role("button", name="View Requisition").click()
    page.get_by_role("link", name="Company Logo").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)