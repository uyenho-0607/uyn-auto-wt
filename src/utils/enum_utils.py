import random


def get_values(class_obj) -> list:
    """
    Get all values from a class.
    Filters out internal attributes, methods, and other non-data attributes.
    """
    return [
        value for key, value in vars(class_obj).items()
        if not key.startswith('_') and not callable(value)
    ]


def get_keys(class_obj, except_values=None) -> list:
    """
    Get all keys from a class.
    Filters out internal attributes, methods, and other non-data attributes.
    """
    except_values = except_values or []
    except_values = except_values if isinstance(except_values, list) else [except_values]

    return [
        key for key, value in vars(class_obj).items()
        if not key.startswith('_') and not callable(vars(class_obj)[key]) and value not in except_values
    ]


def get_key(class_obj, value) -> str:
    """Get a specific key from a class"""
    return next((k for k, v in vars(class_obj).items() if not k.startswith('_') and v == value), None)


def random_values(class_obj, amount=1) -> list:
    return random.choices(get_values(class_obj), k=amount)


def random_value(class_obj):
    return random.choice(get_values(class_obj))
