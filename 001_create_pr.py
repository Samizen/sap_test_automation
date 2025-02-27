from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.common.exceptions import TimeoutException
import time

# Initialize Chrome WebDriver using webdriver_manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def login(driver, username, password):
    try:
        # Open the specified URL - Premikati
        driver.get("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsr=true&realm=PREMIKATI-DEMODSAPP-1-T&awsso_ap=Buyer&awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlrWldaaGRXeDBMMFJwY21WamRFRmpkR2x2Ymo5eVpXRnNiVDFRVWtWTlNVdEJWRWt0UkVWTlQwUlRRVkJRTFRFdFZBPT07YXdzc29fbHU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUk1iMmR2ZFhRdlUxTlBRV04wYVc5dWN3PT07YXdzc29fYXA6UW5WNVpYST07YXdzc29fYXJpZDpNVGN4TmpZeU1qazBOalU0TlE9PTthd3Nzb19rdTphSFIwY0hNNkx5OXpNUzVoZFM1amJHOTFaQzVoY21saVlTNWpiMjB2UW5WNVpYSXZUV0ZwYmk5aFpDOWpiR2xsYm5STFpXVndRV3hwZG1VdlUxTlBRV04wYVc5dWN3PT07YXdzc29fZmw6TVE9PQ%3D%3D%3AMegtIfsrz8OB62dn0rQZYiGAHao%3D#b0")

        # Wait for the username input to be visible and type in the username
        username_textbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='UserName']"))
        )
        username_textbox.send_keys(username)

        # Wait for the password input to be visible and type in the password
        password_textbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='Password']"))
        )
        password_textbox.send_keys(password)

        # 5. Click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@title='Sign in to Ariba']"))
        )
        login_button.click()

    except Exception as e:
        print(f"Error during login: {e}")

username = 'spaudel_prem_admin'
password = 'Iam@Panda123'

login(driver, username, password)  # Call the login function


def check_and_switch_realm(driver):
    try:
        # 1. Wait for the realm label to be present
        realm_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "w-header-realmlabel"))
        )

        # 2. Check if the realm ends with '-C1'
        if realm_label.text.endswith("-C1"):
            print("Already in the correct realm.")
        else:
            print("Switching to the correct realm...")

            # 3. Click on the "Site" menu
            site_menu = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "_7zbt$d"))  # Replace with the actual ID if it's different
            )
            site_menu.click()

            # 4. Click on the realm link (replace with the actual ID if needed)
            realm_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "_ck3em"))  # Replace with the actual ID if it's different
            )
            realm_link.click()

    except TimeoutException:
        print("Error: Could not find realm label or menu items.")
    except Exception as e:
        print(f"Error during realm check and switch: {e}")

# ... (Call the function after login) ...
check_and_switch_realm(driver)

def create_purchase_requisition(driver, quantity=100, search_parameter="book bins", pr_title="Test PR 03"):
    try:
        # Click on More... dropdown
        more_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'More...')]"))
        )
        more_tab.click()
        print('More tab clicked')

        time.sleep(3)
        # 1. Click on Catalog tab
        catalog_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html[1]/body[1]/div[6]/div[3]/div[2]/div[1]/a[7]"))
        )
        catalog_option.click()

        time.sleep(15)  

        # 2. Search for the item
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='Search by part #, supplier name, or keyword']"))  # Corrected XPath
        )
        search_box.click()
        search_box.send_keys(search_parameter)
        print("Search Textbox Entered!!!")

        # 3. Click the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='_pcfaab']"))
        )
        search_button.click()

        print('10 sec sleep started...')
        time.sleep(10)  
        print('10 sec sleep ended...')

        # 4. Wait for the checkbox to be clickable and check it
        # checkbox = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "_dj243c"))
        # )
        # checkbox.click()
        # print('Checkbox Clicked!!!')

        # 5. Wait for the quantity textbox to be visible and update quantity
        quantity_textbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "_klrnhb"))
        )
        quantity_textbox.clear()
        quantity_textbox.send_keys(str(quantity))

        # 6. Wait for the Add to Cart button to be clickable and click it
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "_nmscpc"))
        )
        add_to_cart_button.click()

        # 6. Click on Proceed to Checkout button
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Proceed to Checkout']"))
        )
        checkout_button.click()

        # 7. Enter title
        title_textbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='_mbpnyb']"))
        )
        title_textbox.send_keys(pr_title)

        # 8. Enter today + 7 days date in the delivery date field
        today = datetime.date.today()
        delivery_date = today + datetime.timedelta(days=7)  # Calculate 7 days from today
        delivery_date_str = delivery_date.strftime("%a, %d %b, %Y")  # Format the date
        delivery_date_textbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='_gqzoyb']"))
        )
        delivery_date_textbox.send_keys(delivery_date_str)

        # 9. Click on Submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='_qp3dcd' and contains(., 'Submit')]"))
        )
        submit_button.click()

        time.sleep(5)
        
        view_requisition_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'View Requisition')]"))
        )
        view_requisition_button.click()


    except TimeoutException:
        print("Error: Could not find the necessary elements.")
    except Exception as e:
        print(f"Error during purchase requisition creation: {e}")


create_purchase_requisition(driver)
input("Press Enter to close the browser...")
driver.quit()
