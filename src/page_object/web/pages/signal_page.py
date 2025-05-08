from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.trading import TradingModals
from src.page_object.web.components.trade.chart import Chart
from src.page_object.web.components.trade.place_order_panel import PlaceOrderPanel


class SignalPage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.chart = Chart(actions)
        self.place_order_panel = PlaceOrderPanel(actions)
        self.trading_modals = TradingModals(actions)

    # ------------------------ LOCATORS ------------------------ #

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
