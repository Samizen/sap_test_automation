from test_playwright.config import User_details

def login_ariba(page, username, password):
    page.goto(User_details.bni_url)
    page.get_by_role("textbox", name="User Name").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("Home")