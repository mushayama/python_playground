from .enums import ExpenseType
from .user import User
from .splitStrategy import SplitStrategy

class Expense:
    __expenseId: str = None
    __type: ExpenseType = None
    __payee: User = None
    __involved: list[User] = None
    __shares: list[float] = None
    __amount: float = None
    __amountPerUser: list[float] = None
    __splitStrategy: SplitStrategy = None

    def __init__(self, expenseId: str, payee: User, involved: list[User], amount: float, shares: list[float], splitStrategy: SplitStrategy) -> None:
        self.__expenseId = expenseId
        self.__payee = payee
        self.__involved = involved
        self.__shares = shares
        self.__amount = amount
        self.__splitStrategy = splitStrategy
        self.__amountPerUser = self.__splitStrategy.getSplitAmount(self.__amount, self.__shares)

        self.__addToUsers()

    def __addToUsers(self) -> None:
        paid: dict[User, float] = {}
        for user in range(len(self.__involved)):
            if self.__involved[user] is not self.__payee:
                self.__involved[user].addExpense(self.__expenseId, {self.__payee: -1*self.__amountPerUser[user]})
                paid[self.__involved[user]] = self.__amountPerUser[user]
        self.__payee.addExpense(self.__expenseId, paid)
