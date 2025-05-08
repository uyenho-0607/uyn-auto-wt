from src.data.enums import CountryDialCode, DepositAmount
from src.utils.enum_utils import random_value
from src.utils.random_utils import random_username, random_email, random_phone_number


class ObjectDemoAccount:
    """A class representing a demo account with user information.
    If no values are provided, generates random data for username, email, dial_code and phone_number.
    If None (by default) for any field, that field will be set to None.
    agreement is set to True by default.
    """

    def __init__(
            self, name: any = "", email: any = "", dial_code: any = "", phone_number: any = 0,
            deposit=None, agreement=True
    ):
        self.name = None if name is None else (name or random_username())
        self.email = None if email is None else (email or random_email())
        self.dial_code = None if dial_code is None else (dial_code or random_value(CountryDialCode))
        self.phone_number = None if phone_number is None else (phone_number or random_phone_number(self.dial_code))
        self.deposit = None if deposit is None else (random_value(DepositAmount))
        self.agreement = agreement

    def set_value(self, key, value):
        self.__setattr__(key, value)

    def get_value(self, key):
        return self.__getattribute__(key)
