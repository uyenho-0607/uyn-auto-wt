from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage
from src.utils.assert_utils import soft_assert


class NotificationBox(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __notification_box_des = (AppiumBy.XPATH, "//*[@resource-id='notification-box-description']")
    __btn_close = (AppiumBy.XPATH, "//*[@resource-id='notification-box-close']")

    # ------------------------ ACTIONS ------------------------ #
    def close_notification_box(self):
        self.actions.click(self.__btn_close)

    # ------------------------ VERIFY ------------------------ #
    def verify_notification_box_message(self, expected_message):
        actual_msg = self.actions.get_text(self.__notification_box_des)
        soft_assert(actual_msg, expected_message, "Alert error message validation failed!")
