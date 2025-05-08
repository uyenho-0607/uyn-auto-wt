from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions


class BasePage:
    def __init__(self, actions: MobileActions):
        self.actions = actions

    # ------------------------ LOCATORS ------------------------ #
    __btn_nav_back = (AppiumBy.XPATH, "//*[@resource-id='navigation-back-button']")

    # ------------------------ ACTIONS ------------------------ #
    def go_back(self):
        self.actions.click(self.__btn_nav_back)

    # ------------------------ VERIFY ------------------------ #
