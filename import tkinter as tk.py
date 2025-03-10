import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
from playwright.sync_api import sync_playwright

# Function to create PR in SAP Ariba
def create_pr_in_sap_ariba():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()

            # Navigate to SAP Ariba login page
            page.goto("https://s1.au.cloud.ariba.com/Buyer/Main/ad/loginPage/SSOActions?awsso_cc=YXdzc29fcnU6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJqOXlaV0ZzYlQxUVVrVk5TVXRCVkVrdFJFVk5UMFJUUVZCUUxURXRWQT09O3JlYWxtOlVGSkZUVWxMUVZSSkxVUkZUVTlFVTBGUVVDMHhMVlE9O2F3c3NvX2x1OmFIUjBjSE02THk5ek1TNWhkUzVqYkc5MVpDNWhjbWxpWVM1amIyMHZRblY1WlhJdlRXRnBiaTloWkM5amJHbGxiblJNYjJkdmRYUXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2FwOlFuVjVaWEk9O2F3c3NvX2FyaWQ6TVRjME1URTNOemt5TVRNM09RPT07YXdzc29fa3U6YUhSMGNITTZMeTl6TVM1aGRTNWpiRzkxWkM1aGNtbGlZUzVqYjIwdlFuVjVaWEl2VFdGcGJpOWhaQzlqYkdsbGJuUkxaV1Z3UVd4cGRtVXZVMU5QUVdOMGFXOXVjdz09O2F3c3NvX2ZsOk1RPT0%3D%3A6rkroc4Jfac23ceKcu3MLkUeeyM%3D&awsso_ap=Buyer&awsso_hpk=true&awsso_st=1&passwordadapter=PasswordAdapter1&realm=PREMIKATI-DEMODSAPP-1-T&awsr=true")

            # Login
            page.fill("//input[@id='username']", "spandey_prem_admin")
            page.fill("//input[@id='password']", "@Blessedbe678@")
            page.click("//button[@id='login-button']")
            page.wait_for_load_state("networkidle")

            # Navigate to PR page and create PR
            page.click("//a[contains(text(), 'Create')]")
            page.click("//a[contains(text(), 'Purchase Requisition')]")
            page.wait_for_load_state("networkidle")

            page.fill("//input[@id='pr_title']", "Test PR")
            page.fill("//input[@id='pr_description']", "Automated PR creation")

            page.click("//button[contains(text(), 'Submit')]")
            page.wait_for_load_state("networkidle")

            browser.close()

            messagebox.showinfo("Success", "Purchase Requisition created successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Test failed: {str(e)}")

# Function to run the test in a separate thread
def run_test():
    threading.Thread(target=create_pr_in_sap_ariba, daemon=True).start()

# Create GUI
root = tk.Tk()
root.title("SAP Ariba Test Automation")

# Load and display logo
logo = from PIL import Image

image_path = r"C:\Users\Supriya Pandey\Pictures\Screenshots\logo.png"
image = Image.open(image_path)
image.show()  # Opens the image
logo = logo.resize((150, 150), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo_img)
logo_label.pack(pady=10)

# Add test execution button
run_button = tk.Button(root, text="Run SAP Ariba PR Test", command=run_test, font=("Arial", 12), bg="blue", fg="white")
run_button.pack(pady=10)

# Run the GUI
root.mainloop()
