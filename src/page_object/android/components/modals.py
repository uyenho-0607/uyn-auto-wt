from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from src.data.element_ids import ElementIDs

from src.utils.common_utils import cook_element


class Modals(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    # demo-account-creation-modal
    __demo_account_name = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.DEMO_ACCOUNT_NAME}']")
    __demo_account_email = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.DEMO_ACCOUNT_EMAIL}']")
    __demo_account_phone = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.DEMO_ACCOUNT_PHONE}']")
    __demo_account_dial_code = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.COUNTRY_DIAL_CODE_DROPDOWN}']")
    __demo_account_deposit = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.DEMO_ACCOUNT_DEPOSIT}']")
    __demo_account_confirm = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.DEMO_ACCOUNT_CONFIRM}']")
    __country_dial_code_item = (
        AppiumBy.XPATH,
        f"//*[@resource-id='{ElementIDs.Modals.COUNTRY_DIAL_CODE_ITEM}' and contains(@content-desc, '{{}}')]"
    )
    # feature-announcement-modal
    __btn_got_it = (AppiumBy.ACCESSIBILITY_ID, "Got it")

    # change-password-modal:
    __txt_old_password = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.CHANGE_PASSWORD_OLD}']")
    __txt_new_password = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.CHANGE_PASSWORD_NEW}']")
    __txt_confirm_new_password = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.CHANGE_PASSWORD_CONFIRM}']")
    __btn_submit = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Modals.CHANGE_PASSWORD_SUBMIT}']")

    # ------------------------ ACTIONS ------------------------ #
    # demo-account-creation-modal
    def fill_demo_account_form(self, name: str, email: str, phone: str):
        """Fill out the demo account creation form with provided information"""
        self.actions.send_keys(self.__demo_account_name, name)
        self.actions.send_keys(self.__demo_account_email, email)
        self.actions.send_keys(self.__demo_account_phone, phone)

    def select_dial_code(self):
        """Click on the dial code selector"""
        self.actions.click(self.__demo_account_dial_code)

    def select_country_dial_code(self, country_name: str):
        """Select a country dial code by country name
        Args:
            country_name (str): Name of the country (e.g. "Afghanistan (+93)")
        """
        self.actions.click(cook_element(self.__country_dial_code_item, country_name))

    def select_deposit(self):
        """Click on the deposit selector"""
        self.actions.click(self.__demo_account_deposit)

    def confirm_demo_account(self):
        """Click the confirm button to create demo account"""
        self.actions.click(self.__demo_account_confirm)

    # feature-announcement-modal
    def got_it(self):
        while self.actions.is_element_displayed(self.__btn_got_it):
            self.actions.click(self.__btn_got_it)

    # ------------------------ VERIFY ------------------------ #
