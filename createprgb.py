import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsr=true&realm=PREMIKATI-DEMODSAPP-1-T&passwordadapter=PasswordAdapter1&awsso_st=1&awsso_hpk=true&awsso_ap=Buyer&awsso_cc=YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJqOXlaV0ZzYlQxUVVrVk5TVXRCVkVrdFJFVk5UMFJUUVZCUUxURXRWQT09O3JlYWxtOlVGSkZUVWxMUVZSSkxVUkZUVTlFVTBGUVVDMHhMVlE9O2F3c3NvX2x1OmFIUjBjSE02THk5ek1TNWhkUzVqYkc5MVpDNWhjbWxpWVM1amIyMHZRblY1WlhJdlRXRnBiaTloWkM5amJHbGxiblJNYjJkdmRYUXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2FwOlFuVjVaWEk9O2F3c3NvX2FyaWQ6TVRjME1URTNOemt5TVRNM09RPT07YXdzc29fa3U6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUkxaV1Z3UVd4cGRtVXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2ZsOk1RPT0%3D%3A6rkroc4Jfac23ceKcu3MLkUeeyM%3D")
    page.get_by_role("textbox", name="User Name").click()
    page.get_by_role("textbox", name="User Name").fill("spandey_prem_admin")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("@Blessedbe678@")
    time.sleep(10)
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)
    page.get_by_role("tab", name="Home").click()
    time.sleep(10)
    page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=Z3VpZGVkYnV5cmVkaXJlY3Q6ZEhKMVpRPT07cmVhbG06Y0hKbGJXbHJZWFJwTFdSbGJXOWtjMkZ3Y0MweExYUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOC9jbVZoYkcwOWNISmxiV2xyWVhScExXUmxiVzlrYzJGd2NDMHhMWFFtWjNWcFpHVmtZblY1Y21Wa2FYSmxZM1E5ZEhKMVpRPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGMwTVRJME1EQTJNVEF6TXc9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3AA4fK1lZbPQoletPwL3Yd0qrjTf4%3D&awsso_ap=Buyer&awsso_hpk=true&realm=premikati-demodsapp-1-t&awsr=true")
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Guided Buying Redirect Link").click()
    page1 = page1_info.value
    page1.goto("https://s1.au.cloud.ariba.com/gb/?realm=PREMIKATI-DEMODSAPP-1-T&locale=en_US")
    page1.get_by_role("textbox", name="Find goods and services").click()
    time.sleep(10)
    page1.get_by_role("textbox", name="Find goods and services").fill("pen")
    page1.get_by_role("button", name="Find goods and services").click()
    page1.get_by_role("textbox", name="Change quantity each").click()
    page1.get_by_role("textbox", name="Change quantity each").fill("17")
    page1.get_by_role("button", name="Add to cart").click()
    page1.get_by_role("button", name="Go to checkout").click()
    page1.get_by_role("button", name="").click()
    page1.get_by_role("button", name="13").click()
    page1.get_by_role("combobox", name="Cost Center (no value) Error").click()
    page1.get_by_role("link", name="Ariba - International").click()
    page1.get_by_role("combobox", name="Business Unit (no value)").click()
    page1.get_by_role("link", name="Ariba - Sales").click()
    page1.get_by_role("combobox", name="Company (no value) Error The").click()
    page1.get_by_role("link", name="Ariba - Company 2").click()
    page1.get_by_role("combobox", name="Ship To (no value)").click()
    page1.get_by_role("link", name="Ariba - St. Louis").click()
    page1.get_by_role("button", name="Submit").click()
    page1.get_by_role("button", name="Done").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
