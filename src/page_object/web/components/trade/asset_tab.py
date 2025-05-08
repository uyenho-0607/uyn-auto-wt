from selenium.webdriver.common.by import By

from src.core.actions.web_actions import WebActions
from src.data.enums import AssetTabs
from src.page_object.web.base_page import BasePage
from src.utils.common_utils import cook_element


class AssetTab(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #

    __asset_tab = (By.CSS_SELECTOR, "*[data-testid='tab-asset-order_type-{}']")
    __bulk_close = "bulk-close"
    __drp_bulk_close_all = "dropdown-bulk-close-all"
    __drp_bulk_close_profit = "dropdown-bulk-close-profit"
    __drp_bulk_close_loss = "dropdown-bulk-close-loss"

    __preference = "column-preference"
    __sort_order = "order-sort-selector"
    __btn_track = "asset-open-button-track"
    __btn_close = "asset-open-button-close"
    __btn_edit = "asset-open-button-edit"

    # ------------------------ ACTIONS ------------------------ #
    def select_tab(self, tab: AssetTabs):
        self.actions.click(cook_element(self.__asset_tab, tab))

    # ------------------------ VERIFY ------------------------ #
