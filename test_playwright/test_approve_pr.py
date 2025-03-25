import time
from playwright.sync_api import Playwright, sync_playwright, expect
from test_playwright.test_act_as import act_as
from test_playwright.test_login import login_ariba
from test_playwright.config import User_details

USERNAME = User_details.user
PASSWORD = User_details.password
PR_TITLE = "Test PR - E2E6"

def test_approve_pr():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        login_ariba(page, USERNAME, PASSWORD)
        time.sleep(10)

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
        # Address the number of approval
        approval_users = page.query_selector_all(".apvBorder.BoldBorder.w-apvActive-cell")
        if not approval_users:
            print("No approval boxes found!")  # Debugging
        else:
            print(f"Total Approvers: {len(approval_users)}")  # Debugging


        for user in approval_users:
            print("Entered Loop")
            user.click()
            page.wait_for_timeout(1000)
            approver_link = user.query_selector("a.apvLink.w-approval-link")
            if approver_link:
                approver_name = approver_link.inner_text()
                print(f"Approver Name: {approver_name}")
                act_as(page, approver_name)
                approve_pr(page)


        print("Finished!!!")

def approve_pr(page):
    page.locator("[id=\"_x$y1xc\"]").click()
    page.get_by_role("menuitem", name="Approve (5)").click()
    page.get_by_role("cell", name="Approvable Type:").locator("span").nth(2).click()
    page.get_by_role("option", name="Requisition").click()
    page.get_by_role("link", name="Test PR - E2E6").click()
    page.get_by_role("button", name="Approve").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("link", name="Company Logo").click()

        # # ---------------------
        # context.close()
        # # input("Press Enter to close the browser...")
        # browser.close()


# Login
# Find designated PR
    # Find the numbers of Approvers - for loop
        # Click the Group 
        # Find the first user to approve
        # (create a function to Act as here - parameter "User name")
        # Go back to home
            # Goto "Manage" > "Core Administration" > "User Manager" > "Users"
            # Search for the name of this user - Type the user name and then click on Search
            # On the lower result, click on Action and then Act As - will redirect to the Home Screen

