import pytest
from src.utils.common_utils import generate_random_email, generate_username
from src.utils.logging_utils import logger


@pytest.mark.general
def test(pages, server):
    username = generate_username()
    email = generate_random_email()

    logger.info("Step 1: Open demo account modal")
    pages.login_page.open_demo_account_creation()

    logger.info("Step 2: Fill in demo account details")
    pages.login_page.open_demo_account_modal.input_name(username)
    pages.login_page.open_demo_account_modal.input_email(email)
    pages.login_page.open_demo_account_modal.input_phone_number()
    pages.login_page.open_demo_account_modal.input_deposit()
    pages.login_page.open_demo_account_modal.click_agreement()

    logger.info("Step 3: Submit demo account creation form")
    pages.login_page.open_demo_account_modal.click_next_button()
    breakpoint()
