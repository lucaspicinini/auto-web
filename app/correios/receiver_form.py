from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from app.config import config
from app.open_cart.order import Order


class ReceiverForm():
    """
    A class that encapsulates logic to select
    and fill the order receiver form.
    """
    driver: WebDriver

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def fill(self, order: Order) -> None:
        """Fills the receiver form."""

        # Request Correios reverse logistic page and
        # select the logistic method and postcode
        self.driver.get(config.CORREIOS_LOGISTIC_URL)
        config.sleep()
        service_element = self.driver.find_element(
            By.CSS_SELECTOR, 'select[name="servico"]'
        )
        service_select = Select(service_element)
        if order.city.lower() == config.SENDER_CITY:
            service_select.select_by_value(config.CORREIOS_SEDEX)
        else:
            service_select.select_by_value(config.CORREIOS_PAC)
        postcode_input = self.driver.find_element(By.NAME, "cepOrigem")
        postcode_input.send_keys(order.postcode)
        postcode_confirm = self.driver.find_element(
            By.CSS_SELECTOR, 'input[name="cepOrigem"] + input'
        )
        postcode_confirm.click()
        config.sleep()

        # Fills the form with the receiver data
        postcard_element = self.driver.find_element(By.ID, "cartao")
        postcard_select = Select(postcard_element)
        postcard_select.select_by_value(config.SENDER_POSTCARD)
        fullname_input = self.driver.find_element(By.NAME, "remNome")
        fullname_input.send_keys(order.fullname)
        number_input = self.driver.find_element(By.NAME, "remNumero")
        number_input.send_keys(order.number)
        complement_input = self.driver.find_element(By.NAME, "remComplemento")
        complement_input.send_keys(order.complement)
        ddd_input = self.driver.find_element(By.NAME, "remDDD")
        ddd_input.send_keys(order.ddd)
        telephone_input = self.driver.find_element(By.NAME, "remTelefone")
        telephone_input.send_keys(order.telephone_without_9)
        email_input = self.driver.find_element(By.NAME, "remEmail")
        email_input.send_keys(order.email)
