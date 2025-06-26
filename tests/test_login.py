from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    wait = WebDriverWait(driver, 10)

    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    submit_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")
    submit_button.click()

    # Validate that dashboard is loaded
    wait.until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()
