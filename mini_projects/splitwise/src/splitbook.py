from .user import User
from .expense import Expense
from .enums import ExpenseType
from .utils import verifyExpense, splitStrategyCreator

class SplitBook:
    __users: dict[str, User] = None
    __expense: dict[str, Expense] = None
    __expenseCount: int = None

    def __init__(self, noOfUsers) -> None:
        self.__users={}
        for count in range(noOfUsers):
            userId = "u"+str(count+1)
            self.addUser(userId, "User"+str(count+1), userId+"@gmail.com", "")
        self.displayUsers()

        self.__expense={}
        self.__expenseCount=0

    def addUser(self, userId: str, name: str, email: str, phoneNo: str) -> None:
        self.__users[userId] = User(userId, name, email, phoneNo)

    def displayUsers(self) -> None:
        print("Available users:", end=" ")
        for user in self.__users:
            print(user, end=" ")
        print("")

    def addExpense(self, type: ExpenseType, payee: str, involved: list[str], amount: float, shares: list[float]) -> None:
        if not self.verifyUsers(payee, involved):
            print("Inavlid users for expense")
            return
        if not verifyExpense(type, amount, len(involved), shares):
            print("Invalid Expense")
            return

        if type == ExpenseType.EQUAL:
            shares=[1]*len(involved)

        expenseId = str(self.__expenseCount)
        self.__expenseCount+=1
        involvedUsers = []
        for userId in involved:
            involvedUsers.append(self.__users[userId])
        splitStrategy = splitStrategyCreator(type)

        self.__expense[expenseId] = Expense(expenseId, self.__users[payee], involvedUsers, amount, shares, splitStrategy)


    def verifyUsers(self, payee: str, involved: list[str]) -> bool:
        if payee not in self.__users.keys():
            return False
        for user in involved:
            if user not in self.__users.keys():
                return False
        return True

    def showAll(self) -> None:
        count=0
        for user in self.__users:
            count+= self.__users[user].showUserExpense(True)
        if count==0:
            print("No balance")

    def show(self, userId: str) -> None:
        count = self.__users[userId].showUserExpense(False)
        if count==0:
            print("No balance")

    def simplify(self) -> None:
        amountByUser: list[list[float, User]]=[]
        for user in self.__users.values():
            if user.getTotalBalance()!=0:
                amountByUser.append([user.getTotalBalance(), user])
                user.setAmountOwed({}, True)
        amountByUser.sort(key=lambda a: a[0])

        while len(amountByUser)>0:
            print(amountByUser)
            if -1*amountByUser[0][0]==amountByUser[len(amountByUser)-1][0]:
                amountByUser[0][1].setAmountOwed({amountByUser[len(amountByUser)-1][1]: amountByUser[0][0]})
                amountByUser[len(amountByUser)-1][1].setAmountOwed({amountByUser[0][1]: amountByUser[len(amountByUser)-1][0]})
                amountByUser = amountByUser[1:-1]
            elif -1*amountByUser[0][0]<amountByUser[len(amountByUser)-1][0]:
                amountByUser[0][1].setAmountOwed({amountByUser[len(amountByUser)-1][1]: amountByUser[0][0]})
                amountByUser[len(amountByUser)-1][1].setAmountOwed({amountByUser[0][1]: -1*amountByUser[0][0]})
                amountByUser[len(amountByUser)-1][0]+= amountByUser[0][0]
                amountByUser = amountByUser[1:]
            else:
                amountByUser[0][1].setAmountOwed({amountByUser[len(amountByUser)-1][1]: -1*amountByUser[len(amountByUser)-1][0]})
                amountByUser[len(amountByUser)-1][1].setAmountOwed({amountByUser[0][1]: amountByUser[len(amountByUser)-1][0]})
                amountByUser[0][0]+= amountByUser[len(amountByUser)-1][0]
                amountByUser = amountByUser[:-1]