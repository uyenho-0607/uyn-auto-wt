from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.data.consts import EXPLICIT_WAIT
from src.core.config_manager import Config
from src.data.ui_messages import UIMessages
from src.utils.assert_utils import soft_assert


class BasePage:
    """Base class for all Android pages providing common functionality."""
    
    def __init__(self, actions: MobileActions):
        """Initialize the base page.
        
        Args:
            actions (MobileActions): The mobile actions instance for interacting with the page
        """
        self.actions = actions

    # ------------------------ LOCATORS ------------------------ #
    __alert_error = (AppiumBy.XPATH, "//*[@resource-id='alert-error']")
    __alert_success = (AppiumBy.XPATH, "//*[@resource-id='alert-success']")
    __btn_nav_back = (AppiumBy.XPATH, "//*[@resource-id='navigation-back-button']")

    # ------------------------ ACTIONS ------------------------ #
    def go_back(self):
        """Navigate back using the back button"""
        self.actions.click(self.__btn_nav_back)

    # ------------------------ VERIFY ------------------------ #
    def verify_alert_error_message(self, expected_message: UIMessages):
        """Verify the error alert message.
        
        Args:
            expected_message (UIMessages): The expected error message
        """
        actual_err = self.actions.get_text(self.__alert_error)
        soft_assert(actual_err, expected_message)

    def verify_alert_success_message(self, expected_message: UIMessages):
        """Verify the success alert message.
        
        Args:
            expected_message (UIMessages): The expected success message
        """
        actual_msg = self.actions.get_text(self.__alert_success)
        soft_assert(actual_msg, expected_message)
