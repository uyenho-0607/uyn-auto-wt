import os
import xml.dom.minidom
from typing import Tuple

from src.data.consts import ROOTDIR


def log_page_source(page_source):
    output_path = ROOTDIR / 'page_source_home.xml'
    dom = xml.dom.minidom.parseString(page_source)
    pretty_xml = '\n'.join([line for line in dom.toprettyxml(indent="  ").split('\n') if line.strip()])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)


def cook_element(element: tuple, *custom):
    by, ele = element
    return by, ele.format(*custom)


def translate_sign_in(language: str) -> str:
    translations = {
        "English": "Sign in",
        "简体中文": "登录",
        "繁体中文": "登錄",
        "ภาษาไทย": "ลงชื่อเข้าใช้",
        "Tiếng Việt": "Đăng nhập",
        "Melayu": "Log masuk",
        "Bahasa Indonesia": "Masuk",
        "Japanese": "ログイン",
        "Korean": "로그인",
        "Arabic": "تسجيل الدخول.",
    }

    return translations.get(language, "Translation not available")


def calculate_tp_sl(
        entry_price: float, tp_percentage: float = 0.02, sl_percentage: float = 0.01) -> Tuple[float, float]:
    """
    Calculate take profit and stop loss levels based on entry price and percentages.
    
    Args:
        entry_price (float): The entry price of the position
        tp_percentage (float, optional): Take profit percentage. Defaults to 2% (0.02)
        sl_percentage (float, optional): Stop loss percentage. Defaults to 1% (0.01)
    
    Returns:
        Tuple[float, float]: A tuple containing (take_profit_price, stop_loss_price)
    """
    take_profit = entry_price * (1 + tp_percentage)
    stop_loss = entry_price * (1 - sl_percentage)
    return take_profit, stop_loss


def format_number_with_commas(number: int) -> str:
    """
    Format a number with commas as a thousand separators.
    Examples: 1000000 -> '1,000,000'
    """
    return f"{number:,}"


if __name__ == '__main__':
    os.makedirs("videos", exist_ok=True)