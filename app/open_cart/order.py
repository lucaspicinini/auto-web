from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from app.config import config


class Order():
    """Get an Order() instance with order details."""
    firstname: str | None
    lastname: str | None
    fullname: str
    email: str
    ddd: str
    telephone: str
    telephone_without_9: str
    address: str
    number: str
    complement: str
    neighborhood: str
    postcode: str
    city: str

    def __init__(
        self, driver: WebDriver, user_token: str | None, order_id: str
    ):

        # Goes to order details page in the OpenCart dashboard,
        # get the order properties and binds in the instance
        order_url = (
            config.OPENCART_ORDER_URL +
            f"&user_token={user_token}&order_id={order_id}"
        )
        driver.get(order_url)
        config.sleep()

        # Scraping firstname, lastname and set fullname
        self.firstname = driver.find_element(By.ID, "input-firstname")\
            .get_attribute("value")
        self.lastname = driver.find_element(By.ID, "input-lastname")\
            .get_attribute("value")
        self.set_fullname()

        # Scraping email
        email_input = driver.find_element(By.ID, "input-email")\
            .get_attribute("value")
        self.set_email(email_input)

        # Scraping raw telephone, extracting ddd and phone with no 9 from it
        raw_telephone = driver.find_element(By.ID, "input-telephone")\
            .get_attribute("value")
        self.set_ddd_and_telephones(raw_telephone)

        # Advances in order tabs to get other informations
        buttons = ["button-customer", "button-cart", "button-payment-address"]
        for button in buttons:
            next_button = driver.find_element(By.ID, button)
            next_button.click()
            config.sleep()

        # Scraping address data
        address_input = driver\
            .find_element(By.ID, "input-shipping-address-1")\
            .get_attribute("value")
        self.set_address(address_input)
        number_input = driver\
            .find_element(By.ID, "input-shipping-custom-field5")\
            .get_attribute("value")
        self.set_number(number_input)
        complement_input = driver\
            .find_element(By.ID, "input-shipping-custom-field4")\
            .get_attribute("value")
        self.set_complement(complement_input)
        neighborhood_input = driver\
            .find_element(By.ID, "input-shipping-address-2")\
            .get_attribute("value")
        self.set_neighborhood(neighborhood_input)
        postcode_input = driver\
            .find_element(By.ID, "input-shipping-postcode")\
            .get_attribute("value")
        self.set_postcode(postcode_input)
        city_input = driver\
            .find_element(By.ID, "input-shipping-city")\
            .get_attribute("value")
        self.set_city(city_input)

    def set_fullname(self) -> None:
        if self.firstname is None:
            self.firstname = ""
        if self.lastname is None:
            self.lastname = ""
        self.fullname = self.firstname.strip() + " " + self.lastname.strip()

    def set_email(self, email_input: str | None) -> None:
        if email_input is None:
            email_input = ""
        self.email = email_input.strip()

    def set_ddd_and_telephones(self, raw_telephone: str | None) -> None:
        if raw_telephone is None:
            raw_telephone = ""
        telephone = raw_telephone.strip()\
            .replace("(", "")\
            .replace(")", "")\
            .replace("-", "")\
            .replace(" ", "")
        self.ddd = telephone[:2]
        self.telephone = telephone[2:]
        self.telephone_without_9 = self.telephone[1:]

    def set_address(self, address_input: str | None) -> None:
        if address_input is None:
            address_input = ""
        self.address = address_input.strip()

    def set_number(self, number_input: str | None) -> None:
        if number_input is None:
            number_input = ""
        self.number = number_input.strip()

    def set_complement(self, complement_input: str | None) -> None:
        if complement_input is None:
            complement_input = ""
        self.complement = complement_input.strip()

    def set_neighborhood(self, neighborhood_input: str | None) -> None:
        if neighborhood_input is None:
            neighborhood_input = ""
        self.neighborhood = neighborhood_input.strip()

    def set_postcode(self, postcode_input: str | None) -> None:
        if postcode_input is None:
            postcode_input = ""
        self.postcode = postcode_input.strip().replace("-", "")

    def set_city(self, city_input: str | None) -> None:
        if city_input is None:
            city_input = ""
        self.city = city_input.strip()

    def __str__(self) -> str:
        parts = []

        # Fullname and email
        if self.firstname or self.lastname:
            name_parts = []
            if self.firstname:
                name_parts.append(self.firstname)
            if self.lastname:
                name_parts.append(self.lastname)
            parts.append(f"Nome: {' '.join(name_parts)}")
        parts.append(f"Email: {self.email}")

        # Address
        address_parts = []
        if self.address:
            address_parts.append(self.address)
        if self.number:
            address_parts.append(f"nº {self.number}")
        if self.complement:
            address_parts.append(f"{self.complement}")
        if address_parts:
            parts.append(f"Endereço: {', '.join(address_parts)}")
        if self.postcode:
            parts.append(f"CEP: {self.postcode}")

        # Telephones
        if self.ddd and self.telephone:
            phone = f"({self.ddd}) {self.telephone}"
            if self.telephone_without_9 and self.telephone_without_9\
                    != self.telephone:
                phone += f" (sem 9: {self.telephone_without_9})"
            parts.append(f"Telefone: {phone}")

        return "\n".join(parts)
