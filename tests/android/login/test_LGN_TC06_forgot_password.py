import pytest

from src.utils.logging_utils import logger


@pytest.mark.uat
def test(pages, account, server):
    logger.info("Step 1: Select account type tab")
    pages.login_page.select_account_tab(account)
