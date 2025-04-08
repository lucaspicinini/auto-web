from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

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

    # Automatic Confirm
    # generate_logistic_button = driver.find_element(By.NAME, "btnEnviar")
    # generate_logistic_button.click()
    # config.sleep()

    input("Pressione enter para encerrar")
