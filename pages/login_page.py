from selenium.webdriver.common.by import By

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

    def load(self):
        """
        Navigate to the OrangeHRM login page.
        """
        
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

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
