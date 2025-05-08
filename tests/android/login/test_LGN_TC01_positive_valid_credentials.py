import pytest

from src.core.config_manager import Config
from src.data.enums import Language
from src.utils.enum_utils import random_values
from src.utils.logging_utils import logger
from src.utils.common_utils import log_page_source
from src.core.driver.appium_driver import AppiumDriver


@pytest.mark.parametrize("language", random_values(Language, 1))
def test(pages, server, account, language):
    credentials = Config.get_credentials(server, account)

    logger.info("Step: Login with valid userid and password")
    pages.login_page.login(credentials.username, credentials.password, account, Language.ENGLISH)
    log_page_source(AppiumDriver._android_driver.page_source)
