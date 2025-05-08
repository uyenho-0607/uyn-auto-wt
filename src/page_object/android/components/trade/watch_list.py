from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage


class WatchList(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __tab_all = (AppiumBy.XPATH, "//*[@resource-id='watchlist-tab-all']")
    __tab_favorites = (AppiumBy.XPATH, "//*[@resource-id='watchlist-tab-favorites']")
    __tab_popular = (AppiumBy.XPATH, "//*[@resource-id='watchlist-tab-popular']")
    __tab_gainers = (AppiumBy.XPATH, "//*[@resource-id='watchlist-tab-gainers']")
    __tab_losers = (AppiumBy.XPATH, "//*[@resource-id='watchlist-tab-losers']")

    # ------------------------ ACTIONS ------------------------ #
    # ------------------------ VERIFY ------------------------ #
