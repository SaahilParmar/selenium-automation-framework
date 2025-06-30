from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object Model for the OrangeHRM login page.
    Encapsulates all interactions with the login page elements.
    """

    def __init__(self, driver):
        """
        Initialize the LoginPage with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance used to interact with the browser.
        """
        
        self.driver = driver
        
        # Locators for the login page elements
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")

        # Locator for the error message
        self.error_message_locator = (By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")

    def load(self):
        """
        Navigate to the OrangeHRM login page and wait for the username field to be visible.
        """
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        )

    def enter_username(self, username):
        """
        Enter the username into the username input field.

        Args:
            username (str): The username to input.
        """
        
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        """
        Enter the password into the password input field.

        Args:
            password (str): The password to input.
        """
        
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """
        Click the login button to submit the login form.
        """
        
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self, timeout=10):
        """
        Wait for and return the error message text displayed after a failed login attempt.

        Args:
            timeout (int): Maximum time to wait for the error message to appear.

        Returns:
            str: The error message text.
        """
        wait = WebDriverWait(self.driver, timeout)
        error_element = wait.until(
            EC.visibility_of_element_located(self.error_message_locator)
        )
        return error_element.text
