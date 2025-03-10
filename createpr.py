from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsr=true&realm=PREMIKATI-DEMODSAPP-1-T&awsso_hpk=true&awsso_ap=Buyer&awsso_cc=cmVhbG06VUZKRlRVbExRVlJKTFVSRlRVOUVVMEZRVUMweExWUT07YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJqOXlaV0ZzYlQxUVVrVk5TVXRCVkVrdFJFVk5UMFJUUVZCUUxURXRWQT09O2F3c3NvX2x1OmFIUjBjSE02THk5ek1TNWhkUzVqYkc5MVpDNWhjbWxpWVM1amIyMHZRblY1WlhJdlRXRnBiaTloWkM5amJHbGxiblJNYjJkdmRYUXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2FwOlFuVjVaWEk9O2F3c3NvX2FyaWQ6TVRjME1EUTNNVEEwTURRNE13PT07YXdzc29fa3U6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUkxaV1Z3UVd4cGRtVXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2ZsOk1RPT0%3D%3AfNTfjFMgp1pNOPj%2FuxTWezawJEg%3D")
driver.maximize_window()

# Step 1: Login
driver.find_element(By.ID, "username").send_keys("your_username")
driver.find_element(By.ID, "password").send_keys("your_password")
driver.find_element(By.ID, "loginButton").click()
time.sleep(5)

# Step 2: Navigate to Purchase Requisition Page
driver.find_element(By.LINK_TEXT, "Create").click()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Requisition").click()
time.sleep(5)

# Step 3: Add Item to PR
driver.find_element(By.ID, "searchCatalog").send_keys("Laptop")
driver.find_element(By.ID, "searchCatalog").send_keys(Keys.RETURN)
time.sleep(3)

# Select First Item
driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()
time.sleep(2)

# Step 4: Proceed to Checkout
driver.find_element(By.ID, "checkoutButton").click()
time.sleep(5)

# Step 5: Submit PR
driver.find_element(By.ID, "submitPR").click()
time.sleep(3)

# Validate PR Creation
pr_id = driver.find_element(By.XPATH, "//span[@class='pr-number']").text
print(f"Purchase Requisition Created: {pr_id}")

# Close Browser
driver.quit()
