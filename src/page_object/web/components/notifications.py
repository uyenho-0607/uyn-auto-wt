from src.page_object.web.base_page import BasePage
from selenium.webdriver.common.by import By
from src.data.element_ids import ElementIDs


class Notifications(BasePage):
    def __init__(self, actions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __notification_selector = (By.CSS_SELECTOR, f"*[data-testid='{ElementIDs.Notifications.NOTIFICATION_SELECTOR}']")

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
