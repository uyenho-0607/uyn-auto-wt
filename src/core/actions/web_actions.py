from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.core.actions.base_actions import BaseActions
from src.data.consts import EXPLICIT_WAIT
from src.utils.assert_utils import soft_assert
from src.utils.logging_utils import logger


class WebActions(BaseActions):
    def __init__(self, driver):
        super().__init__(driver)

    # ------- ACTIONS ------ #
    def goto(self, url):
        """Navigate to a URL and wait for the page to be fully loaded."""
        self._driver.get(url)

    def wait_for_url(self, url: str, timeout: int = EXPLICIT_WAIT, retries=1):
        """Wait for the current URL to match the expected URL with retry mechanism."""
        wait = self._wait if timeout == EXPLICIT_WAIT else WebDriverWait(self._driver, timeout)

        for i in range(retries):
            try:
                wait.until(EC.url_to_be(url))

            except TimeoutException as e:
                logger.warning(f"Attempt {i + 1}/{retries} failed for URL '{url}': {type(e).__name__}")

            except Exception as e:
                logger.error(f"Unexpected error for URL '{url}': {type(e).__name__}")

        return self._driver.current_url

    def right_click(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1,
            cond=BaseActions.DEFAULT_CONDITION
    ):
        """Right-click on an element."""
        element = self._find_element(locator, timeout, retries, cond)
        self._action_chains.context_click(element).perform()

    def press_enter(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1,
            cond=BaseActions.DEFAULT_CONDITION
    ):
        """Press Enter key on an element."""
        element = self._find_element(locator, timeout, retries, cond)
        element.send_keys(Keys.ENTER)

    # ------- VERIFY ------ #

    def verify_url(self, expected_url: str, timeout: int = EXPLICIT_WAIT, retries: int = 1):
        """Verify that the current URL matches the expected URL with retry mechanism."""
        actual_url = self.wait_for_url(expected_url, timeout, retries)
        soft_assert(actual_url, expected_url)
