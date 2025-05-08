import random

from src.core.config_manager import Config
from src.data.enums import Language
from src.utils.common_utils import translate_sign_in
from src.utils.enum_utils import get_keys, get_values
from src.utils.logging_utils import logger


def test(pages, server, account):
    credentials = Config.get_credentials(server, account)
    list_value = random.sample(get_values(Language), k=3)

    logger.info(f"Step 1: Change langauge -> {(value := list_value[0])}")
    pages.login_page.select_language(value)

    logger.info(f"Verify 'Sign in' button is changed to {translate_sign_in(value)!r}")
    pages.login_page.verify_language(value)

    logger.info(f"Step 2: Change langauge -> {(value := list_value[1])}")
    pages.login_page.select_language(value)

    logger.info(f"Verify 'Sign in' button is changed to {translate_sign_in(value)!r}")
    pages.login_page.verify_language(value)

    logger.info(f"Step 3: Change langauge -> {(value := list_value[-1])}")
    pages.login_page.select_language(value)

    logger.info(f"Verify 'Sign in' button is changed to {translate_sign_in(value)!r}")
    pages.login_page.verify_language(value)

    logger.info("Step 4: Continue to login ")
    pages.login_page.login(credentials.username, credentials.password, account)

    logger.info("Verify login success")
    pages.home_page.verify_account_info_displayed()
