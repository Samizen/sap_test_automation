import pytest
from playwright.sync_api import sync_playwright
import time


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Launching the browser with headless=False and slowMo to help with debugging
        browser = p.chromium.launch(headless=False, slow_mo=50)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


def test_create_receipt(page):
    # Navigate to the page
    page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGN4TmpZeU1qazBOalU0TlE9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3AMegtIfsrz8OB62dn0rQZYiGAHao%3D&awsso_ap=Buyer&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0")
    
    # Login
    page.get_by_role("textbox", name="User Name").fill("spaudel_prem_admin")
    page.get_by_role("textbox", name="Password").fill("Iam@Panda123")
    page.get_by_role("button", name="Sign In").click()

    time.sleep(3)
    page.locator('a[role="button"][aria-haspopup="menu"][id="_ydbfdb"]').click()
    page.locator("//a[@id='_ydbfdb']").click()
    page.locator('a[title="Receive"][aria-hidden="false"]').click()

    page.locator('input[id="_zso4ld"]').fill('PO151')
    page.locator('button[title="Search for the type of receipt you specify"]').click()

    # Handle the PR350 and receive actions
    page.get_by_role("button", name="Receive").click()
    page.get_by_role("button", name="Accept All").click()

    # Add Comments and Submit
    page.get_by_role("textbox", name="Comments:").fill("Test Comment")
    page.get_by_label("Step Navigation Buttons").get_by_role("button", name="Submit").click()
