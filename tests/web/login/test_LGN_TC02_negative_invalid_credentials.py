from src.core.config_manager import Config
from src.data.enums import Language, URLPaths
from src.data.ui_messages import UIMessages
from src.utils.logging_utils import logger
from src.utils.random_utils import random_password, random_userid


def test(pages, account, server):
    credentials = Config.get_credentials(server, account)

    logger.info("Step 1: Login with valid userid and invalid password")
    pages.login_page.login(credentials.username, random_password(), account, Language.ENGLISH)

    logger.info("Verify URL remains on login page")
    pages.login_page.verify_page_url(URLPaths.LOGIN)

    logger.info(f"Verify {UIMessages.LOGIN_INVALID_CREDENTIALS!r} error message is displayed")
    pages.login_page.verify_alert_error_message(UIMessages.LOGIN_INVALID_CREDENTIALS)

    logger.info("Step 2: Login with invalid userid and valid password")
    pages.login_page.login(random_userid(), credentials.password, account, Language.ENGLISH)

    logger.info("Verify URL remains on login page")
    pages.login_page.verify_page_url(URLPaths.LOGIN)

    logger.info(f"Verify {UIMessages.LOGIN_INVALID_CREDENTIALS!r} error message is displayed")
    pages.login_page.verify_alert_error_message(UIMessages.LOGIN_INVALID_CREDENTIALS)

    logger.info("Step 3: Login with both invalid userid and password")
    pages.login_page.login(random_userid(), random_password(), account, Language.ENGLISH)

    logger.info("Verify URL remains on login page")
    pages.login_page.verify_page_url(URLPaths.LOGIN)

    logger.info(f"Verify {UIMessages.LOGIN_INVALID_CREDENTIALS!r} error message is displayed")
    pages.login_page.verify_alert_error_message(UIMessages.LOGIN_INVALID_CREDENTIALS)
