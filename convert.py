from decimal import *
from typing import Optional
from checks import _check_is_numeric

def to_decimal(number, prec: int=2) -> Optional[Decimal]:
    getcontext().prec = prec

    flag, number = _check_is_numeric(number)
    if flag:
        return Decimal(number)
    else:
        return

def to_int(number) -> Optional[int]:
    flag, number = _check_is_numeric(number)
    if flag:
        return int(number)
    else:
        return
