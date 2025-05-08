import random
import time

import pytest
from src.data.object import ObjectDemoAccount
from src.page_object.web.components.modals.demo_account import DemoAccountModal
from src.utils.logging_utils import logger
from src.utils.random_utils import random_invalid_email, random_number_by_length

pytestmark = [pytest.mark.not_live, pytest.mark.not_crm]


def test_missing_all_required_fields(pages):
    account_info = ObjectDemoAccount(name=None, email=None, dial_code=None, phone_number=None, agreement=False)
    validation_fields = list(DemoAccountModal.validation_fields.values())

    logger.info("Step 1: Open demo account modal")
    pages.login_page.open_demo_account_creation()

    logger.info(f"Step 2: Submit demo account creation form without input any field")
    time.sleep(1)  # wait a bit for loading deposit value
    pages.login_page.demo_account_modal.fill_demo_account_creation_form(account_info)
    pages.login_page.demo_account_modal.click_next_button()

    logger.info(f"Verify validation error messages for fields: {validation_fields!r}")
    pages.login_page.demo_account_modal.verify_field_validation(fields=validation_fields)


def test_invalid_email_and_phone_number_format(pages):
    account_info = ObjectDemoAccount(email=random_invalid_email(), phone_number=random_number_by_length())
    validation_fields = [DemoAccountModal.validation_fields.email, DemoAccountModal.validation_fields.phone_number]

    logger.info("Step 1: Open demo account modal")
    pages.login_page.open_demo_account_creation()

    logger.info(f"Step 2: Submit demo account creation form without invalid email and phone number format")
    time.sleep(1)  # wait a bit for loading deposit value
    pages.login_page.demo_account_modal.fill_demo_account_creation_form(account_info)
    pages.login_page.demo_account_modal.click_next_button()

    logger.info(f"Verify validation error messages for fields: {validation_fields!r}")
    pages.login_page.demo_account_modal.verify_field_validation(fields=validation_fields, validation_type="invalid")


@pytest.mark.parametrize("missing_field", random.choices(list(DemoAccountModal.validation_fields.keys())))
def test_single_missing_field(pages, missing_field):

    account_info = ObjectDemoAccount()
    account_info.set_value(missing_field, None)

    logger.info("Step 1: Open demo account modal")
    pages.login_page.open_demo_account_creation()

    logger.info(f"Step 3: Submit demo account creation form without input field: {missing_field!r}")
    time.sleep(1)
    pages.login_page.demo_account_modal.fill_demo_account_creation_form(account_info)
    pages.login_page.demo_account_modal.click_next_button()

    logger.info(f"Verify validation message for missing {missing_field}")
    pages.login_page.demo_account_modal.verify_field_validation(fields=[missing_field])
