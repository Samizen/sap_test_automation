from playwright.sync_api import sync_playwright


class TestScript:

    def __init__(self, ariba_url="", username="", password=""):
        self.ariba_url = ariba_url
        self.username = username
        self.password = password
        return

    def login(self, page):
        page.goto(self.ariba_url)
        page.fill("input#UserName", self.username)
        page.fill("input#Password", self.password)
        page.click("input[title='Sign in to Ariba']")

    def check_and_switch_realm(self, page):
        realm_label = page.locator(".w-header-realmlabel").first
        realm_text = realm_label.inner_text()

        if realm_text.endswith("-C1"):
            print("Already in the correct realm.")
        else:
            print("Switching to the correct realm...")
            page.click("#_7zbt$d")
            page.click("#_ck3em")

    def process(self):
        return
