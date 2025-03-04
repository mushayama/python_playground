from abc import ABC, abstractmethod
from .enums import ExpenseType

class SplitStrategy(ABC):
    _type: ExpenseType = None

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_split_amount(amount: float, shares: list[float]) -> list[float]:
        pass

class EqualStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.EQUAL

    def get_split_amount(amount: float, shares: list[float]) -> list[float]:
        return [amount/(len(shares))]*len(shares)

class ExactStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.EXACT

    def get_split_amount(amount: float, shares: list[float]) -> list[float]:
        return shares

class PercentStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.PERCENT

    def get_split_amount(amount: float, shares: list[float]) -> list[float]:
        split_amount=[]
        for share in shares:
            split_amount.append(amount*share/100)
        return split_amount

class ShareStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.SHARE

    def get_split_amount(amount: float, shares: list[float]) -> list[float]:
        total_share = sum(shares)
        split_amount=[]
        for share in shares:
            split_amount.append(amount*share/total_share)
        return split_amount
