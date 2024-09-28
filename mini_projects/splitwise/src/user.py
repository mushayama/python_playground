from typing import Type

class User:
    __userId: str = None
    __name: str = None
    __email: str = None
    __phoneNo: str = None
    __totalBalance: float = None
    __passbook: list[str] = None
    __amountOwed: dict[Type['User'], float] = None

    def __init__(self, userId: str, name: str, email: str, phoneNo: str) -> None:
        self.__userId = userId
        self.__name = name
        self.__email = email
        self.__phoneNo = phoneNo
        self.__totalBalance = 0
        self.__passbook = []
        self.__amountOwed = {}

    def getName(self) -> str:
        return self.__name

    def getUserId(self) -> str:
        return self.__userId

    def getTotalBalance(self) -> float:
        return self.__totalBalance

    def setAmountOwed(self, account: dict[Type['User'], float], clear: bool = False) -> None:
        if clear:
            self.__amountOwed={}
        for user in account.keys():
            if user not in self.__amountOwed.keys():
                self.__amountOwed[user]=0
            self.__amountOwed[user]+=account[user]
            if self.__amountOwed[user]==0:
                self.__amountOwed.pop(user)

    def addExpense(self, expenseId: str, account: dict[Type['User'], float]) -> None:
        self.__passbook.append(expenseId)
        for user in account.keys():
            if user not in self.__amountOwed.keys():
                self.__amountOwed[user]=0
            self.__amountOwed[user]+=account[user]
            if self.__amountOwed[user]==0:
                self.__amountOwed.pop(user)
            self.__totalBalance+=account[user]

    def showUserExpense(self, onlyOwed: bool) -> int:
        count=0
        for debtor in self.__amountOwed.keys():
            if self.__amountOwed[debtor]>0:
                count+=1
                print(debtor.getName() + " owes " + self.getName() + ": " + str(self.__amountOwed[debtor]))
            elif onlyOwed==False:
                count+=1
                print(self.getName() + " owes " + debtor.getName() + ": " + str(-1*self.__amountOwed[debtor]))
        return count