from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.config import config
from app.correios.login import CorreiosLogin
from app.correios.receiver_form import ReceiverForm
from app.correios.sender_form import SenderForm
from app.messages.utils import Utils
from app.open_cart.login import OpenCartLogin
from app.open_cart.order import Order


def main():
    print("Logando no OpenCart...")
    chrome_options: Options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)
    driver: WebDriver = webdriver.Chrome(chrome_options)
    open_cart_login: OpenCartLogin = OpenCartLogin(driver)

    order_id: str = input("Digite um pedido: ")
    print(f"Buscando pedido {order_id} no sistema...")
    order: Order = Order(driver, open_cart_login.user_token, order_id)

    print("Logando no sistema dos Correios...")
    correios_login: CorreiosLogin = CorreiosLogin(driver)
    correios_login.accept_terms()

    print("Enviando informações do pedido para os Correios...")
    receiver_form: ReceiverForm = ReceiverForm(driver)
    receiver_form.fill(order)
    sender_form: SenderForm = SenderForm(driver)
    sender_form.fill()

    print("Gerando etiqueta de postagem...")
    generate_logistic_button: WebElement = driver.find_element(
        By.NAME, "btnEnviar"
    )
    generate_logistic_button.click()
    config.sleep()
    driver.switch_to.alert.accept()
    config.sleep()

    authorization_post_code: str | None = driver\
        .find_element(By.CSS_SELECTOR, 'font[color="red"] > b')\
        .get_attribute("innerText")
    date: datetime = datetime.now()
    expire_date: datetime = (datetime.now() + timedelta(days=30))

    reverse_logistic_msg: str = Utils.generate_logistic_msg(
        order.firstname,
        order.fullname,
        authorization_post_code,
        date.strftime("%d/%m/%Y"),
        expire_date.strftime("%d/%m/%Y"),
        order.service
    )
    print(reverse_logistic_msg)

    # input("Pressione enter para encerrar")
