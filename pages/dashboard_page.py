from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.TAG_NAME, "h6")

    def is_dashboard_visible(self):
        return "dashboard" in self.driver.current_url.lower()
