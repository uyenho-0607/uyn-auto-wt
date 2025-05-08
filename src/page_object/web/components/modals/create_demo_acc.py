from selenium.webdriver.common.by import By

from src.data.enums import CountryDialCode, DepositAmount
from src.page_object.web.base_page import BasePage
from src.core.actions.web_actions import WebActions
from src.data.element_ids import ElementIDs
from src.utils import enum_utils, common_utils
from src.utils.common_utils import cook_element


class CreateDemoAccountModal(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __txt_name = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Modals.DEMO_ACCOUNT_NAME}']")
    __txt_email = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Modals.DEMO_ACCOUNT_EMAIL}']")
    __drp_country_dial_code = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.COUNTRY_DIAL_CODE}']")
    __item_country_dial_code = (By.XPATH, "//div[@data-testid='country-dial-code-item' and contains(text(), '+{}')]")
    __txt_phone_number = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Modals.DEMO_ACCOUNT_PHONE}']")
    __deposit = (By.XPATH, "//div[text()='Deposit']")
    __item_deposit = (By.XPATH, "//div[@data-testid='deposit-dropdown-item' and text()='{}']")
    __chb_agreement = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.DEMO_ACCOUNT_AGREEMENT}'] div")
    __btn_next = (By.CSS_SELECTOR, f"button[data-testid='{ElementIDs.Modals.DEMO_ACCOUNT_CONFIRM}']")
    __field_validation = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.INPUT_FIELD_VALIDATION}']")

    # ------------------------ ACTIONS ------------------------ #
    def input_name(self, name: str):
        self.actions.send_keys(self.__txt_name, name)

    def input_email(self, email: str):
        self.actions.send_keys(self.__txt_email, email)

    def input_phone_number(self, country_code: CountryDialCode = None, phone_number: str = None):
        country_code = country_code or enum_utils.random_value(CountryDialCode)
        phone_number = phone_number or common_utils.generate_phone_number(country_code)
        self.actions.click(self.__drp_country_dial_code)
        self.actions.click(cook_element(self.__item_country_dial_code, country_code))
        self.actions.send_keys(self.__txt_phone_number, phone_number)

    def input_deposit(self, deposit: DepositAmount = None):
        deposit = deposit or common_utils.format_number_with_commas(enum_utils.random_value(DepositAmount))
        self.actions.click_by_offset(self.__deposit, x_offset=50, y_offset=20)
        self.actions.click(cook_element(self.__item_deposit, deposit))

    def click_agreement(self):
        self.actions.click(self.__chb_agreement)

    def click_next_button(self):
        self.actions.click(self.__btn_next)

    # ------------------------ VERIFY ------------------------ #
