from src.core.actions.web_actions import WebActions
from src.core.config_manager import Config
from selenium.webdriver.common.by import By

from src.data.ui_messages import UIMessages
from src.data.element_ids import ElementIDs
from src.utils.assert_utils import soft_assert


class BasePage:
    def __init__(self, actions: WebActions):
        self.actions = actions

    # ------------------------ LOCATORS ------------------------ #
    __alert_error = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Base.ALERT_ERROR}']")
    __alert_success = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Base.ALERT_SUCCESS}']")

    # ------------------------ ACTIONS ------------------------ #
    # ------------------------ VERIFY ------------------------ #
    def verify_page_url(self, url_path: str):
        """Verify that the current URL matches the expected page URL"""
        self.actions.verify_url(Config.get_url_path(url_path))

    def verify_alert_message(self, expected_error: UIMessages):
        """Verify that the alert message is displayed with correct text"""
        actual_err = self.actions.get_text(self.__alert_error)
        soft_assert(actual_err, expected_error)
