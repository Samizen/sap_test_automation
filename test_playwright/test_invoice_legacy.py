from playwright.sync_api import sync_playwright
import time
from test_playwright.test_login import login_ariba
from test_playwright.config import User_details

# Parameters for test case
URL = "https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGMwTVRJME9EVXhNak16Tmc9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3ATymCh4RVvNfhYbiPc0XDQwVRWls%3D&awsso_ap=Buyer&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0"
# Parameters for test case
USERNAME = User_details.user
PASSWORD = User_details.password
PO_ID = "PO100"  # Replace with your PO ID
INVOICE_ID = "1234"  # Replace with your invoice ID
INVOICE_DATE = "03/06/2025"  # Replace with your invoice date
REMIT_ADDRESS = "1000005900"  # Replace with your remit address
SEARCH_QUERY = "Test PR - E2E6"  # Replace with your search query

def test_invoice_legacy():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the login page
        page.goto(URL)

        # Login
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(5)

        # Navigate to Home and click Create
        page.get_by_role("tab", name="Home").click()
        time.sleep(5)
        page.get_by_role("button", name="Create").click()
        time.sleep(3)

        # Go to Invoice
        page.get_by_role("menuitem", name="Invoice").click()
        time.sleep(3)

        # Select PO-Based
        page.locator("label").filter(has_text="PO-Based").locator("label").click()
        time.sleep(3)

        # Select PO ID
        page.locator("[id=\"_aeqrid\"]").get_by_role("link").click()
        page.get_by_role("option", name="Search more").click()
        page.get_by_role("combobox", name="Search for a specific value").locator("span").nth(1).click()
        page.get_by_role("option", name="Title").click()
        page.get_by_role("textbox", name="Search for a specific value").click()
        page.get_by_role("textbox", name="Search for a specific value").click()
        page.get_by_role("textbox", name="Search for a specific value").fill(SEARCH_QUERY)
        page.get_by_title("Search for a specific value").click()

        row = page.locator('tr[dr="1"]').filter(has_text=SEARCH_QUERY)
        # Click the checkbox inside the row
        row.locator('input[type="checkbox"]').first.click()

        time.sleep(4)

        # Fill Invoice Details
        page.get_by_role("textbox", name="Supplier Invoice #:").click()
        page.get_by_role("textbox", name="Supplier Invoice #:").fill(INVOICE_ID)
        time.sleep(3)

        # Fill Invoice Date
        page.get_by_role("textbox", name="Invoice Date:").fill(INVOICE_DATE)
        time.sleep(3)

        # Fill Remit Address
        page.locator('input[id="_a_inqd"][type="text"][role="combobox"]').fill(REMIT_ADDRESS)

        # Submit the form
        time.sleep(3)
        page.locator("[id=\"_5avxf\"]").click()

        # Cleanup
        context.close()
        browser.close()