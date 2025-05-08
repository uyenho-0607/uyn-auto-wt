from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from selenium.common import WebDriverException

from src.data.project_info import DriverList
from src.utils.logging_utils import logger


class AppiumDriver:
    _appium_service = None

    @classmethod
    def __start_appium_service(cls, host="localhost", port=4723):
        cls._appium_service = AppiumService()
        args = [
            "-pa", "/wd/hub",
            "--address", host,
            "--port", str(port),
        ]

        logger.debug("- Starting appium service...")
        cls._appium_service.start(args=args, timeout_ms=30000)
        logger.info("- Appium service started !")

    @classmethod
    def init_android_driver(cls, host="http://localhost", port=4723) -> webdriver.Remote:
        options = UiAutomator2Options()
        options.udid = "R5CWA20BQ9P"
        options.app_package = "com.aquariux.wt.sit.lirunex"
        options.app_activity = ".MainActivity"
        options.app_wait_activity = ".MainActivity"
        options.auto_grant_permissions = True
        options.platform_name = "Android"
        options.device_name = "Galaxy S22"
        options.platform_version = "14"
        options.no_reset = False
        options.full_reset = False
        options.new_command_timeout = 60
        options.page_load_timeout = 30

        cls.__start_appium_service()

        try:
            logger.debug("- Init android driver...")
            driver = webdriver.Remote(f"{host}:{port}/wd/hub", options=options)
            
            DriverList.all_drivers["android"] = driver
            logger.info("- Android driver init !")
            return driver

        except WebDriverException as error:
            raise WebDriverException(f"Failed to init resources driver with error: {error!r}")

    @classmethod
    def quit_android_driver(cls):
        if DriverList.all_drivers["android"]:
            DriverList.all_drivers["android"].quit()
            DriverList.all_drivers["android"] = None

        cls.stop_appium_service()

    @classmethod
    def stop_appium_service(cls):
        if cls._appium_service:
            cls._appium_service.stop()
            cls._appium_service = None
