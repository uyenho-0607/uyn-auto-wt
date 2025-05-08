from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from src.data.enums import SettingOpt
from src.data.element_ids import ElementIDs


class SettingPage(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __btn_account_selector = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Navigation.ACCOUNT_SELECTOR}']")
    __txt_account_name = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Navigation.ACCOUNT_NAME}']")
    __txt_account_id = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Navigation.ACCOUNT_ID}']")
    __txt_account_detail = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Navigation.ACCOUNT_DETAIL}']")
    
    # Account Settings
    __opt_setting = (AppiumBy.XPATH, f"//*[@resource-id='{ElementIDs.Setting.SETTING_OPTION}']")
    __switch_one_click_trading = (AppiumBy.XPATH, "//*[@resource-id='setting-option-oct']//android.widget.Switch")

    # Support & About
    __btn_help_support = (AppiumBy.XPATH, "//*[@resource-id='setting-option-help-support']")
    __btn_about = (AppiumBy.XPATH, "//*[@resource-id='setting-option-about']")
    
    # Logout
    __btn_logout = (AppiumBy.XPATH, "//*[@resource-id='account-logout']")

    # ------------------------ ACTIONS ------------------------ #

    def toggle_one_click_trading(self):
        self.actions.click(self.__switch_one_click_trading)

    # def open_help_support(self):
    #     self.actions.click(self.__btn_help_support)
    #
    # def open_about(self):
    #     self.actions.click(self.__btn_about)

    def logout(self):
        self.actions.click(self.__btn_logout)

    # ------------------------ VERIFY ------------------------ #
