import time, re
from playwright.sync_api import Playwright, sync_playwright, expect
from test_playwright.test_act_as import act_as
from test_playwright.test_login import login_ariba
from test_playwright.config import User_details

USERNAME = User_details.user
PASSWORD = User_details.password
PR_TITLE = "AT-14"

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

        # Get PR_number for the requisition for later search 
        element = page.locator(".pageHead.w-page-head")
        full_text = element.text_content().strip()
        full_text = re.sub(r'\s*-\s*', ' - ', full_text)  # normalise spacing around hyphen
        PR_number = full_text.split(" - ")[0].strip()
        print("Extracted PR Number:", PR_number)

        approver_names = []

        # Locate all approval boxes
        # approval_users = page.locator(".apvBorder.BoldBorder.w-apvActive-cell")
        approval_links = page.locator('a.apvLink[title^="Active"][bh="HL"]')
        print(approval_links)
        count = approval_links.count() # 2 boxes

        if count == 0:
            print("No approval boxes found!")
        else:
            print(f"Total Approvers: {count}")

        # Loop through approval boxes
        for i in range(1,count): 
            print(f"Processing Approver Box {i+1}")
            user = approval_links.nth(i)
            print(user)
            print(f"Found approval link {i}")
            user.click()
            page.wait_for_timeout(1000)
            print("page: ",page)

            # Check for group approver table
            table = page.locator("text=Users who can approve:")
            print("printing table: ",table.inner_text())
            print("table.count()",table.count())

            if table.count() > 0:
                print("[Group] Detected group approver. Extracting user from group...")
                try:
                    first_user = table.locator("xpath=../../following-sibling::tr//a").first.text_content()
                    print(first_user)
                    print(f"[Group → User] Found approver: {first_user}")
                except Exception as e:
                    print("[Group] Could not extract user from group table!", e)
                    continue
            else:
                # Handle individual approver
                try:
                    print("Entered name::::")
                    approver_name = page.locator('tr:has-text("Name:") >> td.ffp-noedit').first.inner_text().strip()
                    print(f"[User] Found approver: {approver_name}")
                    first_user=approver_name
                except Exception as e:
                    print("[User] Approver link not found!", e)
                    continue

            print("press done ....................")
            time.sleep(5)
            # page.get_by_role("button", name="Done").click()
            print("pressed.")
            approver_names.append(first_user)
            page.wait_for_timeout(1000)
        page.get_by_alt_text("Company Logo").click()


        print(approver_names)
        # Act and approve for each approver
        for name in approver_names:
            print(f"\n--- Acting as: {name} ---")
            act_as(page, name)
            time.sleep(5)
            approve_pr(page, PR_number)
            page.wait_for_load_state("networkidle")


def approve_pr(page, PR_no):
    page.get_by_role("tab", name="Home").click()
    # headers = page.locator("table th")
    # header_texts = headers.all_inner_texts()
    # id_col_index = next((i for i, text in enumerate(header_texts) if text.strip() == "ID"), None)
    # print("ids: ",id_col_index)
    # time.sleep(4)
    pr_links=page.locator(f"a:has-text('{PR_no}')").all()
    done=0
    for link in pr_links:
        try:
            print(link)
             # page.click(f"a:has-text('{PR_no}')")
            # page.locator("[id=\"_et6pk\"]").get_by_role("link", name=PR_no).click()
            link.click()
            time.sleep(2)
            page.get_by_role("button", name="Approve").click()
            time.sleep(2)
            page.get_by_role("button", name="OK").click()
            # Go back to homepage
            page.get_by_alt_text("Company Logo").click()
            time.sleep(3)
            page.get_by_text("Stop").click()
            done=1
            
        except Exception as e:
            print(f"link: {link} not working", e)

        if not done:
            raise Exception("Approve not completed.")
   
