from typing import Type

class User:
    __user_id: str = None
    __name: str = None
    __email: str = None
    __phone_no: str = None
    __total_balance: float = None
    __passbook: list[str] = None
    __amount_owed: dict[Type['User'], float] = None

    def __init__(self, userId: str, name: str, email: str, phone_no: str) -> None:
        self.__user_id = userId
        self.__name = name
        self.__email = email
        self.__phone_no = phone_no
        self.__total_balance = 0
        self.__passbook = []
        self.__amount_owed = {}

    def get_name(self) -> str:
        return self.__name

    def get_user_id(self) -> str:
        return self.__user_id

    def get_total_balance(self) -> float:
        return self.__total_balance

    def set_amount_owed(self, account: dict[Type['User'], float], clear: bool = False) -> None:
        if clear:
            self.__amount_owed={}
        for user in account.keys():
            if user not in self.__amount_owed.keys():
                self.__amount_owed[user]=0
            self.__amount_owed[user]+=account[user]
            if self.__amount_owed[user]==0:
                self.__amount_owed.pop(user)

    def add_expense(self, expense_id: str, account: dict[Type['User'], float]) -> None:
        self.__passbook.append(expense_id)
        for user in account.keys():
            if user not in self.__amount_owed.keys():
                self.__amount_owed[user]=0
            self.__amount_owed[user]+=account[user]
            if self.__amount_owed[user]==0:
                self.__amount_owed.pop(user)
            self.__total_balance+=account[user]

    def show_user_expense(self, only_owed: bool) -> int:
        count=0
        for debtor in self.__amount_owed.keys():
            if self.__amount_owed[debtor]>0:
                count+=1
                print(debtor.get_name() + " owes " + self.get_name() + ": " + str(self.__amount_owed[debtor]))
            elif only_owed==False:
                count+=1
                print(self.get_name() + " owes " + debtor.get_name() + ": " + str(-1*self.__amount_owed[debtor]))
        return count