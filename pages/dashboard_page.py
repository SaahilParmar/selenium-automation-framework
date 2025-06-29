from selenium.webdriver.common.by import By

class DashboardPage:
    """
    Page Object Model for the OrangeHRM dashboard page.
    Encapsulates interactions and checks related to the dashboard.
    """

    def __init__(self, driver):
        """
        Initialize the DashboardPage with a Selenium WebDriver instance.

        Args:
            driver: Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        
        # Locator for the dashboard header element
        self.dashboard_header = (By.TAG_NAME, "h6")

    
    def is_dashboard_visible(self):
        """
        Check if the dashboard page is currently visible by verifying the URL.

        Returns:
            bool: True if 'dashboard' is in the current URL, False otherwise.
        """
        return "dashboard" in self.driver.current_url.lower()
