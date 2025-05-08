from selenium.webdriver.common.by import By

from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage


class WatchList(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #

    # watch list items
    __tab_all = (By.CSS_SELECTOR, "*[data-testid='tab-all']")
    __tab_favourites = (By.CSS_SELECTOR, "*[data-testid='tab-my-watchlist']")
    __tab_top_picks = (By.CSS_SELECTOR, "*[data-testid='tab-popular']")
    __tab_top_gainer = (By.CSS_SELECTOR, "*[data-testid='tab-top-gainer']")
    __tab_top_loser = (By.CSS_SELECTOR, "*[data-testid='tab-top-loser']")

    __item_by_name = (By.XPATH, "//div[@data-testid='watchlist-symbol' and text()='{}']")
    __trading_items = (
        By.XPATH, "//div[@data-testid='watchlist-list-item']//div[@data-testid='chart-symbol-status-trading']"
    )
    __closed_items = (
        By.XPATH, "//div[@data-testid='watchlist-list-item']//div[@data-testid='chart-symbol-status-closed']"
    )
    __unstar_icon = (
        By.XPATH,
        "//div[text()='{}']/ancestor::div[@data-testid='watchlist-list-item']"
        "//div[@data-testid='watchlist-star-unwatch']"
    )
    __star_icon = (
        By.XPATH,
        "//div[text()='{}']/ancestor::div[@data-testid='watchlist-list-item']"
        "//div[@data-testid='watchlist-star-watch']"
    )

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
