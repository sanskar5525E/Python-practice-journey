from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, url, username_selector, password_selector, submit_selector, username, password):
    """
    Automates login to a website using Selenium.
    
    Args:
    - driver: Selenium WebDriver instance (e.g., Chrome).
    - url: The login page URL.
    - username_selector: CSS selector for the username field (e.g., '#username').
    - password_selector: CSS selector for the password field (e.g., '#password').
    - submit_selector: CSS selector for the submit button (e.g., 'button[type="submit"]').
    - username: Your username string.
    - password: Your password string.
    
    Returns: True if login appears successful (e.g., redirected), False otherwise.
    """
    try:
        # Navigate to the login page
        driver.get(url)
        
        # Wait for the username field to be present and enter username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, username_selector)))
        driver.find_element(By.CSS_SELECTOR, username_selector).send_keys(username)
        
        # Enter password
        driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)
        
        # Click submit
        driver.find_element(By.CSS_SELECTOR, submit_selector).click()
        
        # Wait for a post-login element (e.g., a dashboard or success indicator)
        # Adjust this based on the site; here, we check if URL changes or a specific element appears
        WebDriverWait(driver, 10).until(EC.url_changes(url))  # Or use EC.presence_of_element_located for a specific element
        
        print("Login successful!")
        return True
    except Exception as e:
        print(f"Login failed: {e}")
        return False

# Usage example
if __name__ == "__main__":
    # Set up the driver (adjust path to your WebDriver)
    service = Service('/path/to/chromedriver')  # Replace with your ChromeDriver path
    driver = webdriver.Chrome(service=service)
    
    # Call the function with site-specific details
    success = login(
        driver=driver,
        url="https://example.com/login",  # Replace with actual login URL
        username_selector="#username",    # Replace with actual CSS selector
        password_selector="#password",    # Replace with actual CSS selector
        submit_selector="button[type='submit']",  # Replace with actual CSS selector
        username="your_username",
        password="your_password"
    )
    
    if success:
        # Proceed with further automation (e.g., scrape data)
        pass
    
    driver.quit()  # Close the browser
