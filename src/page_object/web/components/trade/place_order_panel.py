from selenium.webdriver.common.by import By

from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage


class PlaceOrderPanel(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __toggle_oct = (By.CSS_SELECTOR, "*[data-testid='toggle-oct']")
    __toggle_oct_checked = (By.CSS_SELECTOR, "*[data-testid='toggle-oct-checked']")
    __btn_oct_confirm = (By.CSS_SELECTOR, "button[data-testid='oct-modal-button-confirm']")

    __tab_oct = (By.CSS_SELECTOR, "*[data-testid='tab-one-click-trading']")
    __tab_trade = (By.CSS_SELECTOR, "*[data-testid='tab-trade']")
    __tab_specification = (By.CSS_SELECTOR, "*[data-testid='tab-specification']")

    __txt_size = (By.CSS_SELECTOR, "input[data-testid='trade-input-volume']")
    __increase_size = (By.CSS_SELECTOR, "*[data-testid='trade-input-volume-increase']")
    __decrease_size = (By.CSS_SELECTOR, "*[data-testid='trade-input-volume-decrease']")
    __swap_units = (By.CSS_SELECTOR, "*[data-testid='trade-swap-to-units']")
    __btn_buy = (By.CSS_SELECTOR, "*[data-testid='trade-button-oct-order-buy']")
    __btn_sell = (By.CSS_SELECTOR, "*[data-testid='trade-button-oct-order-sell']")
    __drp_order_type = (By.CSS_SELECTOR, "*[data-testid='trade-dropdown-order-type']")
    __opt_order_type = (By.CSS_SELECTOR, "*[data-testid='trade-dropdown-order-type-{}']")
    __txt_stop_loss_price = (By.CSS_SELECTOR, "input[data-testid='trade-input-stoploss-price']")

    __txt_stop_loss_point = (By.CSS_SELECTOR, "*[data-testid='trade-input-stoploss-points']")
    __decrease_stop_loss = (By.CSS_SELECTOR, "*[data-testid='trade-input-stoploss-price-decrease']")
    __increase_stop_loss = (By.CSS_SELECTOR, "*[data-testid='trade-input-stoploss-price-increase']")
    __txt_take_profit = (By.CSS_SELECTOR, "*[data-testid='trade-input-takeprofit-price']")
    __decrease_take_profit = (By.CSS_SELECTOR, "*[data-testid='trade-input-takeprofit-price-decrease']")
    __increase_take_profit = (By.CSS_SELECTOR, "*[data-testid='trade-input-takeprofit-price-increase']")
    __btn_place_order = (By.CSS_SELECTOR, "*[data-testid='trade-button-order']")

    # order_type = limit/ stop
    __txt_price = (By.CSS_SELECTOR, "*[data-testid='trade-input-price']")
    __decrease_price = (By.CSS_SELECTOR, "*[data-testid='trade-input-price-decrease']")
    __increase_price = (By.CSS_SELECTOR, "*[data-testid='trade-input-price-increase']")
    __drp_expiry = (By.CSS_SELECTOR, "*[data-testid='trade-dropdown-expiry']")
    __opt_expiry = (By.CSS_SELECTOR, "*[data-testid='trade-dropdown-expiry-{}']")

    # MT5
    __drp_fill_policy = (By.CSS_SELECTOR, "*[data-testid='trade-dropdown-fill-policy']")
    __opt_fill_policy = (By.CSS_SELECTOR, "*[data-testid='trade-dropdown-fill-policy-{}']")

    # ------------------------ ACTIONS ------------------------ #
    def enable_oct(self):
        """
        Enable One-Click Trading by clicking the toggle if it's not already enabled
        """
        if self.actions.is_element_displayed(self.__toggle_oct, timeout=5):
            self.actions.click(self.__toggle_oct)
        self.actions.click(self.__btn_oct_confirm)

    def disable_oct(self):
        """
        Disable One-Click Trading by clicking the toggle if it's currently enabled
        """
        if self.actions.is_element_displayed(self.__toggle_oct_checked, timeout=5):
            self.actions.click(self.__toggle_oct_checked)
        self.actions.click(self.__btn_oct_confirm)

    # ------------------------ VERIFY ------------------------ #
