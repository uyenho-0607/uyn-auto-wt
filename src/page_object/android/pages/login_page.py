from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.data.enums import AccountType, Language
from src.page_object.android.base_page import BasePage
from src.page_object.android.components.modals.demo_account import DemoAccountModal
from src.page_object.android.components.modals.password import PasswordModal
from src.utils.assert_utils import soft_assert
from src.utils.common_utils import cook_element, translate_sign_in
from src.utils.logging_utils import logger


class LoginPage(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)
        self.demo_account_modal = DemoAccountModal(actions)
        self.password_modal = PasswordModal(actions)

    # ------------------------ LOCATORS ------------------------ #
    __tab_account_type = (AppiumBy.XPATH, "//*[@resource-id='tab-login-account-type-{}']")
    __drp_language = (AppiumBy.XPATH, "//*[@resource-id='language-dropdown']")
    __opt_language = (AppiumBy.XPATH, "//*[@resource-id='language-option' and contains(@content-desc, '{}')]")
    __txt_user_id = (AppiumBy.XPATH, "//*[@resource-id='login-user-id']")
    __txt_password = (AppiumBy.XPATH, "//*[@resource-id='login-password']")
    __btn_sign_in = (AppiumBy.XPATH, "//*[@resource-id='login-submit']")
    __lnk_reset_password = (AppiumBy.XPATH, "//*[@resource-id='reset-password-link']")
    __btn_sign_up = (AppiumBy.XPATH, "//*[@resource-id='login-account-signup']")
    __alert_error = (AppiumBy.XPATH, "//*[@resource-id='alert-error']")
    __btn_skip = (AppiumBy.XPATH, "//*[resource-id='ads-skip-button']")

    # ------------------------ ACTIONS ------------------------ #
    def select_account_tab(self, account_type: AccountType):
        self.actions.click(cook_element(self.__tab_account_type, account_type))

    def select_language(self, language: Language):
        self.actions.click(self.__drp_language)
        self.actions.click(cook_element(self.__opt_language, language))

    def click_sign_in(self):
        self.actions.click(self.__btn_sign_in)

    def click_forgot_password(self):
        self.actions.click(self.__lnk_reset_password)

    def login(self, userid, password, account_type: AccountType, language: Language = None):

        while self.actions.is_element_displayed(self.__btn_skip, timeout=15):
            self.actions.click(self.__btn_skip)

        if language:
            self.select_language(language)

        self.select_account_tab(account_type)
        self.actions.send_keys(self.__txt_user_id, str(userid))
        self.actions.send_keys(self.__txt_password, str(password))
        self.actions.click(self.__btn_sign_in)

    def select_open_demo_account(self):
        self.select_account_tab(AccountType.DEMO)
        self.actions.click(self.__btn_sign_up)

    # ------------------------ VERIFY ------------------------ #
    def verify_language(self, language: Language):
        actual = self.actions.get_text(self.__btn_sign_in)
        soft_assert(actual, translate_sign_in(language))

    def verify_account_tab_is_displayed(self):
        acc_tab_demo = cook_element(self.__tab_account_type, AccountType.DEMO)
        self.actions.verify_element_is_displayed(acc_tab_demo)

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

    def verify_alert_error_message(self, expected_message):
        actual_err = self.actions.get_text(self.__alert_error)
        soft_assert(actual_err, expected_message, "Error message validation failed!")
