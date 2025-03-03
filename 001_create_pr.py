from base import TestScript
from playwright.sync_api import sync_playwright
import time
import datetime


class Create_Pr(TestScript):

    def create_pr(self, page, search_parameter="", quantity=0, pr_title=""):
        try:
            page.wait_for_selector("text=More...").click()
            print('More tab clicked')

            time.sleep(3)

            # Click on Catalog tab
            page.wait_for_selector(
                "xpath=/html[1]/body[1]/div[6]/div[3]/div[2]/div[1]/a[7]"
            ).click()

            time.sleep(15)

            # Search for the item
            search_box = page.wait_for_selector(
                "input[placeholder='Search by part #, supplier name, or keyword']"
            )
            search_box.click()
            search_box.fill(search_parameter)
            print("Search Textbox Entered!!!")

            # Click the search button
            page.wait_for_selector("#_pcfaab").click()

            print('10 sec sleep started...')
            time.sleep(10)
            print('10 sec sleep ended...')

            # Wait for the quantity textbox and update quantity
            quantity_textbox = page.wait_for_selector("#_klrnhb")
            quantity_textbox.fill(str(quantity))

            # Click on Add to Cart button
            page.wait_for_selector("#_nmscpc").click()

            # Click on Proceed to Checkout button
            page.wait_for_selector("a[title='Proceed to Checkout']").click()

            # Enter PR title
            title_textbox = page.wait_for_selector("#_mbpnyb")
            title_textbox.fill(pr_title)

            # Enter delivery date (today + 7 days)
            today = datetime.date.today()
            delivery_date = today + datetime.timedelta(days=7)
            delivery_date_str = delivery_date.strftime("%a, %d %b, %Y")
            delivery_date_textbox = page.wait_for_selector("#_gqzoyb")
            delivery_date_textbox.fill(delivery_date_str)

            # Click on Submit button
            page.wait_for_selector("button#_qp3dcd:has-text('Submit')").click()

            time.sleep(5)

            # Click on View Requisition button
            page.wait_for_selector(
                "button:has-text('View Requisition')").click()

        except Exception as e:
            print(f"Error during purchase requisition creation: {e}")

        return

    def process(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            self.login(page)
            self.check_and_switch_realm(page)
            self.create_pr(page)
            browser.close()
            return


Create_Pr(
    ariba_url=
    "https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsr=true&realm=PREMIKATI-DEMODSAPP-1-T&awsso_ap=Buyer&awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGN4TmpZeU1qazBOalU0TlE9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3AMegtIfsrz8OB62dn0rQZYiGAHao%3D#b0",
    username="",
    password="").process()
