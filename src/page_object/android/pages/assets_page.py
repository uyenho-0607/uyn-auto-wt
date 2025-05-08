from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage
from src.page_object.web.components.modals.trading import TradingModals
from src.page_object.web.components.trade.asset_tab import AssetTab


class AssetsPage(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)
        self.asset_tab = AssetTab(actions)
        self.trading_modals = TradingModals(actions)

    # ------------------------ LOCATORS ------------------------ #

    # ------------------------ ACTIONS ------------------------ #

    # ------------------------ VERIFY ------------------------ #
