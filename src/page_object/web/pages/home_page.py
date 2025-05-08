from src.page_object.web.components.modals.feature_announcement import FeatureAnnouncementModal
from src.page_object.web.components.navigation import Navigation
from src.page_object.web.components.setting import Setting
from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.navigation = Navigation(actions)
        self.setting = Setting(actions)
        self.feature_announcement_modal = FeatureAnnouncementModal(actions)

    # ------------------------ LOCATORS ------------------------ #

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #

    def verify_login_successful(self):
        """Verify successful login by checking trade page URL and account info"""
        self.navigation.verify_account_info_displayed()
