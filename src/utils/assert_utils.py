import pytest_check as check

from src.data.project_info import DriverList, StepLogs
from src.utils.allure_utils import capture_and_attach_screenshot
from src.utils.logging_utils import logger


def soft_assert(actual, expected, error_message=None):
    error_message = error_message or f"Validation failed! Actual: {actual!r}, Expected: {expected!r}"
    res = check.equal(actual, expected, error_message)

    if not res:
        logger.error(error_message)

        for driver in DriverList.all_drivers.values():
            capture_and_attach_screenshot(driver)

        # save failed message details
        # failed_msg = check.check_log.get_failures()[-1]
        # failed_msg = failed_msg.rsplit(": ", 1)[1]

        # save failed verify step
        failed_step = [item for item in StepLogs.test_steps if "verify" in item.lower()][-1]
        StepLogs.all_failed_logs.append((failed_step, error_message))
