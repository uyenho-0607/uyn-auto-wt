from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from src.data.enums import AccountType, Language
from src.data.element_ids import ElementIDs
from src.page_object.android.components.modals import Modals
from src.utils.common_utils import cook_element


class LoginPage(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)
        self.open_demo_account_modal = Modals(actions)

    # ------------------------ LOCATORS ------------------------ #
    __tab_account_type = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.ACCOUNT_TYPE}']")
    __drp_language = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.LANGUAGE_DROPDOWN}']")
    __txt_user_id = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.USER_ID}']")
    __txt_password = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.PASSWORD}']")
    __btn_sign_in = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.SUBMIT}']")
    __lnk_reset_password = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.RESET_PASSWORD}']")
    __btn_sign_up = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Login.ACCOUNT_SIGNUP}']")
    __opt_language = (AppiumBy.ACCESSIBILITY_ID, "{}")

    # ------------------------ ACTIONS ------------------------ #
    def select_language(self, language: Language):
        self.actions.click(self.__drp_language)
        self.actions.click(cook_element(self.__opt_language, language))

    def login(self, userid, password, account_type: AccountType, language: Language = None):
        if language:
            self.select_language(language)

        self.actions.click(cook_element(self.__tab_account_type, account_type.lower()))
        self.actions.send_keys(self.__txt_user_id, str(userid))
        self.actions.send_keys(self.__txt_password, str(password))
        self.actions.click(self.__btn_sign_in)

    def select_open_demo_account(self):
        self.actions.click(cook_element(self.__tab_account_type, AccountType.DEMO))
        self.actions.click(self.__btn_sign_up)

    # ------------------------ VERIFY ------------------------ #
