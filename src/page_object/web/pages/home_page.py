from selenium.webdriver.common.by import By
from src.core.actions.web_actions import WebActions
from src.data.enums import Features
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.feature_announcement import FeatureAnnouncementModal
from src.page_object.web.components.notifications import Notifications
from src.page_object.web.components.settings import Settings
from src.utils.common_utils import cook_element


class HomePage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.notifications = Notifications(actions)
        self.settings = Settings(actions)
        self.feature_announcement_modal = FeatureAnnouncementModal(actions)

    # ------------------------ LOCATORS ------------------------ #
    # Top Bar Elements
    __account_selector = (By.CSS_SELECTOR, "*[data-testid='account-selector']")
    __account_name = (By.CSS_SELECTOR, "*[data-testid='account-name']")
    __account_id = (By.CSS_SELECTOR, "*[data-testid='account-id']")
    __txt_symbol_search = (By.CSS_SELECTOR, "*[data-testid='symbol-input-search']")

    # Side Bar Elements
    __side_bar_option = (By.CSS_SELECTOR, "*[data-testid='side-bar-option-{}']")

    # ------------------------ ACTIONS ------------------------ #
    # Navigation Actions
    def navigate_to(self, feature: Features):
        """Navigate to a specific feature using the sidebar"""
        self.actions.click(cook_element(self.__side_bar_option, feature))

    # ------------------------ VERIFY ------------------------ #
    def verify_account_info_displayed(self):
        """Verify that account information is displayed"""
        self.actions.verify_element_is_displayed(self.__account_selector)
        self.actions.verify_element_is_displayed(self.__account_name)
        self.actions.verify_element_is_displayed(self.__account_id)
