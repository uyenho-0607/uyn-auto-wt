from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions, SafariOptions

from src.data.consts import GRID_SERVER
from src.data.project_info import DriverList


class WebDriver:
    _driver = None

    @classmethod
    def init_driver(cls, browser="chrome", headless=False, grid=False):
        match browser.lower():
            case "chrome":
                options = ChromeOptions()
                options.add_experimental_option('excludeSwitches', ['enable-logging', "enable-automation"])
                # options.add_argument("--incognito")
                prefs = {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False
                }
                options.add_experimental_option("prefs", prefs)

                if headless:
                    options.add_argument("--headless")

                if grid:  # using selenium-grid
                    driver = webdriver.Remote(GRID_SERVER, options=options)
                else:
                    driver = webdriver.Chrome(options=options)

            case "firefox":
                options = FirefoxOptions()
                if headless:
                    options.add_argument("--headless")

                if grid:
                    driver = webdriver.Remote(GRID_SERVER, options=options)
                else:
                    driver = webdriver.Firefox(options=options)

            case "safari":
                options = SafariOptions()
                if headless:
                    options.add_argument("--headless")

                if grid:
                    driver = webdriver.Remote(GRID_SERVER, options=options)
                else:
                    driver = webdriver.Safari(options=options)

            case _:
                raise ValueError(f"Invalid browser value: {browser!r} !!!")

        driver.maximize_window()
        driver.set_page_load_timeout(10)
        
        # Move browser to second display (assuming 1920x1080 resolution for main display)
        # This positions the window at x=2000 (past the first display) and y=0 (top of the screen)
        driver.set_window_position(2000, 0)
        
        DriverList.all_drivers["web"] = driver
        return driver

    @classmethod
    def quit(cls):
        if DriverList.all_drivers.get("web"):
            DriverList.all_drivers["web"].quit()
            DriverList.all_drivers["web"] = None
