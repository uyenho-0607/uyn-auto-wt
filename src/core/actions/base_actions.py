from functools import wraps
from typing import Union

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.data.consts import EXPLICIT_WAIT
from src.data.project_info import StepLogs
from src.utils.allure_utils import capture_and_attach_screenshot
from src.utils.assert_utils import soft_assert
from src.utils.logging_utils import logger


def handle_broken_steps(func):
    """Decorator to handle broken steps and capture screenshots when element is not found."""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            # Save broken steps for custom report
            StepLogs.broken_steps.append(StepLogs.test_steps[-1])
            if "verify" in StepLogs.test_steps[-1].lower():
                StepLogs.broken_steps.append([item for item in StepLogs.test_steps if "step" in item.lower()][-1])

            capture_and_attach_screenshot(self._driver, name="broken")
            raise e

    return wrapper


class BaseActions:
    DEFAULT_CONDITION = EC.visibility_of_element_located

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(driver=self._driver, timeout=EXPLICIT_WAIT)
        self._action_chains = ActionChains(self._driver)

    @handle_broken_steps
    def _find_element(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1, cond=DEFAULT_CONDITION
    ) -> Union[WebElement, list[WebElement]]:
        """Find single element with retry mechanism. Raises Exception if not found after retries."""
        wait = self._wait if timeout == EXPLICIT_WAIT else WebDriverWait(self._driver, timeout)

        for i in range(retries):
            try:
                return wait.until(cond(locator))

            except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
                logger.warning(f"Attempt {i + 1}/{retries} failed for {locator}: {type(e).__name__}")

            except Exception as e:
                logger.error(f"Unexpected error for {locator}: {type(e).__name__}")

        raise Exception(f"Element with locator {locator} not found after {retries} attempt(s)")

    def _find_elements(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1
    ) -> list[WebElement]:
        """Find multiple elements with retry mechanism. Returns empty list if none found."""
        wait = self._wait if timeout == EXPLICIT_WAIT else WebDriverWait(self._driver, timeout)

        for i in range(retries):
            try:
                return wait.until(EC.presence_of_all_elements_located(locator))

            except (TimeoutException, StaleElementReferenceException, NoSuchElementException) as e:
                logger.warning(f"Attempt {i + 1}/{retries} failed for {locator}: {type(e).__name__}")

            except Exception as e:
                logger.error(f"Unexpected error for {locator}: {type(e).__name__}")

        return []

    def click(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1, cond=DEFAULT_CONDITION
    ):
        """Click on an element."""
        element = self._find_element(locator, timeout, retries, cond)
        element.click()

    def click_by_offset(
            self, locator: tuple[str, str], x_offset=0, y_offset=0,
            timeout=EXPLICIT_WAIT, retries=1, cond=DEFAULT_CONDITION
    ):
        ele = self._find_element(locator, timeout, retries, cond)
        self._action_chains.move_to_element_with_offset(ele, x_offset, y_offset).click().perform()

    def send_keys(
            self, locator: tuple[str, str], value: str,
            timeout=EXPLICIT_WAIT, retries=1, cond=DEFAULT_CONDITION
    ):
        """Send keys to an element."""
        element = self._find_element(locator, timeout, retries, cond)
        element.clear()
        element.send_keys(value)

    def get_attribute(
            self, locator: tuple[str, str], attribute: str,
            timeout=EXPLICIT_WAIT, retries=1, cond=DEFAULT_CONDITION
    ) -> str | None:
        """Get attribute value from an element."""
        element = self._find_element(locator, timeout, retries, cond)
        return element.get_attribute(attribute)

    def get_text(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1, cond=DEFAULT_CONDITION
    ) -> str:
        """Get text from element."""
        element = self._find_element(locator, timeout, retries, cond)
        return element.text

    def wait_for_element_invisible(self, locator: tuple[str, str], timeout=EXPLICIT_WAIT, retries=1):
        self._find_element(locator, timeout, retries, cond=EC.invisibility_of_element_located)

    def is_element_displayed(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT
    ) -> bool:
        """Check if element is displayed."""
        wait = self._wait if timeout == EXPLICIT_WAIT else WebDriverWait(self._driver, timeout)

        try:
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()

        except Exception:
            return False

    # ------- VERIFY ------ #
    def verify_element_is_displayed(
            self, locator: tuple[str, str], timeout=EXPLICIT_WAIT
    ):
        soft_assert(
            self.is_element_displayed(locator, timeout), True, f"Element with locator {locator} is not displayed"
        )
