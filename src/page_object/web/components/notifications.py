from selenium.webdriver.common.by import By

from src.page_object.web.base_page import BasePage


class Notifications(BasePage):
    def __init__(self, actions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __notification_selector = (By.CSS_SELECTOR, "*[data-testid='notification-selector']")
    __notification_des = (By.CSS_SELECTOR, "*[data-testid='notification-description']")
    __notification_title = (By.CSS_SELECTOR, "*[data-testid='notification-title']")
    __btn_close = (By.CSS_SELECTOR, "*[data-testid='notification-close-button']")

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
