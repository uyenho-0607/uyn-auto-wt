import random

import pytest

from src.data.enums import AccountType
from src.data.object import ObjectDemoAccount
from src.utils.logging_utils import logger


@pytest.mark.demo
def test(pages):
    account_info = ObjectDemoAccount()
    use_default_deposit = random.randint(0, 1)

    logger.info("Step 1: Open demo account modal")
    pages.login_page.open_demo_account_creation()

    logger.info("Step 2: Fill in demo account details")
    pages.login_page.demo_account_modal.fill_demo_account_creation_form(account_info, default_deposit=use_default_deposit)

    logger.info("Step 3: Submit demo account creation form")
    pages.login_page.demo_account_modal.click_next_button()

    logger.info("Verify demo account ready message")
    pages.login_page.demo_account_modal.verify_ready_message()

    logger.info("Verify demo account username is correct")
    pages.login_page.demo_account_modal.verify_account_info(account_info.name)
    # save userid and password for validation
    user_id, password, *_ = pages.login_page.demo_account_modal.get_account_details().values()

    logger.info("Step 4: Click Sign in button")
    pages.login_page.demo_account_modal.sign_in_from_completion()

    logger.info("Verify demo tab is selected")
    pages.login_page.verify_account_tab_is_selected(AccountType.DEMO)

    logger.info("Verify autofill values of account ID and password is correct")
    pages.login_page.verify_account_autofill_value(user_id, password)

    logger.info("Step 5: Click Sign in button")
    pages.login_page.click_sign_in()

    logger.info("Verify login successfully")
    pages.home_page.feature_announcement_modal.got_it()
    pages.home_page.verify_account_info_displayed()

