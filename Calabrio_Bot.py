from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r'C:\Users\SHKIL\Downloads\chromedriver_win32\chromedriver.exe'

# Set Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Initialize Chrome driver with options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Wait for the page to load
    driver.get("https://login-eu.calabriocloud.com/?realm=/bravo#/")

    # Find the email input field, enter the email, and click "Next"
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'floatingLabelInput17')))
    email = ""
    email_input.send_keys(email)

    # Locate and click the "Next" button by class name
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
    )
    next_button.click()

    # Wait for the password input field to become available
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'floatingLabelInput22')))

    # Enter the password
    password = ""
    password_input.send_keys(password)

    # Submit the login form
    password_input.send_keys(Keys.RETURN)

    # Wait for the next page to load
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'MuiButton-label'))
    )

    # Click on the "Add-Ons" button by XPath
    addons_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Add-Ons']"))
    )
    addons_button.click()

    # Get the handles of all open windows or tabs
    all_handles = driver.window_handles

    # Switch to the new window (assuming it opens in a new window)
    new_window_handle = None
    for handle in all_handles:
        if handle != driver.current_window_handle:
            new_window_handle = handle
            break

    if new_window_handle:
        driver.switch_to.window(new_window_handle)

        # Wait for the "Open" button to become available in the new window
        open_trax_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Open TRAX']//span[text()='Open']"))
        )

        # Click the "Open" button
        open_trax_button.click()

        # Wait for the next page to load in the new window (adjust the XPath as needed)
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='your-next-page-element']"))
        )

        # Capture and print the page source of the next page in the new window
        next_page_source = driver.page_source
        print(next_page_source)

        # Close the new window and switch back to the original one
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # Wait for the button inside the span to become available on the last page
    last_page_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root MuiAutocomplete-popupIndicator jss34']"))
    )

    # Click the button on the last page
    last_page_button.click()

    # Continue with further actions if needed...

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Finally, close the original window or tab
# driver.quit()
