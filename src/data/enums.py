# -- GENERAL -- #
from src.utils.enum_utils import get_values


class SiteURLs:
    MEMBER_SITE = "base"
    ADMIN_PORTAL = "bo"
    ROOT_ADMIN = "root"


# -- URL PATHS -- #
class URLPaths:
    LOGIN = "login"
    TRADE = ""
    ASSETS = "assets"
    SIGNAL = "signal"
    MARKETS = "markets"
    CALENDAR = "calendar"
    NEWS = "news"
    EDUCATION = "education"


class Client:
    LIRUNEX = "lirunex"
    TRANSACTION_CLOUD = "transactionCloud"


class Server:
    MT4 = "mt4"
    MT5 = "mt5"


class AccountType:
    DEMO = "demo"
    CRM = "crm"
    LIVE = "live"


# -- LOGIN PAGE -- #

class Language:
    ENGLISH = "English"
    SIMPLIFIED_CHINESE = "简体中文"
    TRADITIONAL_CHINESE = "繁体中文"
    THAILAND = "ภาษาไทย"
    VIETNAM = "Tiếng Việt"
    MELAYU = "Melayu"
    BAHASA_INDONESIA = "Bahasa Indonesia"
    JAPANESE = "Japanese"
    KOREAN = "Korean"
    ARABIC = "Arabic"


class CountryDialCode:
    # Some common countries
    SINGAPORE = 65
    UNITED_STATES = 1
    VIETNAM = 84
    CHINA = 86
    THAILAND = 66


class DepositAmount:
    THREE_THOUSAND = 3000
    FIVE_THOUSAND = 5000
    TEN_THOUSAND = 10000
    TWENTY_FIVE_THOUSAND = 25000
    FIFTY_THOUSAND = 50000
    ONE_HUNDRED_THOUSAND = 100000
    FIVE_HUNDRED_THOUSAND = 500000
    ONE_MILLION = 1000000
    FIVE_MILLION = 5000000


# -- HOME PAGE -- #
class Features:
    TRADE = "Trade"
    MARKETS = "Markets"
    ASSETS = "Assets"
    SIGNAL = "Signal"
    CALENDAR = "Calendar"
    NEWS = "News"
    EDUCATION = "Education"


# -- SETTING -- #
class SettingOpt:
    SWITCH_TO_LIVE = "switch-to-live"
    CHANGE_PASSWORD = "change-password"
    CHANGE_LANGUAGE = "language"
    LINKED_DEVICES = "linked-device"
    CONTACT_INFORMATION = "contact-information"
    LOG_OUT = "logout"

    # mobile only
    ONE_CLICK_TRADING = "oct"
    APPEARANCE = "appearance"


# -- TRADE -- #
class OrderType:
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop limit"  # MT5


class Expiry:
    GOOD_TILL_CANCELLED = "good-till-cancelled"
    GOOD_TILL_DAY = "good-till-day"
    GOOD_TILL_END = "good-till-end"
    # MT5
    SPECIFIED_DATE = "specified-date"
    SPECIFIED_DATE_TIME = "specified-date-and-time"


class FillPolicy:  # MT5
    FILL_OR_KILL = "fill-or-kill"
    IMMEDIATE_OR_CANCEL = "immediate-or-cancel"
    RETURN = "return"


class AssetTabs:
    OPEN_POSITION = "open-positions"
    PENDING_ORDERS = "pending-orders"
    POSITIONS_HISTORY = "history"

if __name__ == '__main__':
    print(get_values(Language))