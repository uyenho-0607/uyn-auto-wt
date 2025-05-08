from selenium.webdriver.common.by import By

from src.core.actions.web_actions import WebActions
from src.core.config_manager import Config
from src.data.enums import SettingOpt, Language, URLPaths
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.password import PasswordModal
from src.utils.common_utils import cook_element


class Settings(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.__change_password_modal = PasswordModal(actions)

    # ------------------------ LOCATORS ------------------------ #
    __btn_setting = (By.CSS_SELECTOR, "*[data-testid='setting-button']")
    __opt_setting = (By.CSS_SELECTOR, "*[data-testid='setting-option-{}']")
    __opt_language = (By.XPATH, "//div[@data-testid='setting-option-language']//li[text()='{}']")

    # ------------------------ ACTIONS ------------------------ #
    def __open_setting(self):
        self.actions.click(self.__btn_setting)

    def switch_to_live_account(self):
        self.__open_setting()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.SWITCH_TO_LIVE))

    def change_language(self, language: Language):
        self.__open_setting()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.CHANGE_LANGUAGE))
        self.actions.click(cook_element(self.__opt_language, language))

    def change_password(self, old_password, new_password):
        self.__open_setting()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.CHANGE_PASSWORD))
        self.__change_password_modal.change_password(old_password, new_password)

    def logout(self):
        self.__open_setting()
        self.actions.click(cook_element(self.__opt_setting, SettingOpt.LOG_OUT))
        self.actions.wait_for_url(Config.get_url_path(URLPaths.LOGIN))

    # ------------------------ VERIFY ------------------------ #
