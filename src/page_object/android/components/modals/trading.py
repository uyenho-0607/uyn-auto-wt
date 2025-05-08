from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage
from src.utils.assert_utils import soft_assert


class TradingModals(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ======================== ONE CLICK TRADING ======================== #

    # ------------------------ LOCATORS ------------------------ #
    __btn_oct_confirm = (AppiumBy.XPATH, "//*[@resource-id='oct-modal-button-confirm']")

    # ------------------------ ACTIONS ------------------------ #
    def agree_and_continue(self):
        self.actions.click(self.__btn_oct_confirm)

    # ------------------------ VERIFY ------------------------ #

    # ======================== TRADE CONFIRMATION ======================== #
    __btn_trade_confirm = (AppiumBy.XPATH, "//*[@resource-id='trade-confirmation-button-confirm']")
    __trade_confirm_order_type = (AppiumBy.XPATH, "//*[@resource-id='trade-confirmation-order-type']")  # note: get text, text is caplock
    __trade_confirm_symbol = (AppiumBy.XPATH, "//*[@resource-id='trade-confirmation-symbol']")
    __trade_confirm_volume = (
        AppiumBy.XPATH,
        "//div[@resource-id='trade-confirmation-label' and normalize-space(text())='Volume']/following-sibling::div"
    )
    __trade_confirm_price = (
        AppiumBy.XPATH,
        "//div[@resource-id='trade-confirmation-label' and normalize-space(text())='Price']/following-sibling::div"
    )
    __trade_confirm_stop_loss = (
        AppiumBy.XPATH,
        "//div[@resource-id='trade-confirmation-label' and normalize-space(text())='Stop Loss']/following-sibling::div"
    )
    __trade_confirm_take_profit = (
        AppiumBy.XPATH,
        "//div[@resource-id='trade-confirmation-label' and normalize-space(text())='Take Profit']/following-sibling::div"
    )
    __trade_confirm_expiry = (
        AppiumBy.XPATH,
        "//div[@resource-id='trade-confirmation-label' and normalize-space(text())='Expiry']/following-sibling::div"
    )
    __trade_confirm_fill_policy = (
        AppiumBy.XPATH,
        "//div[@resource-id='trade-confirmation-label' and normalize-space(text())='Fill Policy']/following-sibling::div"
    )

    # ------------------------ LOCATORS ------------------------ #
    # Order Confirmation Modal
    __order_confirmation_modal = (AppiumBy.XPATH, "//*[@resource-id='order-confirmation-modal']")
    __order_details = (AppiumBy.XPATH, "//*[@resource-id='order-details']")
    __btn_confirm_order = (AppiumBy.XPATH, "//*[@resource-id='confirm-order-button']")
    __btn_cancel_order = (AppiumBy.XPATH, "//*[@resource-id='cancel-order-button']")

    # Order Success Modal
    __order_success_modal = (AppiumBy.XPATH, "//*[@resource-id='order-success-modal']")
    __success_message = (AppiumBy.XPATH, "//*[@resource-id='success-message']")
    __btn_view_order = (AppiumBy.XPATH, "//*[@resource-id='view-order-button']")
    __btn_close_success = (AppiumBy.XPATH, "//*[@resource-id='close-success-button']")

    # Order Error Modal
    __order_error_modal = (AppiumBy.XPATH, "//*[@resource-id='order-error-modal']")
    __error_message = (AppiumBy.XPATH, "//*[@resource-id='error-message']")
    __btn_close_error = (AppiumBy.XPATH, "//*[@resource-id='close-error-button']")

    # ------------------------ ACTIONS ------------------------ #
    def confirm_order(self):
        """Confirm the order in the confirmation modal."""
        self.actions.click(self.__btn_confirm_order)

    def cancel_order(self):
        """Cancel the order in the confirmation modal."""
        self.actions.click(self.__btn_cancel_order)

    def view_order(self):
        """View the order details after successful placement."""
        self.actions.click(self.__btn_view_order)

    def close_success_modal(self):
        """Close the success modal."""
        self.actions.click(self.__btn_close_success)

    def close_error_modal(self):
        """Close the error modal."""
        self.actions.click(self.__btn_close_error)

    # ------------------------ VERIFY ------------------------ #
    def verify_confirmation_modal_displayed(self):
        """Verify that the order confirmation modal is displayed."""
        self.actions.verify_element_is_displayed(self.__order_confirmation_modal)
        self.actions.verify_element_is_displayed(self.__order_details)

    def verify_success_modal_displayed(self):
        """Verify that the order success modal is displayed."""
        self.actions.verify_element_is_displayed(self.__order_success_modal)
        self.actions.verify_element_is_displayed(self.__success_message)

    def verify_error_modal_displayed(self):
        """Verify that the order error modal is displayed."""
        self.actions.verify_element_is_displayed(self.__order_error_modal)
        self.actions.verify_element_is_displayed(self.__error_message)

    def verify_success_message(self, expected_message: str):
        """Verify the success message.
        
        Args:
            expected_message (str): The expected success message
        """
        actual_message = self.actions.get_text(self.__success_message)
        soft_assert(actual_message, expected_message)

    def verify_error_message(self, expected_message: str):
        """Verify the error message.
        
        Args:
            expected_message (str): The expected error message
        """
        actual_message = self.actions.get_text(self.__error_message)
        soft_assert(actual_message, expected_message)

