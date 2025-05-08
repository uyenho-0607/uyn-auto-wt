from typing import Any

from src.core.config_manager import Config
from src.core.driver.appium_driver import AppiumDriver
from src.core.driver.web_driver import WebDriver
from src.utils.logging_utils import logger


class DriverManager:

    @classmethod
    def get_driver(cls, platform=Config.get_value("platform") or "web", **kwargs) -> Any:
        """
        Get a driver instance for the specified platform.
        """
        match platform.lower():
            case "web":
                return WebDriver.init_driver(
                    browser=kwargs.get("browser", Config.get_value("browser")),
                    headless=kwargs.get("headless", Config.get_value("headless")),
                    grid=kwargs.get("grid", Config.get_value("grid")),
                )

            case "ios":
                logger.warning("iOS driver initialization not implemented yet")
                return None

            case "android":
                return AppiumDriver.init_android_driver()

            case _:
                raise ValueError(f"Invalid platform: {platform}")

    @classmethod
    def quit_driver(cls, platform=Config.get_value("platform") or "web"):
        match platform.lower():
            case "web":
                WebDriver.quit()

            case "ios":
                logger.warning("iOS driver quit not implemented yet")

            case "android":
                AppiumDriver.quit_android_driver()

            case _:
                raise ValueError(f"Invalid platform: {platform}")

