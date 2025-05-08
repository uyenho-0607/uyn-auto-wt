from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage
from src.page_object.android.components.modals.feature_announcement import FeatureAnnouncementModal
from src.page_object.android.components.settings import Settings

class HomePage(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)
        self.feature_anm_modal = FeatureAnnouncementModal(actions)
        self.settings = Settings(actions)

    # ------------------------ LOCATORS ------------------------ #
    # Top Navigation
    __account_selector = (AppiumBy.XPATH, "//*[@resource-id='account-selector']")
    __account_type_tag = (AppiumBy.XPATH, "//*[@resource-id='account-type-tag']")
    __available_balance_dropdown = (AppiumBy.XPATH, "//*[@resource-id='available-balance-dropdown']")
    __available_balance_title = (AppiumBy.XPATH, "//*[@resource-id='available-balance-title']")
    __symbol_search_selector = (AppiumBy.XPATH, "//*[@resource-id='symbol-search-selector']")
    __notification_selector = (AppiumBy.XPATH, "//*[@resource-id='notification-selector']")

    # Watchlist Tabs
    __tab_all = (AppiumBy.XPATH, "//*[@resource-id='tab-all']")
    __tab_my_watchlist = (AppiumBy.XPATH, "//*[@resource-id='tab-my-watchlist']")
    __tab_popular = (AppiumBy.XPATH, "//*[@resource-id='tab-popular']")
    __tab_top_gainer = (AppiumBy.XPATH, "//*[@resource-id='tab-top-gainer']")
    __tab_top_loser = (AppiumBy.XPATH, "//*[@resource-id='tab-top-loser']")

    # Watchlist Items
    __watchlist_list_item = (AppiumBy.XPATH, "//*[@resource-id='watchlist-list-item']")
    __symbol_market_close = (AppiumBy.XPATH, "//*[@resource-id='symbol-market-close']")
    __symbol_market_open = (AppiumBy.XPATH, "//*[@resource-id='symbol-market-open']")

    # Bottom Navigation
    __home_nav_option = (AppiumBy.XPATH, "//*[@resource-id='home-nav-option-signal']")
    __news_nav_option = (AppiumBy.XPATH, "//*[@resource-id='home-nav-option-news']")
    __calendar_nav_option = (AppiumBy.XPATH, "//*[@resource-id='home-nav-option-calendar']")
    __copy_trade_nav_option = (AppiumBy.XPATH, "//*[@resource-id='home-nav-option-copy-trade']")

    # Banners
    __deposit_banner = (AppiumBy.XPATH, "//*[@resource-id='deposit-banner']")
    __start_account_banner = (AppiumBy.XPATH, "//*[@resource-id='start-account-banner']")

    # ------------------------ ACTIONS ------------------------ #

    def search_symbol(self, symbol):
        self.actions.click(self.__symbol_search_selector)

    def open_notifications(self):
        self.actions.click(self.__notification_selector)






    # ------------------------ VERIFY ------------------------ #
    def verify_account_info_displayed(self):
        """Verify that account information is displayed"""
        self.actions.verify_element_is_displayed(self.__account_selector)
