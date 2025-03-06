from playwright.sync_api import Page, Playwright, sync_playwright
import time


def test_create_pr():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGN4TmpZeU1qazBOalU0TlE9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3AMegtIfsrz8OB62dn0rQZYiGAHao%3D&awsso_ap=Buyer&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true#b0")
        page.get_by_role("textbox", name="User Name").fill("spaudel_prem_admin")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_text("Password", exact=True).click()
        page.get_by_role("textbox", name="Password").fill("Iam@Panda123")
        page.get_by_role("button", name="Sign In").click()
        time.sleep(5)
        page.get_by_role("tab", name="Home").click()
        page.get_by_role("link", name="Guided Buying Redirect Link").click()
        # with page.expect_popup() as page1_info:
        #     page.get_by_role("link", name="Guided Buying Redirect Link").click()
        #     page1 = page1_info.value
        #     page1.wait_for_load_state()
        page.goto("https://s1.au.cloud.ariba.com/gb/?realm=PREMIKATI-DEMODSAPP-1-T&locale=en_US")
        page.get_by_role("textbox", name="Find goods and services").click()
        page.get_by_role("textbox", name="Find goods and services").fill("book bins")
        page.get_by_role("button", name="Find goods and services").click()
        page.hover('div.thumbnail.result-item-with-image')
        page.get_by_role("textbox", name="Change quantity each").click()
        page.get_by_role("textbox", name="Change quantity each").fill("10")
        page.get_by_role("button", name="Add to cart").click()
        page.get_by_role("button", name="Go to checkout").click()
        page.get_by_role("textbox", name="Requisition title Required").click()
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").press("ControlOrMeta+Shift+ArrowLeft")
        page.get_by_role("textbox", name="Requisition title Required").fill("Test PR 05 GB")
        page.get_by_role("button", name="Submit").click()
        page.get_by_role("button", name="Done").click()
