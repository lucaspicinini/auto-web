from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.config import config


class CorreiosLogin():
    """Encapsulates Correios Dashboard login."""
    accept_button: WebElement

    def __init__(self, driver: WebDriver):
        # Enter Correios services panel, fills the
        # admin code in the form and submit it.
        driver.get(config.CORREIOS_PANEL_URL)
        config.sleep()
        admin_code_input = driver.find_element(By.ID, "tx_codigo")
        admin_code_input.send_keys(config.CORREIOS_ADMIN_CODE)
        enter_button = driver.find_element(
            By.CSS_SELECTOR, "td:has(input#tx_codigo) + td input"
        )
        enter_button.click()
        config.sleep()

        # Fills next form with Correios credentials and submit
        email_input = driver.find_element(By.ID, "tx_email")
        password_input = driver.find_element(By.ID, "tx_senha")
        email_input.send_keys(config.CORREIOS_USERNAME)
        password_input.send_keys(config.CORREIOS_PASSWORD)
        enter_button = driver.find_element(
            By.CSS_SELECTOR, "input#tx_senha + input"
        )
        enter_button.click()
        config.sleep()

        # Selects accept button element
        self.accept_button = driver.find_element(
            By.CSS_SELECTOR, '.ui-dialog-buttonset button[type="button"]'
        )

    def accept_terms(self) -> None:
        """Accept terms of use and finish the Correios services login."""
        self.accept_button.click()
        config.sleep()
