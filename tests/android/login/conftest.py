import pytest

from src.core.actions.mobile_actions import MobileActions
from src.core.config_manager import Config
from src.core.driver.driver_manager import DriverManager
from src.page_object.android.pages.home_page import HomePage
from src.page_object.android.pages.login_page import LoginPage
from src.utils.logging_utils import logger


@pytest.fixture
def android_pages():
    """
    Fixture to initialize and provide page objects for login tests.
    Handles driver setup and cleanup.
    """
    logger.info("Initializing Android driver")
    driver = DriverManager.get_driver(
        platform=Config.config.platform
    )
    actions = MobileActions(driver)

    class PageContainer:
        login_page = LoginPage(actions)
        home_page = HomePage(actions)

    yield PageContainer

    logger.info("Cleaning up Android driver")
    DriverManager.quit_driver(Config.config.platform)
