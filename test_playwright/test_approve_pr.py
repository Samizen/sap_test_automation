import time
from playwright.sync_api import Playwright, sync_playwright, expect
from test_playwright.test_act_as import act_as
from test_playwright.test_login import login_ariba

USERNAME = "spaudel_prem_admin"
PASSWORD = "Iam@Panda123"
PR_TITLE = "Test PR - E2E5"

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
        approval_users = page.query_selector_all("div.apvBorder.BoldBorder.w-apvApproved-cell")
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
            # table_row = user.query_selector("tr[id^='_']")
            # if table_row:
            #     name_cell = table_row.query_selector("td.ffp-noedit")
            #     if name_cell:
            #         table_name = name_cell.inner_text().strip()
            #         print(f"Approver Name from Table: {table_name}")
                act_as(page, approver_name)


        print("Finished!!!")


        # page.get_by_role("tab", name="Home").click()
        # page.locator("[id=\"_ikzaw\"]").get_by_role("link", name="Test PR - E2E5").click()
        # page.get_by_role("link", name="Finance").click()
        # page.get_by_role("cell", name="Samit Paudel", exact=True).click()
        # page.get_by_role("link", name="Samit Paudel").click()
        # page.get_by_role("link", name="Go To Dashboard").click()
        # page.locator("[id=\"_ikzaw\"]").get_by_role("link", name="Test PR - E2E5").click()
        # page.get_by_role("link", name="SG_DEMO_USER_1").click()
        # page.locator("[id=\"_vvxidc\"]").get_by_text("SG_DEMO_USER_1").click()
        # page.get_by_role("button", name="Done").click()
        # page.get_by_role("link", name="SG_DEMO_USER_1").click()
        # page.get_by_role("link", name="Go To Dashboard").click()
        # page.get_by_role("button", name="Manage").click()
        # page.get_by_role("menuitem", name="Core Administration").click()
        # page.locator("#tocAlley").get_by_role("row", name="User Manager", exact=True).get_by_role("cell").first.click()
        # page.get_by_role("cell", name="Users", exact=True).click()
        # page.get_by_role("cell", name="Users", exact=True).click()
        # page.get_by_role("link", name="Users").click()
        # page.get_by_role("textbox", name="Name:").click()
        # page.get_by_role("textbox", name="Name:").fill("SG_USER_DEMO")
        # page.get_by_role("textbox", name="Name:").press("Enter")
        # page.get_by_role("textbox", name="Name:").click()
        # page.get_by_role("textbox", name="Name:").press("ArrowLeft")
        # page.get_by_role("textbox", name="Name:").press("ArrowLeft")
        # page.get_by_role("textbox", name="Name:").press("ArrowLeft")
        # page.get_by_role("textbox", name="Name:").press("ArrowLeft")
        # page.get_by_role("textbox", name="Name:").press("ArrowLeft")
        # page.get_by_role("textbox", name="Name:").press("ArrowLeft")
        # page.get_by_role("textbox", name="Name:").fill("USER_DEMO")
        # page.get_by_role("textbox", name="Name:").press("Enter")
        # page.get_by_label("Page Content").get_by_role("button", name="Search").click()
        # page.get_by_role("tab", name="Home").click()
        # page.locator("[id=\"_ikzaw\"]").get_by_role("link", name="Test PR - E2E5").click()
        # page.get_by_role("link", name="Back").click()
        # page.get_by_role("button", name="Manage").click()
        # page.get_by_role("menuitem", name="Core Administration").click()
        # page.get_by_role("link", name="Users").click()
        # page.get_by_role("textbox", name="Name:").click()
        # page.get_by_role("textbox", name="Name:").fill("SG_DEMO_USER")
        # page.get_by_role("textbox", name="Name:").press("Enter")
        # page.get_by_role("button", name="Actions").click()
        # page.get_by_role("menuitem", name="Act As").click()
        # page.get_by_role("tab", name="Home").click()
        # page.locator("[id=\"_mxvubd\"]").click()
        # page.get_by_role("button", name="Approve").click()
        # page.get_by_role("button", name="OK").click()
        # page.get_by_role("tab", name="Home").click()
        # page.get_by_role("link", name="Stop").click()
        # page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/aw?awh=r&awssk=k2t1HDRuhCHHBm4R&realm=PREMIKATI-DEMODSAPP-1-T&dard=1#b1")
        # page.get_by_role("button", name="Manage").click()
        # page.get_by_role("menuitem", name="Core Administration").click()
        # page.locator("#tocAlley").get_by_role("row", name="User Manager", exact=True).get_by_role("link").first.click()
        # page.get_by_role("link", name="Users").click()
        # page.get_by_role("textbox", name="Name:").click()
        # page.get_by_role("textbox", name="Name:").fill("Samit Paudel")
        # page.get_by_role("textbox", name="Name:").press("Enter")
        # page.get_by_role("button", name="Actions").click()
        # page.get_by_role("menuitem", name="Act As").click()
        # page.locator("[id=\"_srxlid\"]").get_by_role("link", name="Test PR - E2E5").click()
        # page.get_by_role("button", name="Show Approval Flow").click()

        # ---------------------
        context.close()
        # input("Press Enter to close the browser...")
        browser.close()


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

