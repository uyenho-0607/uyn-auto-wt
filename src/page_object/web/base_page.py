from selenium.webdriver.common.by import By
from src.core.actions.web_actions import WebActions
from src.data.consts import EXPLICIT_WAIT
from src.core.config_manager import Config
from src.data.ui_messages import UIMessages
from src.utils.assert_utils import soft_assert


class BasePage:
    """Base class for all web pages providing common functionality."""
    
    def __init__(self, actions: WebActions):
        """Initialize the base page.
        
        Args:
            actions (WebActions): The web actions instance for interacting with the page
        """
        self.actions = actions

    # ------------------------ LOCATORS ------------------------ #
    __spin_loader = (By.CSS_SELECTOR, "*[data-testid='spin-loader']")
    __alert_error = (By.CSS_SELECTOR, "*[data-testid='alert-error']")
    __alert_success = (By.CSS_SELECTOR, "*[data-testid='alert-success']")

    # ------------------------ ACTIONS ------------------------ #
    def wait_for_loader(self, timeout: int = EXPLICIT_WAIT):
        """Wait for the loader to be invisible.
        
        Args:
            timeout (int): Maximum time to wait in seconds
        """
        self.actions.wait_for_element_invisible(self.__spin_loader, timeout=timeout)

    # ------------------------ VERIFY ------------------------ #
    def verify_page_url(self, url_path: str, timeout: int = EXPLICIT_WAIT):
        """Verify that the current URL matches the expected page URL.
        
        Args:
            url_path (str): The expected URL path
            timeout (int): Maximum time to wait in seconds
        """
        expected_url = Config.get_url_path(url_path)
        self.actions.verify_url(expected_url, timeout=timeout)

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
