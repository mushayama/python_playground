from math import floor
from .enums import ExpenseType
from typing import Optional
from .splitStrategy import SplitStrategy, EqualStrategy, ExactStrategy, PercentStrategy, ShareStrategy

def rounnd_off(number: float) -> float:
    return floor(number*100)/100

def verify_expense(expense_type: ExpenseType, amount: float, no_of_involved: int, shares: list[float]) -> bool:
    if expense_type==ExpenseType.EQUAL:
        return True
    elif expense_type==ExpenseType.EXACT:
        return sum(shares)==amount and no_of_involved==len(shares)
    elif expense_type==ExpenseType.PERCENT:
        return sum(shares)==100 and no_of_involved==len(shares)
    elif expense_type==ExpenseType.SHARE:
        return no_of_involved==len(shares)
    return False

def split_strategy_creator(expense_type: ExpenseType) -> Optional[SplitStrategy]:
    if expense_type==ExpenseType.EQUAL:
        return EqualStrategy
    elif expense_type==ExpenseType.EXACT:
        return ExactStrategy
    elif expense_type==ExpenseType.PERCENT:
        return PercentStrategy
    elif expense_type==ExpenseType.SHARE:
        return ShareStrategy
    return None