class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        self.driver.find_element(*by_locator).click()

    def enter_text(self, by_locator, value):
        self.driver.find_element(*by_locator).send_keys(value)

    def get_title(self):
        return self.driver.title
