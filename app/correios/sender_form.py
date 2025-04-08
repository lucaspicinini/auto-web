from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app.config import config


class SenderForm():
    """
    A class that encapsulates logic to fill sender form.
    """
    driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill(self) -> None:
        """Fills the sender form."""
        receiver_postcode_input = self.driver.find_element(
            By.NAME, "cepDestino"
        )
        receiver_postcode_input.send_keys(config.SENDER_POSTCODE)
        confirm_receiver_postcode = self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="cepDestino"] + a'
        )
        confirm_receiver_postcode.click()
        config.sleep()
        receiver_name_input = self.driver.find_element(By.NAME, "desNome")
        receiver_name_input.send_keys(config.SENDER_LABEL)
        receiver_number_input = self.driver.find_element(By.NAME, "desNumero")
        receiver_number_input.send_keys(config.SENDER_ADDRESS_NUMBER)
        receiver_ddd_input = self.driver.find_element(By.NAME, "desDDD")
        receiver_ddd_input.send_keys(config.SENDER_DDD)
        receiver_telephone_input = self.driver.find_element(
            By.NAME, "desTelefone"
        )
        receiver_telephone_input.send_keys(config.SENDER_TELEPHONE)
        receiver_email_input = self.driver.find_element(By.NAME, "desEmail")
        receiver_email_input.send_keys(config.SENDER_EMAIL)
