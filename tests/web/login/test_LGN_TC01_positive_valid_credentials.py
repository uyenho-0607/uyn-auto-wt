import pytest

from src.core.config_manager import Config
from src.data.enums import Language, URLPaths
from src.utils.enum_utils import random_values
from src.utils.logging_utils import logger


@pytest.mark.parametrize("language", random_values(Language, 1))
def test(pages, server, account, language):
    credentials = Config.get_credentials(server, account)

    logger.info("Step 1: Login with valid userid and password")
    pages.login_page.login(credentials.username, credentials.password, account, language)
    pages.home_page.feature_announcement_modal.got_it()

    logger.info("Verify trade/ home page URL is correct")
    pages.home_page.verify_page_url(URLPaths.TRADE)

    logger.info("Verify account info is displayed")
    pages.home_page.verify_login_successful()

    logger.info("Step 2: User tries to logout")
    pages.home_page.setting.logout()

    logger.info("Verify login page URL is correct")
    pages.login_page.verify_page_url(URLPaths.LOGIN)

    logger.info("Verify login account tab is displayed")
    pages.login_page.verify_login_account_tab_is_displayed()
