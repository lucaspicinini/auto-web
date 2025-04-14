from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from app.config import config


class LogisticCode():
    """
    Creates a namespace for reverse
    logistic generation action.
    """

    @staticmethod
    def authorize(driver: WebDriver) -> str | None:
        """Returns a unique reverse logistic code."""
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

        return authorization_post_code
