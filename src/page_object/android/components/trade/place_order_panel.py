from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage


class PlaceOrderPanel(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    # Order Type
    __drp_order_type = (AppiumBy.XPATH, "//*[@resource-id='order-type-dropdown']")
    __opt_order_type = (AppiumBy.XPATH, "//*[@resource-id='order-type-option' and @text='{}']")
    
    # Order Details
    __txt_amount = (AppiumBy.XPATH, "//*[@resource-id='order-amount-input']")
    __txt_price = (AppiumBy.XPATH, "//*[@resource-id='order-price-input']")
    __txt_stop_loss = (AppiumBy.XPATH, "//*[@resource-id='stop-loss-input']")
    __txt_take_profit = (AppiumBy.XPATH, "//*[@resource-id='take-profit-input']")
    
    # Buttons
    __btn_buy = (AppiumBy.XPATH, "//*[@resource-id='buy-button']")
    __btn_sell = (AppiumBy.XPATH, "//*[@resource-id='sell-button']")
    __btn_place_order = (AppiumBy.XPATH, "//*[@resource-id='place-order-button']")

    # ------------------------ ACTIONS ------------------------ #
    def select_order_type(self, order_type: str):
        """Select the order type.
        
        Args:
            order_type (str): The type of order to select (e.g. 'Market', 'Limit', etc.)
        """
        self.actions.click(self.__drp_order_type)
        self.actions.click((AppiumBy.XPATH, f"//*[@resource-id='order-type-option' and @text='{order_type}']"))

    def set_amount(self, amount: float):
        """Set the order amount.
        
        Args:
            amount (float): The amount to set
        """
        self.actions.send_keys(self.__txt_amount, str(amount))

    def set_price(self, price: float):
        """Set the order price.
        
        Args:
            price (float): The price to set
        """
        self.actions.send_keys(self.__txt_price, str(price))

    def set_stop_loss(self, price: float):
        """Set the stop loss price.
        
        Args:
            price (float): The stop loss price to set
        """
        self.actions.send_keys(self.__txt_stop_loss, str(price))

    def set_take_profit(self, price: float):
        """Set the take profit price.
        
        Args:
            price (float): The take profit price to set
        """
        self.actions.send_keys(self.__txt_take_profit, str(price))

    def click_buy(self):
        """Click the buy button."""
        self.actions.click(self.__btn_buy)

    def click_sell(self):
        """Click the sell button."""
        self.actions.click(self.__btn_sell)

    def click_place_order(self):
        """Click the place order button."""
        self.actions.click(self.__btn_place_order)

    # ------------------------ VERIFY ------------------------ #
    def verify_panel_displayed(self):
        """Verify that the order panel is displayed."""
        self.actions.verify_element_is_displayed(self.__panel_container)

    def verify_amount_value(self, expected_amount: str):
        """Verify the amount field value.
        
        Args:
            expected_amount (str): The expected amount value
        """
        actual_amount = self.actions.get_attribute(self.__txt_amount, "text")
        assert actual_amount == str(expected_amount), f"Expected amount {expected_amount} but got {actual_amount}"

    def verify_price_value(self, expected_price: str):
        """Verify the price field value.
        
        Args:
            expected_price (str): The expected price value
        """
        actual_price = self.actions.get_attribute(self.__txt_price, "text")
        assert actual_price == str(expected_price), f"Expected price {expected_price} but got {actual_price}" 