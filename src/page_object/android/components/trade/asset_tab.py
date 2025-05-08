from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage


class AssetTab(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __tab_container = (AppiumBy.XPATH, "//*[@resource-id='asset-tab-container']")
    __tab_item = (AppiumBy.XPATH, "//*[@resource-id='asset-tab-item']")
    __tab_name = (AppiumBy.XPATH, "//*[@resource-id='asset-tab-name']")
    __tab_price = (AppiumBy.XPATH, "//*[@resource-id='asset-tab-price']")
    __tab_change = (AppiumBy.XPATH, "//*[@resource-id='asset-tab-change']")
    __tab_favorite = (AppiumBy.XPATH, "//*[@resource-id='asset-tab-favorite']")

    # ------------------------ ACTIONS ------------------------ #
    def select_asset(self, asset_name: str):
        """Select an asset from the tab.
        
        Args:
            asset_name (str): The name of the asset to select
        """
        asset_locator = (AppiumBy.XPATH, f"//*[@resource-id='asset-tab-name' and contains(@text, '{asset_name}')]")
        self.actions.click(asset_locator)

    def toggle_favorite(self, asset_name: str):
        """Toggle the favorite status of an asset.
        
        Args:
            asset_name (str): The name of the asset to toggle favorite status for
        """
        favorite_button = (AppiumBy.XPATH, 
            f"//*[@resource-id='asset-tab-name' and contains(@text, '{asset_name}')]"
            "/ancestor::*[@resource-id='asset-tab-item']//*[@resource-id='asset-tab-favorite']")
        self.actions.click(favorite_button)

    # ------------------------ VERIFY ------------------------ #
    def verify_tab_displayed(self):
        """Verify that the asset tab is displayed."""
        self.actions.verify_element_is_displayed(self.__tab_container)
        self.actions.verify_element_is_displayed(self.__tab_item)

    def verify_asset_in_tab(self, asset_name: str):
        """Verify that an asset is present in the tab.
        
        Args:
            asset_name (str): The name of the asset to verify
        """
        asset_locator = (AppiumBy.XPATH, f"//*[@resource-id='asset-tab-name' and contains(@text, '{asset_name}')]")
        self.actions.verify_element_is_displayed(asset_locator)

    def verify_asset_price(self, asset_name: str, expected_price: str):
        """Verify the price of an asset.
        
        Args:
            asset_name (str): The name of the asset to verify
            expected_price (str): The expected price
        """
        price_locator = (AppiumBy.XPATH, 
            f"//*[@resource-id='asset-tab-name' and contains(@text, '{asset_name}')]"
            "/ancestor::*[@resource-id='asset-tab-item']//*[@resource-id='asset-tab-price']")
        actual_price = self.actions.get_text(price_locator)
        assert actual_price == expected_price, f"Expected price {expected_price} but got {actual_price}" 