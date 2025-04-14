from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from app.correios.login import CorreiosLogin
from app.correios.logistic_code import LogisticCode
from app.correios.receiver_form import ReceiverForm
from app.correios.sender_form import SenderForm
from app.messages.utils import Utils
from app.open_cart.login import OpenCartLogin
from app.open_cart.order import Order


def main(order_id: str) -> None:
    print("Logando no OpenCart...")
    chrome_options: Options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("detach", True)
    driver: WebDriver = webdriver.Chrome(chrome_options)
    open_cart_login: OpenCartLogin = OpenCartLogin(driver)

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
    authorization_post_code: str | None = LogisticCode.authorize(driver)

    reverse_logistic_msg: str = Utils.generate_logistic_msg(
        order,
        authorization_post_code,
        datetime.now(),
        datetime.now() + timedelta(days=30),
    )

    print(reverse_logistic_msg)

    # input("Pressione enter para encerrar")
