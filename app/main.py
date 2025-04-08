from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.config import config
from app.correios.login import CorreiosLogin
from app.correios.receiver_form import ReceiverForm
from app.correios.sender_form import SenderForm
from app.open_cart.login import OpenCartLogin
from app.open_cart.order import Order


def main():
    driver: WebDriver = webdriver.Chrome()
    open_cart_login: OpenCartLogin = OpenCartLogin(driver)

    order_id: str = input("Digite um pedido: ")
    order: Order = Order(driver, open_cart_login.user_token, order_id)

    correios_login: CorreiosLogin = CorreiosLogin(driver)
    correios_login.accept_terms()

    receiver_form: ReceiverForm = ReceiverForm(driver)
    receiver_form.fill(order)

    sender_form: SenderForm = SenderForm(driver)
    sender_form.fill()

    generate_logistic_button: WebElement = driver.find_element(
        By.NAME, "btnEnviar"
    )
    generate_logistic_button.click()
    config.sleep()
    driver.switch_to.alert.accept()
    config.sleep()

    # # Gets final reverse logistic post code
    # authorization_post_code: str | None = driver\
    #     .find_element(By.CSS_SELECTOR, 'font[color="red"] > b')\
    #     .get_attribute("innerText")
    # print(authorization_post_code)

    input("Pressione enter para encerrar")
