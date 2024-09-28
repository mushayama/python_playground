from abc import ABC, abstractmethod
from .enums import ExpenseType

class SplitStrategy(ABC):
    _type: ExpenseType = None

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def getSplitAmount(amount: float, shares: list[float]) -> list[float]:
        pass

class EqualStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.EQUAL

    def getSplitAmount(amount: float, shares: list[float]) -> list[float]:
        return [amount/(len(shares))]*len(shares)

class ExactStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.EXACT

    def getSplitAmount(amount: float, shares: list[float]) -> list[float]:
        return shares

class PercentStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.PERCENT

    def getSplitAmount(amount: float, shares: list[float]) -> list[float]:
        splitAmount=[]
        for share in shares:
            splitAmount.append(amount*share/100)
        return splitAmount

class ShareStrategy(SplitStrategy):
    def __init__(self) -> None:
        super().__init__()
        self._type = ExpenseType.SHARE

    def getSplitAmount(amount: float, shares: list[float]) -> list[float]:
        totalShare = sum(shares)
        splitAmount=[]
        for share in shares:
            splitAmount.append(amount*share/totalShare)
        return splitAmount
