"""
Tests for the login functionality of OrangeHRM demo site using Selenium and Pytest.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    """
    Test that a user can log in with valid credentials.
    Asserts that the dashboard page is reached after login.
    """
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait = WebDriverWait(driver, 10)
    
    # Wait for username and password fields to be present
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    
    # Enter valid credentials
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    
    # Click the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Wait for the dashboard URL to appear
    wait.until(EC.url_contains("/dashboard"))
    assert "/dashboard" in driver.current_url

def test_login_invalid_credentials(driver):
    """
    Test that login fails with invalid credentials.
    Asserts that an error message is displayed.
    """
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait = WebDriverWait(driver, 10)
    
    # Wait for username and password fields to be present
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    
    # Enter invalid credentials
    username_input.send_keys("invalid_user")
    password_input.send_keys("wrong_password")
    
    # Click the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Wait for the error message to be visible
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")))
    assert "Invalid credentials" in error_message.text
