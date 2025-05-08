import pytest

from src.core.config_manager import Config
from src.data.enums import Language
from src.utils.enum_utils import random_values
from src.utils.logging_utils import logger


@pytest.mark.uyn
@pytest.mark.parametrize("language", random_values(Language, 2))
def test(android_pages, server, account, language):
    credentials = Config.get_credentials(server, account)

    logger.info("Step 1: Login with valid userid and password")
    android_pages.login_page.login(credentials.username, credentials.password, account, Language.ENGLISH)

    logger.info("Verify account info is displayed")
    android_pages.home_page.verify_account_info_displayed()

    logger.info("Step 2: User tries to logout")
    android_pages.home_page.settings.logout()

    logger.info("Verify login account tabs is displayed")
    android_pages.login_page.verify_account_tab_is_displayed()
