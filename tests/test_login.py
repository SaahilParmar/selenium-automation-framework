"""
Tests for the login functionality of OrangeHRM demo site using Selenium and Pytest,
refactored to use the Page Object Model (POM).
"""

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_success(driver):
    """
    Test that a user can log in with valid credentials using the Page Object Model.
    Asserts that the dashboard page is reached after login.
    """
    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)

    login_page.load()
    login_page.enter_username(config.username)
    login_page.enter_password(config.password)
    login_page.click_login()

    assert dashboard_page.is_dashboard_visible(), "Dashboard page was not reached after login."

def test_login_invalid_credentials(driver):
    """
    Test that login fails with invalid credentials using the Page Object Model.
    Asserts that an error message is displayed.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Wait for the error message to be visible
    wait = WebDriverWait(driver, 10)
    error_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]"))
    )
    assert "Invalid credentials" in error_message.text, "Expected error message not displayed for invalid login."
