from .enums import ExpenseType
from .user import User
from .splitStrategy import SplitStrategy

class Expense:
    __expense_id: str = None
    __type: ExpenseType = None
    __payee: User = None
    __involved: list[User] = None
    __shares: list[float] = None
    __amount: float = None
    __amount_per_user: list[float] = None
    __split_strategy: SplitStrategy = None

    def __init__(self, expense_id: str, payee: User, involved: list[User], amount: float, shares: list[float], split_strategy: SplitStrategy) -> None:
        self.__expense_id = expense_id
        self.__payee = payee
        self.__involved = involved
        self.__shares = shares
        self.__amount = amount
        self.__split_strategy = split_strategy
        self.__amount_per_user = self.__split_strategy.get_split_amount(self.__amount, self.__shares)

        self.__add_to_users()

    def __add_to_users(self) -> None:
        paid: dict[User, float] = {}
        for user in range(len(self.__involved)):
            if self.__involved[user] is not self.__payee:
                self.__involved[user].add_expense(self.__expense_id, {self.__payee: -1*self.__amount_per_user[user]})
                paid[self.__involved[user]] = self.__amount_per_user[user]
        self.__payee.add_expense(self.__expense_id, paid)
