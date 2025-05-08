from selenium.webdriver.common.by import By
from src.page_object.web.base_page import BasePage
from src.core.actions.web_actions import WebActions
from src.data.element_ids import ElementIDs


class FeatureAnnouncementModal(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __btn_got_it_feature_ann = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.FEATURE_ANNOUNCEMENT_GOT_IT}']")
    __btn_try_it_now_feature_ann = (
        By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Modals.FEATURE_ANNOUNCEMENT_TRY_NOW}']"
    )

    # ------------------------ ACTIONS ------------------------ #
    def got_it(self):
        """
        Clicks the 'Got it' button on the feature announcement modal.
        Will continue clicking if multiple announcements are present.
        """
        while self.actions.is_element_displayed(self.__btn_got_it_feature_ann, timeout=5):
            self.actions.click(self.__btn_got_it_feature_ann)

    def try_it_now(self):
        """Clicks the 'Try it now' button on the feature announcement modal."""
        self.actions.click(self.__btn_try_it_now_feature_ann)

    # ------------------------ VERIFY ------------------------ #
    
