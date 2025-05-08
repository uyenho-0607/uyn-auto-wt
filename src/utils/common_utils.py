import random
import string
import xml.dom.minidom
from typing import Tuple

from src.data.consts import ROOTDIR


def log_page_source(page_source):
    output_path = ROOTDIR / 'page_source.xml'
    dom = xml.dom.minidom.parseString(page_source)
    pretty_xml = '\n'.join([line for line in dom.toprettyxml(indent="  ").split('\n') if line.strip()])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)


def cook_element(element: tuple, *custom):
    by, ele = element
    return by, ele.format(*custom)


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


def random_userid() -> str:
    """
    Generate a random user ID in the format similar to the sit.yaml file.
    Format: 10 digits number
    
    Returns:
        str: Random user ID
    """
    return ''.join(random.choices(string.digits, k=10))


def random_password() -> str:
    """
    Generate a random password following the format in sit.yaml.
    Format: 12 characters including uppercase, lowercase, numbers, and special characters
    
    Returns:
        str: Random password
    """
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Ensure at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest with random characters from all sets
    all_chars = uppercase + lowercase + digits + special
    password.extend(random.choices(all_chars, k=8))

    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)


def generate_random_email() -> str:
    """
    Generate a random email address with some popular domain.
    
    Returns:
        str: Random email address
    """
    # Generate random username (8-12 characters)
    domains = ["aquriux.com", "gmail.com"]
    username_length = random.randint(8, 12)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return f"{username}@{random.choice(domains)}"


def format_number_with_commas(number: int) -> str:
    """
    Format a number with commas as a thousand separators.
    Args:
        number (int): The number to format
    Returns:
        str: The formatted number with commas
    Examples:
        >>> format_number_with_commas(3000)
        '3,000'
        >>> format_number_with_commas(1000000)
        '1,000,000'
    """
    return f"{number:,}"


def generate_phone_number(country_code: int) -> str:
    """
    Generate a random phone number based on the country code.
    """
    # Generate random number based on country code using match-case
    match str(country_code):
        case '84':  # Vietnam
            number = '9' + ''.join(random.choices(string.digits, k=8))
            return number
        case '65':  # Singapore
            number = ''.join(random.choices(string.digits, k=8))
            return number
        case '1':  # United States
            number = ''.join(random.choices(string.digits, k=10))
            return f'{number[:3]}-{number[3:6]}-{number[6:]}'
        case '86':  # China
            number = ''.join(random.choices(string.digits, k=11))
            return number
        case '66':  # Thailand
            number = '9' + ''.join(random.choices(string.digits, k=8))
            return number
        case _:  # Default case for other countries
            number = ''.join(random.choices(string.digits, k=10))
            return number


def generate_username() -> str:
    """
    Generate a random username with prefix 'Auto'.
    Format: Auto + random string of 8 characters (letters and numbers)
    
    Returns:
        str: Random username with 'Auto' prefix
    """
    random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"Auto {random_suffix}"
