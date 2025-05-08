from appium.webdriver.common.appiumby import AppiumBy

from src.core.actions.mobile_actions import MobileActions
from src.page_object.android.base_page import BasePage


class Chart(BasePage):
    def __init__(self, actions: MobileActions):
        super().__init__(actions)

    # ------------------------ LOCATORS ------------------------ #
    __chart_container = (AppiumBy.XPATH, "//*[@resource-id='chart-container']")
    __btn_zoom_in = (AppiumBy.XPATH, "//*[@resource-id='chart-zoom-in']")
    __btn_zoom_out = (AppiumBy.XPATH, "//*[@resource-id='chart-zoom-out']")
    __btn_reset_zoom = (AppiumBy.XPATH, "//*[@resource-id='chart-reset-zoom']")
    __btn_draw_tools = (AppiumBy.XPATH, "//*[@resource-id='chart-draw-tools']")

    # ------------------------ ACTIONS ------------------------ #
    def zoom_in(self):
        """Zoom in on the chart."""
        self.actions.click(self.__btn_zoom_in)

    def zoom_out(self):
        """Zoom out on the chart."""
        self.actions.click(self.__btn_zoom_out)

    def reset_zoom(self):
        """Reset the chart zoom level."""
        self.actions.click(self.__btn_reset_zoom)

    def open_draw_tools(self):
        """Open the chart drawing tools."""
        self.actions.click(self.__btn_draw_tools)

    # ------------------------ VERIFY ------------------------ #
    def verify_chart_displayed(self):
        """Verify that the chart is displayed."""
        self.actions.verify_element_is_displayed(self.__chart_container) 