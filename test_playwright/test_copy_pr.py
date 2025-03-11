import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGMwTVRNeU56TTFOREl4TVE9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3An3XVywctYVxyB59T21NK%2FS6tCAM%3D&awsso_ap=Buyer&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0")
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("spandey_prem_admin") #fill with your username
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("@Blessedbe678@")    #fill with your password
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)
    page.get_by_role("tab", name="Home").click()
    time.sleep(10)
    page.get_by_label("Search and Command Bar").get_by_role("link", name="Requisition").click()   
    time.sleep(10)
    page.wait_for_selector("input[name=\"_icg\\$nd\"]", state="visible")
    page.locator("input[name=\"_icg\\$nd\"]").click()
    page.locator("input[name=\"_icg\\$nd\"]").fill("PR351")    #give your PR ID heree.
    time.sleep(10)
    page.locator("[id=\"_4opwwd\"]").click() #Command to search
    #page.get_by_title("Run this search").click()
    page.get_by_role("link", name="PR351").click()
    time.sleep(10)
    page.get_by_role("button", name="Copy").click(force=True)
    page.get_by_role("combobox", name="Ship To:").click(force=True)  #fill your ship to address here.
    page.locator("[id=\"_bjabzb\"]").get_by_role("link").click(force=True)
    page.get_by_role("option", name="Ariba - Pittsburgh").click(foce=True)  #Fill the delivery address here
    time.sleep(10)  #fill the delivery place
    page.get_by_role("textbox", name="Need-by Date:").fill("03/20/2025") #fill 1 weeek after today
    time.sleep(10)
    page.get_by_role("button", name="Submit").click(force=True)
    time.sleep(10)

    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)