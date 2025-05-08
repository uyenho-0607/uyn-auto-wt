from src.core.actions.web_actions import WebActions
from selenium.webdriver.common.by import By
from src.data.element_ids import ElementIDs

from src.page_object.web.base_page import BasePage
from src.utils.common_utils import cook_element


class Modals(BasePage):
    """
    This class contains all modal-related components and actions.
    Each modal section is clearly separated with comments and contains its own locators and actions.
    """
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ======================== DEMO ACCOUNT CREATION MODAL ======================== #
    # Locators

    # ======================== DEMO ACCOUNT COMPLETION MODAL ======================== #
    # Locators
    __demo_acc_completion_title = (By.CSS_SELECTOR, f"span[data-testid='{ElementIDs.Modals.DEMO_COMPLETION_TITLE}']")
    __demo_acc_userid = (By.XPATH, f"(//span[@data-testid='{ElementIDs.Modals.DEMO_COMPLETION_VALUE}'])[1]")
    __demo_acc_password = (By.CSS_SELECTOR, f"(//span[@data-testid='{ElementIDs.Modals.DEMO_COMPLETION_VALUE}'])[2]")
    __demo_acc_name = (By.CSS_SELECTOR, f"(//span[@data-testid='{ElementIDs.Modals.DEMO_COMPLETION_VALUE}'])[4]")
    __demo_acc_deposit = (By.CSS_SELECTOR, f"(//span[@data-testid='{ElementIDs.Modals.DEMO_COMPLETION_VALUE}'])[6]")
    __btn_sign_in_demo_acc_completion = (
        By.CSS_SELECTOR, f"button[data-testid='{ElementIDs.Modals.DEMO_COMPLETION_SIGN_IN}']"
    )

    # Actions
    def get_demo_account_details(self):
        """
        Gets the demo account details from the completion modal.
        
        Returns:
            dict: Dictionary containing userid, password, name, and deposit
        """
        return {
            'userid': self.actions.get_text(self.__demo_acc_userid),
            'password': self.actions.get_text(self.__demo_acc_password),
            'name': self.actions.get_text(self.__demo_acc_name),
            'deposit': self.actions.get_text(self.__demo_acc_deposit)
        }

    def sign_in_from_completion(self):
        """Clicks the sign-in button on the demo account completion modal."""
        self.actions.click(self.__btn_sign_in_demo_acc_completion)

    # ======================== FEATURE ANNOUNCEMENT MODAL ======================== #
    # Locators
    __btn_got_it_feature_ann = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.FEATURE_ANNOUNCEMENT_GOT_IT}']")
    __btn_try_it_now_feature_ann = (
        By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.FEATURE_ANNOUNCEMENT_TRY_NOW}']"
    )

    # Actions
    def got_it(self):
        """
        Clicks the 'Got it' button on the feature announcement modal.
        Will continue clicking if multiple announcements are present.
        """
        while self.actions.is_element_displayed(self.__btn_got_it_feature_ann):
            self.actions.click(self.__btn_got_it_feature_ann)

    def try_it_now(self):
        """Clicks the 'Try it now' button on the feature announcement modal."""
        self.actions.click(self.__btn_try_it_now_feature_ann)

    # ======================== CHANGE PASSWORD MODAL ======================== #

    # ======================== ONE CLICK TRADING MODAL ======================== #
    # Locators
    __btn_oct_confirm = (By.CSS_SELECTOR, "button[data-testid='oct-modal-button-confirm']")

    # Actions
    def agree_and_continue(self):
        self.actions.click(self.__btn_oct_confirm)


