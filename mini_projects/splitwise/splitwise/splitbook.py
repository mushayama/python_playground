from .user import User
from .expense import Expense
from .enums import ExpenseType
from .utils import verify_expense, split_strategy_creator

class SplitBook:
    __users: dict[str, User] = None
    __expense: dict[str, Expense] = None
    __expense_count: int = None

    def __init__(self, no_of_users) -> None:
        self.__users={}
        for count in range(no_of_users):
            user_id = "u"+str(count+1)
            self.add_user(user_id, "User"+str(count+1), user_id+"@gmail.com", "")
        self.display_users()

        self.__expense={}
        self.__expense_count=0

    def add_user(self, user_id: str, name: str, email: str, phone_no: str) -> None:
        self.__users[user_id] = User(user_id, name, email, phone_no)

    def display_users(self) -> None:
        print("Available users:", end=" ")
        for user in self.__users:
            print(user, end=" ")
        print("")

    def add_expense(self, type: ExpenseType, payee: str, involved: list[str], amount: float, shares: list[float]) -> None:
        if not self.verify_users(payee, involved):
            print("Inavlid users for expense")
            return
        if not verify_expense(type, amount, len(involved), shares):
            print("Invalid Expense")
            return

        if type == ExpenseType.EQUAL:
            shares=[1]*len(involved)

        expense_id = str(self.__expense_count)
        self.__expense_count+=1
        involved_users = []
        for user_id in involved:
            involved_users.append(self.__users[user_id])
        split_strategy = split_strategy_creator(type)

        self.__expense[expense_id] = Expense(expense_id, self.__users[payee], involved_users, amount, shares, split_strategy)


    def verify_users(self, payee: str, involved: list[str]) -> bool:
        if payee not in self.__users.keys():
            return False
        for user in involved:
            if user not in self.__users.keys():
                return False
        return True

    def show_all(self) -> None:
        count=0
        for user in self.__users:
            count+= self.__users[user].show_user_expense(True)
        if count==0:
            print("No balance")

    def show(self, user_id: str) -> None:
        count = self.__users[user_id].show_user_expense(False)
        if count==0:
            print("No balance")

    def simplify(self) -> None:
        amount_by_user: list[list[float, User]]=[]
        for user in self.__users.values():
            if user.get_total_balance()!=0:
                amount_by_user.append([user.get_total_balance(), user])
                user.set_amount_owed({}, True)
        amount_by_user.sort(key=lambda a: a[0])

        while len(amount_by_user)>0:
            print(amount_by_user)
            if -1*amount_by_user[0][0]==amount_by_user[len(amount_by_user)-1][0]:
                amount_by_user[0][1].set_amount_owed({amount_by_user[len(amount_by_user)-1][1]: amount_by_user[0][0]})
                amount_by_user[len(amount_by_user)-1][1].set_amount_owed({amount_by_user[0][1]: amount_by_user[len(amount_by_user)-1][0]})
                amount_by_user = amount_by_user[1:-1]
            elif -1*amount_by_user[0][0]<amount_by_user[len(amount_by_user)-1][0]:
                amount_by_user[0][1].set_amount_owed({amount_by_user[len(amount_by_user)-1][1]: amount_by_user[0][0]})
                amount_by_user[len(amount_by_user)-1][1].set_amount_owed({amount_by_user[0][1]: -1*amount_by_user[0][0]})
                amount_by_user[len(amount_by_user)-1][0]+= amount_by_user[0][0]
                amount_by_user = amount_by_user[1:]
            else:
                amount_by_user[0][1].set_amount_owed({amount_by_user[len(amount_by_user)-1][1]: -1*amount_by_user[len(amount_by_user)-1][0]})
                amount_by_user[len(amount_by_user)-1][1].set_amount_owed({amount_by_user[0][1]: amount_by_user[len(amount_by_user)-1][0]})
                amount_by_user[0][0]+= amount_by_user[len(amount_by_user)-1][0]
                amount_by_user = amount_by_user[:-1]