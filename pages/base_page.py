class BasePage:
    """
    Base class for all page objects.
    Provides common methods for interacting with web elements.
    """

    def __init__(self, driver):
        """
        Initialize the BasePage with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    
    def click(self, by_locator):
        """
        Click on the web element specified by the locator.

        Args:
            by_locator (tuple): Locator for the web element (By, value).
        """
        self.driver.find_element(*by_locator).click()

    
    def enter_text(self, by_locator, value):
        """
        Enter text into the web element specified by the locator.

        Args:
            by_locator (tuple): Locator for the web element (By, value).
            value (str): The text to enter.
        """
        self.driver.find_element(*by_locator).send_keys(value)

    
    def get_title(self):
        """
        Get the title of the current page.

        Returns:
            str: The title of the current page.
        """
        return self.driver.title
