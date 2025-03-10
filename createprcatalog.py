from playwright.sync_api import sync_playwright

def create_pr_in_sap_ariba():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for running in the background
        context = browser.new_context()
        page = context.new_page()

        # Navigate to SAP Ariba login page
        page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=cGFzc3dvcmRhZGFwdGVyOlVHRnpjM2R2Y21SQlpHRndkR1Z5TVE9PTtyZWFsbTpVRkpGVFVsTFFWUkpMVVJGVFU5RVUwRlFVQzB4TFZRPTthd3Nzb19ydTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZDWndZWE56ZDI5eVpHRmtZWEIwWlhJOVVHRnpjM2R2Y21SQlpHRndkR1Z5TVE9PTthd3Nzb19sdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STWIyZHZkWFF2VTFOUFFXTjBhVzl1Y3c9PTthd3Nzb19hcDpRblY1WlhJPTthd3Nzb19hcmlkOk1UYzBNVEUzTVRBeE5URTJPUT09O2F3c3NvX2t1OmFIUjBjSE02THk5ek1TNWhkUzVqYkc5MVpDNWhjbWxpWVM1amIyMHZRblY1WlhJdlRXRnBiaTloWkM5amJHbGxiblJMWldWd1FXeHBkbVV2VTFOUFFXTjBhVzl1Y3c9PTthd3Nzb19mbDpNUT09%3APZZS1MsmCocFKIYqShpq7QLiR9w%3D&awsso_ap=Buyer&awsso_hpk=true&passwordadapter=PasswordAdapter1&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true")

        # Login to SAP Ariba
        page.fill("//input[@id='UserName']", "spandey_prem_admin")  # Replace with actual username field XPath
        page.fill("//input[@id='Password']", "@Blessedbe678@")  # Replace with actual password field XPath
        page.click("//*[@id='loginForm']/table/tbody/tr[2]/td/input")  # Replace with actual login button XPath
        page.wait_for_load_state("networkidle")

        # Navigate to Purchase Requisition page
        page.click("//a[contains(text(), 'Create')]")  # Replace with actual "Create" menu button XPath
        page.click("//a[contains(text(), ' Requisition')]")  # Replace with actual PR menu XPath
        page.wait_for_load_state("networkidle")

        # Fill out the PR form
        page.fill("//input[@id='pr_title']", "Test Purchase Requisition")  # Replace with PR title field XPath
        page.fill("//input[@id='pr_description']", "Automated PR creation via Playwright")  # Replace with description field XPath

        # Select item category (if required)
        page.click("//select[@id='category']")  
        page.select_option("//select[@id='category']", "IT Equipment")  # Replace with actual option value

        # Add an item to the PR
        page.click("//button[contains(text(), 'Add Item')]")  # Replace with actual add item button XPath
        page.fill("//input[@id='item_name']", "Laptop")  # Replace with item name field XPath
        page.fill("//input[@id='item_quantity']", "2")  # Replace with item quantity field XPath
        page.fill("//input[@id='item_price']", "1500")  # Replace with item price field XPath

        # Submit the PR
        page.click("//button[contains(text(), 'Submit')]")  # Replace with actual submit button XPath
        page.wait_for_load_state("networkidle")

        print("Purchase Requisition created successfully.")

        # Close browser
        browser.close()

if __name__ == "__main__":
    create_pr_in_sap_ariba()
