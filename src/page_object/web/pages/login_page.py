from selenium.webdriver.common.by import By

from src.core.actions.web_actions import WebActions
from src.data.enums import AccountType, Language
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.demo_account import DemoAccountModal
from src.utils.assert_utils import soft_assert
from src.utils.common_utils import cook_element, translate_sign_in


class LoginPage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.demo_account_modal = DemoAccountModal(actions)

    # ------------------------ LOCATORS ------------------------ #
    __drp_language = (By.CSS_SELECTOR, "*[data-testid='language-dropdown']")
    __opt_language = (By.XPATH, "//li[@data-testid='language-option' and text()='{}']")
    __tab_account_type = (By.CSS_SELECTOR, "*[data-testid='tab-login-account-type-{}']")
    __txt_user_id = (By.CSS_SELECTOR, "input[data-testid='login-user-id']")
    __txt_password = (By.CSS_SELECTOR, "input[data-testid='login-password']")
    __btn_login = (By.CSS_SELECTOR, "button[data-testid='login-submit']")
    __forgot_password = (By.CSS_SELECTOR, "*[data-testid='reset-password-link']")
    __open_demo_account = (By.CSS_SELECTOR, "*[data-testid='login-account-signup']")

    # ------------------------ ACTIONS ------------------------ #

    def select_account_tab(self, account_type: AccountType):
        self.actions.click(cook_element(self.__tab_account_type, account_type))

    def select_language(self, language: Language):
        self.actions.click(self.__drp_language)
        self.actions.click(cook_element(self.__opt_language, language))

    def click_sign_in(self):
        self.actions.click(self.__btn_login)

    def click_forgot_password(self):
        self.actions.click(self.__forgot_password)

    def login(self, userid, password, account_type: AccountType, language: Language = None):
        if language:
            self.select_language(language)

        self.select_account_tab(account_type)
        self.actions.send_keys(self.__txt_user_id, str(userid))
        self.actions.send_keys(self.__txt_password, str(password))
        self.actions.click(self.__btn_login)

    def open_demo_account_creation(self):
        self.select_account_tab(AccountType.DEMO)
        self.actions.click(self.__open_demo_account)

    # ------------------------ VERIFY ------------------------ #
    def verify_language(self, language: Language):
        actual = self.actions.get_text(self.__btn_login)
        soft_assert(actual, translate_sign_in(language))

    def verify_account_tabs_is_displayed(self):
        acc_tab_demo = cook_element(self.__tab_account_type, AccountType.DEMO)
        acc_tab_live = cook_element(self.__tab_account_type, AccountType.LIVE)
        # Check account tab demo is displayed
        soft_assert(self.actions.is_element_displayed(acc_tab_demo), True)

        # Check account tab live is displayed
        soft_assert(self.actions.is_element_displayed(acc_tab_live), True)

    def verify_account_tab_is_selected(self, account_type: AccountType):
        # verify 'selected' in class attribute of account tab
        class_attr = self.actions.get_attribute(
            cook_element(self.__tab_account_type, account_type), "class"
        )
        soft_assert(
            "selected" in class_attr, True,
            f"Demo account is not selected, class attribute: {class_attr!r}"
        )

    def verify_account_autofill_value(self, userid, password):
        actual_userid = self.actions.get_attribute(self.__txt_user_id, "value")
        soft_assert(actual_userid, str(userid))

        actual_password = self.actions.get_attribute(self.__txt_password, "value")
        soft_assert(actual_password, password)
