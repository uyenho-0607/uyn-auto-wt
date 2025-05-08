from typing import Optional

from selenium.webdriver.common.keys import Keys

from src.data.consts import EXPLICIT_WAIT
from src.core.actions.base_actions import BaseActions


class MobileActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll(
            self, source_locator: tuple[str, str], target_locator: tuple[str, str],
            timeout=EXPLICIT_WAIT, retries=1, cond=BaseActions.DEFAULT_CONDITION, duration: Optional[int] = 500
    ):
        source_ele = self._find_element(source_locator, timeout, retries, cond)
        target_ele = self._find_element(target_locator, timeout, retries, cond)
        self._driver.scroll(source_ele, target_ele, duration)

    def hide_keyboard(self):
        """Hide keyboard."""
        try:
            self._driver.hide_keyboard()
        except Exception as e:
            # Some devices might need a different approach
            self._driver.execute_script("mobile: hideKeyboard")

    def press_back(self):
        """Press back button."""
        self._driver.press_keycode(4)  # Android back button keycode

    def press_home(self):
        """Press home button."""
        self._driver.press_keycode(3)  # Android home button keycode

    def press_enter(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1,
            cond=BaseActions.DEFAULT_CONDITION
    ):
        """Press Enter key on an element."""
        element = self._find_element(locator, timeout, retries, cond)
        element.send_keys(Keys.ENTER)
