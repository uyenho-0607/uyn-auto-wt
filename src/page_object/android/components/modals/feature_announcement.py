from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage


class FeatureAnnouncementModal(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __btn_got_it = (AppiumBy.XPATH, "//*[@resource-id='feature-announcement-modal-got-it-button']")
    __btn_try_now = (AppiumBy.XPATH, "//*[@resource-id='feature-announcement-modal-try-it-now-button']")

    # ------------------------ ACTIONS ------------------------ #
    def got_it(self):
        """Click the 'Got it' button to dismiss the feature announcement."""
        while self.actions.is_element_displayed(self.__btn_got_it):
            self.actions.click(self.__btn_got_it)

    def try_it_now(self):
        """Click the 'Try it now' button to try the new feature."""
        self.actions.click(self.__btn_try_now)

    # ------------------------ VERIFY ------------------------ #
    
