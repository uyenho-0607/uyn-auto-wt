import pytest

from src.core.actions.web_actions import WebActions
from src.core.config_manager import Config
from src.core.driver.driver_manager import DriverManager
from src.page_object.web.pages.home_page import HomePage
from src.page_object.web.pages.login_page import LoginPage
from src.utils.logging_utils import logger


@pytest.fixture
def pages():
    """
    Fixture to initialize and provide page objects for login tests.
    Handles driver setup, page navigation, and cleanup.
    """
    logger.info("Initializing web driver")
    driver = DriverManager.get_driver(
        platform=Config.config.platform,
        browser=Config.config.browser,
        headless=Config.config.headless
    )
    actions = WebActions(driver)

    logger.info("Navigating to login page")
    actions.goto(Config.get_url_site())

    class PageContainer:
        login_page = LoginPage(actions)
        home_page = HomePage(actions)

    yield PageContainer

    logger.info("Cleaning up web driver")
    DriverManager.quit_driver(Config.config.platform)
