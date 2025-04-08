from urllib.parse import parse_qs, urlparse

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app.config import config


class OpenCartLogin():
    """Encapsulates OpenCart Admin Dashboard login."""
    user_token: str | None

    def __init__(self, driver: WebDriver):
        # Navigates to admin login page and get form elements
        driver.get(config.OPENCART_PANEL_URL)
        config.sleep()
        username = driver.find_element(By.ID, "input-username")
        password = driver.find_element(By.ID, "input-password")
        submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")

        # Clear inputs, fills form with credentials
        # and submit the form
        username.clear()
        password.clear()
        username.send_keys(config.OPENCART_USERNAME)
        password.send_keys(config.OPENCART_PASSWORD)
        submit_button.click()
        config.sleep()

        # Get the query param user_token from the current URL
        # and binds in the Login instance
        current_url = driver.current_url
        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query)
        self.user_token = query_params.get('user_token', [None])[0]
