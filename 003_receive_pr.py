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

# Example usage:
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

# Calling the login function
check_and_switch_realm(driver)

def search_and_open_pr(driver, pr_title="Test PR 02"):
    try:
        # 1. Click on Home tab
        home_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@role='tab' and text()='Home']"))
        )
        home_tab.click()
        print('Home clicked')

        print('10 sec wait started...')
        time.sleep(5)
        print('10 sec wait ended...')
        
        # 2. Click on the Requisition dropdown
        requisition_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='_1eckkc']"))
        )
        requisition_dropdown.click()
        print('Requistion dropdown clicked!!')

        # 3. Select Requisition from the dropdown
        requisition_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='_j5uqud']"))
        )
        requisition_option.click()
        print('Requistion selected!!')

        time.sleep(5)
        # 4. Enter the PR title in the search box
        search_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value='Title']"))
        )
        search_box.click()
        search_box.send_keys(pr_title)
        print(pr_title)

        # 5. Click the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[//div[@data-icon='']]"))
        )
        search_button.click()

        time.sleep(5)
        # 5. Find the PR with the matching title
        pr_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"/html[1]/body[1]/div[6]/div[3]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/div[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[2]/td[5]/span[1]/table[1]/tbody[1]/tr[1]/td[1]/a[1]"))
        )
        pr_link.click()

        # 6. Check if the PR title matches the expected title
        pr_title_element = pr_link.find_element(By.XPATH, "..")  # Get the parent <td> element
        if pr_title_element.text == pr_title:
            print(f"Found PR with title: {pr_title}")
            pr_link.click()  # Click on the PR title to open it
        else:
            print(f"PR with title '{pr_title}' not found.")


    except TimeoutException:
        print("Error: Could not find the necessary elements.")
    except Exception as e:
        print(f"Error during receive_pr: {e}")

search_and_open_pr(driver)

def receive_pr(driver):
    try:
        # 1. Click on Receive button
        receive_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Receive')]"))
        )
        receive_button.click()

        # 2. Click on Accept All button
        accept_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Accept All')]"))
        )
        accept_all_button.click()


        time.sleep(5)
        # 3. Click on Submit button
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Submit this receipt for approval']"))
        )
        submit_button.click()

        # 4. Click on Home link
        home_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Home')]"))
        )
        home_link.click()

    except TimeoutException:
        print("Error: Could not find the necessary elements.")
    except Exception as e:
        print(f"Error during receive_pr: {e}")


receive_pr(driver)
input("Press Enter to close the browser...")
driver.quit()