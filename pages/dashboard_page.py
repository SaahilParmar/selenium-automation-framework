from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")

    
    def is_dashboard_visible(self, timeout=20):
        """
        Check if the dashboard page is currently visible by waiting for the dashboard header.

        Args:
            timeout (int): Maximum time to wait for the dashboard header to appear.

        Returns:
            bool: True if the dashboard header is visible, False otherwise.
        """
        try:
            wait = WebDriverWait(self.driver, timeout)
            # Wait for an h6 element that contains the text 'Dashboard'
            header = wait.until(
                EC.visibility_of_element_located(self.dashboard_header)
            )
            return header.is_displayed()
        except:
            return False
