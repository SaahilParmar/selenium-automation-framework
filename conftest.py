import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    """
    Add custom command-line options to pytest.

    Args:
        parser: The pytest parser object.

    Adds:
        --browser: Specify the browser to run tests (default: chrome).
        --headless: Run tests in headless mode if specified.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")


@pytest.fixture
def driver(request):
    """
    Pytest fixture to initialize and provide a Selenium WebDriver instance.

    Reads command-line options for browser type and headless mode.
    Currently supports only Chrome.

    Args:
        request: Pytest's built-in fixture to access test context and config.

    Yields:
        driver: Selenium WebDriver instance for use in tests.

    Quits the driver after the test completes.
    """
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = Options()
        if headless:
            
            # Add Chrome options for headless execution
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        # Set up Chrome WebDriver using webdriver_manager for automatic driver management
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield driver
    
    # Quit the browser after the test is done
    driver.quit()
