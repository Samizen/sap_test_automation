import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGMwTVRJME9EVXhNak16Tmc9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3ATymCh4RVvNfhYbiPc0XDQwVRWls%3D&awsso_ap=Buyer&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0")
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("spandey_prem_admin") #Fill your username here
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("@Blessedbe678@") #fill your password here
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)
    page.get_by_role("tab", name="Home").click()
    time.sleep(10)
    page.get_by_role("button", name="Create").click()  #clicking on create option
    time.sleep(10)
    page.get_by_role("menuitem", name="Invoice").click() #Go to Invoice
    time.sleep(10)
    page.locator("label").filter(has_text="PO-Based").locator("label").click() #Click on PO Based
    time.sleep(10)
    page.locator("[id=\"_aeqrid\"]").get_by_role("link").click()
    page.get_by_role("option", name="PO100").click() #Put your PO ID here.
    time.sleep(15)
    page.get_by_role("textbox", name="Supplier Invoice #:").click()
    time.sleep(10)
    page.get_by_role("textbox", name="Supplier Invoice #:").fill("1234") #fill your invoice id here
    time.sleep(5)
    page.get_by_role("textbox", name="Invoice Date:").fill("03/06/2025")
    time.sleep(10) #select date here fill today;s date
    #page.get_by_role("textbox", name="Payment Terms:").fill("") #fill the payment terms here
    #page.get_by_role("combobox",name="Remit To Address:").fill("Utah") #fill your remit to address here.
     # Click on Submit button
    page.locator("[id=\"_5avxf\"]").click()
    time.sleep(10)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
