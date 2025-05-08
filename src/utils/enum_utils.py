import random


def get_values(enum_class) -> list:
    """
    Get all values from an enum-like class.
    """
    return [
        value for key, value in vars(enum_class).items()
        if not key.startswith('_') and isinstance(value, (str, int, float))
    ]


def random_values(enum_class, amount=1) -> list:
    return random.choices(get_values(enum_class), k=amount)


def random_value(enum_class):
    return random.choice(get_values(enum_class))
