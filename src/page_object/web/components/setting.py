from src.core.actions.web_actions import WebActions
from src.core.config_manager import Config
from src.data.enums import SettingOpt, Language, URLPaths
from src.data.element_ids import ElementIDs
from src.page_object.web.base_page import BasePage
from selenium.webdriver.common.by import By
from src.utils.common_utils import cook_element
from src.page_object.web.components.modals.change_password import ChangePasswordModal


class Setting(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.__change_password_modal = ChangePasswordModal(actions)

    # ------------------------ LOCATORS ------------------------ #
    __btn_setting = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Setting.SETTING_BUTTON}']")
    __opt_setting = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Setting.SETTING_OPTION}']")
    __opt_language = (By.XPATH, f"//div[@data-testid='{ElementIDs.Setting.SETTING_LANGUAGE}']//li[text()='{{}}']")

    # ------------------------ ACTIONS ------------------------ #
    def __open_panel(self):
        self.actions.click(self.__btn_setting)

    def switch_to_live_account(self):
        self.__open_panel()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.SWITCH_TO_LIVE))

    def change_language(self, language: Language):
        """Change the site language"""
        self.__open_panel()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.CHANGE_LANGUAGE))
        self.actions.click(cook_element(self.__opt_language, language))

    def change_password(self, old_password, new_password):
        """Change the site password"""
        self.__open_panel()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.CHANGE_PASSWORD))
        self.__change_password_modal.change_password(old_password, new_password)

    def logout(self):
        self.__open_panel()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.LOG_OUT))
        self.actions.wait_for_url(Config.get_url_path(URLPaths.LOGIN))

    # ------------------------ VERIFY ------------------------ #
