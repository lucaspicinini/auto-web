import time
import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    """
    Set global configs for application
    and binds in a Config() instance.
    """
    SLEEP_TIME: float = 2

    # Credentials
    OPENCART_USERNAME = os.getenv('OPENCART_USERNAME', "")
    OPENCART_PASSWORD = os.getenv('OPENCART_PASSWORD', "")
    CORREIOS_USERNAME = os.getenv('CORREIOS_USERNAME', "")
    CORREIOS_PASSWORD = os.getenv('CORREIOS_PASSWORD', "")
    CORREIOS_ADMIN_CODE = os.getenv('CORREIOS_ADMIN_CODE', "")

    # URLS
    OPENCART_PANEL_URL = os.getenv('OPENCART_PANEL_URL', "")
    OPENCART_ORDER_URL = os.getenv('OPENCART_ORDER_URL', "")
    CORREIOS_PANEL_URL = os.getenv('CORREIOS_PANEL_URL', "")
    CORREIOS_LOGISTIC_URL = os.getenv('CORREIOS_LOGISTIC_URL', "")

    # Sender configuration
    SENDER_CITY = os.getenv('SENDER_CITY', "")
    SENDER_POSTCARD = os.getenv('SENDER_POSTCARD', "")
    SENDER_POSTCODE = os.getenv('SENDER_POSTCODE', "")
    SENDER_LABEL = os.getenv('SENDER_LABEL', "")
    SENDER_ADDRESS_NUMBER = os.getenv('SENDER_ADDRESS_NUMBER', "")
    SENDER_DDD = os.getenv('SENDER_DDD', "")
    SENDER_TELEPHONE = os.getenv('SENDER_TELEPHONE', "")
    SENDER_EMAIL = os.getenv('SENDER_EMAIL', "")

    # Services
    CORREIOS_SEDEX = "03_247_0_9912339721"
    CORREIOS_PAC = "03_301_0_9912339721"

    def sleep(self) -> None:
        time.sleep(self.SLEEP_TIME)


config = Config()
