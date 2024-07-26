from decimal import *
from typing import Optional
from checks import _check_is_numeric

def to_decimal(number, prec: int=2) -> Optional[Decimal]:
    """
    Convert `number` to decimal rounding to `prec` digits.
    If `number` is not at number, None is returned.

    Attrs:
        number: Any object.
        prec: int, default 2.

    Return:
        Decimal(number) or None
    """
    getcontext().prec = prec

    if isinstance(number, Decimal) or number is None:
        return number
    verification_flag, convert_string = _check_is_numeric(number)
    if verification_flag:
        return Decimal(convert_string)
    else:
        return

def to_real(number, prec: int=2) -> Optional[Decimal]:
    """
    Convert `number` to decimal rounding to `prec` digits.
    If `number` is not at number, None is returned.

    Attrs:
        number: Any object.
        prec: int, default 2.

    Return:
        Decimal(number) or None
    """
    return to_decimal(number, prec)

def to_float(number) -> Optional[float]:
    """
    Convert `number` to float.
    If `number` is not at number, None is returned.
    """
    if isinstance(number, float) or number is None:
        return number
    verification_flag, convert_string = _check_is_numeric(number)
    if verification_flag:
        return float(convert_string)
    else:
        return

def to_int(number) -> Optional[int]:
    """
    Convert `number` to int.
    If `number` is not at number, None is returned.
    """
    if isinstance(number, int) or number is None:
        return number
    verification_flag, convert_string = _check_is_numeric(number)
    if verification_flag:
        return int(convert_string)
    else:
        return

def to_integer(number) -> Optional[int]:
    """
    Convert `number` to int.
    If `number` is not at number, None is returned.
    """
    return to_int(number)

def to_bool(input_flag) -> Optional[bool]:
    if isinstance(input_flag, bool) or input_flag is None:
        return input_flag
    numeric_flag = to_int(input_flag)
    if numeric_flag is None:
        return
    elif numeric_flag in [0, 1]:
        return bool(numeric_flag)
    else:
        if isinstance(input_flag, str) and input_flag.title() in ['True', 'False']:
            return bool(input_flag)
        else:
            return

def to_boolean(number) -> Optional[bool]:
    return to_bool(flag)

def to_str():
    pass

def to_string():
    pass

def to_datetime():
    pass

def to_date():
    pass
