from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.url_contains("/dashboard"))
    assert "/dashboard" in driver.current_url

def test_login_invalid_credentials(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    wait = WebDriverWait(driver, 10)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    username_input.send_keys("invalid_user")
    password_input.send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")))
    assert "Invalid credentials" in error_message.text
