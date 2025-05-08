from src.core.actions.web_actions import WebActions
from src.data.enums import Features
from src.data.element_ids import ElementIDs
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.setting import Setting
from selenium.webdriver.common.by import By

from src.utils.common_utils import cook_element


class Navigation(BasePage):
    """Manages all navigation elements including top bar and sidebar"""
    
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self._setting = Setting(actions)

    # ------------------------ LOCATORS ------------------------ #
    # Top Bar Elements
    __account_selector = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Navigation.ACCOUNT_SELECTOR}']")
    __account_name = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Navigation.ACCOUNT_NAME}']")
    __account_id = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Navigation.ACCOUNT_ID}']")

    # Side Bar Elements
    __side_bar_option = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Navigation.SIDE_BAR_OPTION}']")

    # ------------------------ ACTIONS ------------------------ #
    # Account Actions
    def get_account_info(self) -> dict:
        """Get current account information"""
        return {
            "name": self.actions.get_text(self.__account_name),
            "id": self.actions.get_text(self.__account_id)
        }

    # Navigation Actions
    def navigate_to(self, feature: Features):
        """Navigate to a specific feature using the sidebar"""
        self.actions.click(cook_element(self.__side_bar_option, feature.lower()))

    # ------------------------ VERIFY ------------------------ #
    def verify_account_info_displayed(self):
        """Verify that account information is displayed"""
        self.actions.verify_element_is_displayed(self.__account_selector)
        self.actions.verify_element_is_displayed(self.__account_name)
        self.actions.verify_element_is_displayed(self.__account_id)
