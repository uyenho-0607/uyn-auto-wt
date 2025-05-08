import os.path
import shutil

import allure
import pytest

from src.core.config_manager import Config
from src.core.driver.driver_manager import DriverManager
from src.data.consts import ROOTDIR, VIDEO_DIR
from src.data.project_info import DriverList
from src.utils.allure_utils import log_step_to_allure, custom_allure_report, capture_and_attach_video
from src.utils.logging_utils import logger


def pytest_addoption(parser: pytest.Parser):
    parser.addoption("--env", default="sit", help="Environment to run tests (sit, release_sit, uat)")
    parser.addoption("--client", default="lirunex",
                     help="Client to test (lirunex, transactionCloud) - single value only")
    parser.addoption("--server", default="mt4,mt5", help="Server types to test (mt4,mt5) - comma separated")
    parser.addoption("--account", default="demo,live", help="Account types to test (demo,live, crm) - comma separated")
    parser.addoption("--platform", default="web", help="Platform to run tests (web, ios, android)")
    parser.addoption("--user", help="Custom username")
    parser.addoption("--password", help="Custom password")
    parser.addoption("--browser", default="chrome", help="Browser for web tests (chrome, firefox, safari)")
    parser.addoption("--headless", default=False, action="store_true", help="Run browser in headless mode")
    parser.addoption("--grid", default=False, action="store_true", help="Run browser in headless mode")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item: pytest.Item):
    """Setup test and configure Allure reporting"""

    # Set up Allure test structure
    server = getattr(item.callspec, "params", {}).get("server", "mt4").upper()
    account = getattr(item.callspec, "params", {}).get("account", "live").capitalize()
    package_name = item.parent.parent.name.capitalize()

    # Set allure labels
    allure.dynamic.parent_suite(server)
    allure.dynamic.suite(account)
    allure.dynamic.sub_suite(package_name)

    if item.get_closest_marker("mt5") and Config.get_value("server") == "mt4":
        pytest.skip("This test is for mt5 server only")

    if item.get_closest_marker("uat") and Config.get_value("env") != "uat":
        pytest.skip("This test is for UAT environment only")

    print("\x00")  # print a non-printable character to break a new line on console
    logger.info(f"- Running test case: {item.parent.name} - [{server}] - [{account}] ")


def pytest_runtest_teardown(item: pytest.Item):
    """Cleanup after test execution"""
    pass


def pytest_sessionstart(session: pytest.Session):
    print("\x00")  # print a non-printable character to break a new line on console
    logger.debug("============ pytest_sessionstart ============ ")

    logger.info(">> Load environment configuration")
    Config.load_config(session.config.getoption("env"))

    Config.set_value("client", session.config.getoption("client"))
    logger.info(f">> Client: {Config.get_value("client")!r}")

    # Set users config values

    Config.set_value("server", session.config.getoption("server"))
    Config.set_value("account", session.config.getoption("account"))

    Config.set_value("platform", session.config.getoption("platform"))
    Config.set_value("browser", session.config.getoption("browser"))
    Config.set_value("headless", session.config.getoption("headless"))
    Config.set_value("allure_dir", session.config.getoption("allure_report_dir"))


def pytest_sessionfinish(session: pytest.Session):
    DriverManager.quit_driver(Config.config["platform"])

    allure_dir = session.config.option.allure_report_dir
    if allure_dir and os.path.exists(ROOTDIR / allure_dir):
        custom_allure_report(allure_dir)  # custom allure report

        # Set allure report properties
        _platform = session.config.getoption("platform")
        browser = session.config.getoption("browser")

        platform = f"{_platform.capitalize()}" + (f" - {browser.capitalize()}" if _platform == "web" else "")

        env_data = {
            "Client": " ".join(map(str.capitalize, Config.get_value("client").split("_"))),
            "Platform": platform,
            "Environment": session.config.getoption("env").capitalize(),
        }

        with open(f"{allure_dir}/environment.properties", "w") as f:
            for key, value in env_data.items():
                f.write(f"{key}={value}\n")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Handle test reporting and Allure steps"""
    outcome = yield
    report = outcome.get_result()

    platform = Config.get_value("platform")
    driver = DriverList.all_drivers.get(platform)
    allure_dir = item.config.option.allure_report_dir

    if not driver:
        return

    # Start recording at the beginning of the test
    if report.when == "setup" and platform in ['android', 'ios']:
        if allure_dir and os.path.exists(ROOTDIR / allure_dir):
            try:
                driver.start_recording_screen(options={"bit_rate": 200000, "video_size": "480x270"})
                logger.debug(f"Started screen recording for {platform} test")
            except Exception as e:
                logger.error(f"Failed to start screen recording: {str(e)}")

    # Handle test completion
    if report.when == "call":
        if allure_dir and os.path.exists(ROOTDIR / allure_dir):
            log_step_to_allure()  # show test steps and verify on allure

            try:
                # Attach video for both web and mobile
                capture_and_attach_video(driver)
                logger.debug(f"Video recording attached to Allure report for {platform} test")
            except Exception as e:
                logger.error(f"Failed to handle video recording: {str(e)}")


@pytest.fixture(scope="session", autouse=True)
def setup_video_folder():
    if Config.get_value("platform") in ["android", "ios"] and Config.get_value("allure_dir"):
        if os.path.exists(VIDEO_DIR):
            shutil.rmtree(VIDEO_DIR)

        os.makedirs(VIDEO_DIR)
