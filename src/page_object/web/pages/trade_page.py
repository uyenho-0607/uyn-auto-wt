from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.trading import TradingModals
from src.page_object.web.components.trade.asset_tab import AssetTab
from src.page_object.web.components.trade.chart import Chart
from src.page_object.web.components.trade.place_order_panel import PlaceOrderPanel
from src.page_object.web.components.trade.watch_list import WatchList


class TradePage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.watch_list = WatchList(actions)
        self.asset_tab = AssetTab(actions)
        self.place_order_panel = PlaceOrderPanel(actions)
        self.chart = Chart(actions)
        self.trading_modals = TradingModals(actions)

    # ------------------------ LOCATORS ------------------------ #

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
