from selenium.webdriver.common.by import By
from src.page_object.web.base_page import BasePage
from src.core.actions.web_actions import WebActions
from src.data.element_ids import ElementIDs


class ChangePasswordModal(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __txt_old_password = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Modals.CHANGE_PASSWORD_OLD}']")
    __txt_new_password = (By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Modals.CHANGE_PASSWORD_NEW}']")
    __txt_confirm_new_password = (
        By.CSS_SELECTOR, f"input[data-testid='{ElementIDs.Modals.CHANGE_PASSWORD_CONFIRM}']"
    )
    __btn_submit = (By.CSS_SELECTOR, f"button[data-testid='{ElementIDs.Modals.CHANGE_PASSWORD_SUBMIT}']")

    # ------------------------ ACTIONS ------------------------ #
    def change_password(self, old_password, new_password):
        """
        Changes the user's password using the change password modal.
        Args:
            old_password (str): Current password
            new_password (str): New password to set
        """
        self.actions.send_keys(self.__txt_old_password, old_password)
        self.actions.send_keys(self.__txt_new_password, new_password)
        self.actions.send_keys(self.__txt_confirm_new_password, new_password)
        self.actions.click(self.__btn_submit)

    # ------------------------ VERIFY ------------------------ #
    
