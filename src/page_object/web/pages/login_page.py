from selenium.webdriver.common.by import By
from src.core.actions.web_actions import WebActions
from src.data.enums import AccountType, Language, URLPaths
from src.data.element_ids import ElementIDs
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.create_demo_acc import CreateDemoAccountModal
from src.utils.assert_utils import soft_assert
from src.utils.common_utils import cook_element


class LoginPage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.open_demo_account_modal = CreateDemoAccountModal(actions)

    # ------------------------ LOCATORS ------------------------ #
    __txt_user_id = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Login.USER_ID}']")
    __txt_password = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Login.PASSWORD}']")
    __btn_login = (By.CSS_SELECTOR, f"button[data-testid='{ElementIDs.Login.SUBMIT}']")
    __open_demo_account = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Login.ACCOUNT_SIGNUP}']")
    __tab_account_type = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Login.ACCOUNT_TYPE}']")
    __drp_language = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Login.LANGUAGE_DROPDOWN}']")
    __opt_language = (By.XPATH, f"//li[@data-testid='{ElementIDs.Login.LANGUAGE_OPTION}' and text()='{{}}']")

    # ------------------------ ACTIONS ------------------------ #

    def __select_account_tab(self, account_type: AccountType):
        self.actions.click(cook_element(self.__tab_account_type, account_type.lower()))

    def __select_language(self, language: Language):
        self.actions.click(self.__drp_language)
        self.actions.click(cook_element(self.__opt_language, language))

    def login(self, userid, password, account_type: AccountType, language: Language = None):
        if language:
            self.__select_language(language)

        self.__select_account_tab(account_type)
        self.actions.send_keys(self.__txt_user_id, str(userid))
        self.actions.send_keys(self.__txt_password, str(password))
        self.actions.click(self.__btn_login)

    def open_demo_account_creation(self):
        self.__select_account_tab(AccountType.DEMO)
        self.actions.click(self.__open_demo_account)

    # ------------------------ VERIFY ------------------------ #
    def verify_login_account_tab_is_displayed(self):
        acc_tab_demo = cook_element(self.__tab_account_type, AccountType.DEMO.lower())
        acc_tab_live = cook_element(self.__tab_account_type, AccountType.LIVE.lower())
        # Check account tab demo is displayed
        soft_assert(self.actions.is_element_displayed(acc_tab_demo), True)

        # Check account tab live is displayed
        soft_assert(self.actions.is_element_displayed(acc_tab_live), True)

    def verify_demo_acc_creation_value(self, userid, password):
        actual_userid = self.actions.get_attribute(self.__txt_user_id, "value")
        soft_assert(actual_userid, str(userid))

        actual_password = self.actions.get_attribute(self.__txt_password, "value")
        soft_assert(actual_password, password)

