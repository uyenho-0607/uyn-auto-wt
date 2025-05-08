from typing import Optional, Tuple, Union
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from src.core.actions.base_actions import BaseActions
from src.data.consts import EXPLICIT_WAIT


class MobileActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll(
            self, source_locator: tuple[str, str], target_locator: tuple[str, str],
            timeout=EXPLICIT_WAIT, retries=1, cond=BaseActions.DEFAULT_CONDITION,
            duration: Optional[int] = 500
    ):
        """Scroll from source element to target element.
        
        Args:
            source_locator: Source element locator
            target_locator: Target element locator
            timeout: Maximum time to wait for elements
            retries: Number of retry attempts
            cond: Expected condition to wait for
            duration: Scroll duration in milliseconds
        """
        source_ele = self._find_element(source_locator, timeout, retries, cond)
        target_ele = self._find_element(target_locator, timeout, retries, cond)
        self._driver.scroll(source_ele, target_ele, duration)

    def scroll_to_text(self, text: str, direction: str = "down"):
        """Scroll until text is found on screen.
        
        Args:
            text: Text to scroll to
            direction: Scroll direction ('up' or 'down')
        """
        self._driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
            f'new UiSelector().text("{text}"))'
        )

    def hide_keyboard(self):
        """Hide the keyboard if it's visible."""
        try:
            self._driver.hide_keyboard()
        except Exception:
            try:
                # Some devices might need a different approach
                self._driver.execute_script("mobile: hideKeyboard")
            except Exception:
                # If both methods fail, try pressing back button
                self.press_back()

    def press_back(self):
        """Press device back button."""
        self._driver.press_keycode(4)  # Android back button keycode

    def press_home(self):
        """Press device home button."""
        self._driver.press_keycode(3)  # Android home button keycode

    def press_enter(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1,
            cond=BaseActions.DEFAULT_CONDITION
    ):
        """Press enter key on an element.
        
        Args:
            locator: Element locator tuple
            timeout: Maximum time to wait for element
            retries: Number of retry attempts
            cond: Expected condition to wait for
        """
        element = self._find_element(locator, timeout, retries, cond)
        element.send_keys(Keys.ENTER)
