from math import floor
from .enums import ExpenseType
from typing import Optional
from .splitStrategy import SplitStrategy, EqualStrategy, ExactStrategy, PercentStrategy, ShareStrategy

def rounndOff(number: float) -> float:
    return floor(number*100)/100

def verifyExpense(expenseType: ExpenseType, amount: float, noOfInvolved: int, shares: list[float]) -> bool:
    if expenseType==ExpenseType.EQUAL:
        return True
    elif expenseType==ExpenseType.EXACT:
        return sum(shares)==amount and noOfInvolved==len(shares)
    elif expenseType==ExpenseType.PERCENT:
        return sum(shares)==100 and noOfInvolved==len(shares)
    elif expenseType==ExpenseType.SHARE:
        return noOfInvolved==len(shares)
    return False

def splitStrategyCreator(expenseType: ExpenseType) -> Optional[SplitStrategy]:
    if expenseType==ExpenseType.EQUAL:
        return EqualStrategy
    elif expenseType==ExpenseType.EXACT:
        return ExactStrategy
    elif expenseType==ExpenseType.PERCENT:
        return PercentStrategy
    elif expenseType==ExpenseType.SHARE:
        return ShareStrategy
    return None