from selenium.webdriver.common.by import By

from src.core.actions.web_actions import WebActions
from src.page_object.web.base_page import BasePage


class TradingModals(BasePage):
    def __init__(self, actions: WebActions):
        super().__init__(actions)

    # ======================== ONE CLICK TRADING ======================== #

    # ------------------------ LOCATORS ------------------------ #
    __btn_oct_confirm = (By.CSS_SELECTOR, "button[data-testid='oct-modal-button-confirm']")

    # ------------------------ ACTIONS ------------------------ #
    def agree_and_continue(self):
        self.actions.click(self.__btn_oct_confirm)

    # ------------------------ VERIFY ------------------------ #

    # ======================== TRADE CONFIRMATION ======================== #
    __btn_trade_confirm = (By.CSS_SELECTOR, "button[data-testid='trade-confirmation-button-confirm']")
    __trade_confirm_order_type = (By.CSS_SELECTOR, "*[data-testid='trade-confirmation-order-type']")  # note: get text, text is caplock
    __trade_confirm_symbol = (By.CSS_SELECTOR, "*[data-testid='trade-confirmation-symbol']")
    __trade_confirm_volume = (
        By.XPATH,
        "//div[@data-testid='trade-confirmation-label' and normalize-space(text())='Volume']/following-sibling::div"
    )
    __trade_confirm_price = (
        By.XPATH,
        "//div[@data-testid='trade-confirmation-label' and normalize-space(text())='Price']/following-sibling::div"
    )
    __trade_confirm_stop_loss = (
        By.XPATH,
        "//div[@data-testid='trade-confirmation-label' and normalize-space(text())='Stop Loss']/following-sibling::div"
    )
    __trade_confirm_take_profit = (
        By.XPATH,
        "//div[@data-testid='trade-confirmation-label' and normalize-space(text())='Take Profit']/following-sibling::div"
    )
    __trade_confirm_expiry = (
        By.XPATH,
        "//div[@data-testid='trade-confirmation-label' and normalize-space(text())='Expiry']/following-sibling::div"
    )
    __trade_confirm_fill_policy = (
        By.XPATH,
        "//div[@data-testid='trade-confirmation-label' and normalize-space(text())='Fill Policy']/following-sibling::div"
    )

