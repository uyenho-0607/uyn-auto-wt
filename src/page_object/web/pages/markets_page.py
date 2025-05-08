from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.trade.watch_list import WatchList


class MarketsPage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.watch_list = WatchList(actions)

    # ------------------------ LOCATORS ------------------------ #

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
