from .splitbook import SplitBook
from .enums import ExpenseType

def command_palette() -> None:
    print("1: SHOW - display all balances")
    print("2: SHOW <user_id> - display balances for a particular user")
    print("3: EXPENSE <user_id_of_payee> <amount_paid> <no. of involved_users> <list of involved users> <Expense Type> <Expense Type specifications>")
    print("\t <Expense Type> : <Expense Type specifications>")
    print("\t EQUAL : None")
    print("\t EXACT : list of amount owed per user that adds up to total amount")
    print("\t PERCENT : list of percent owed by each user")
    print("\t SHARE : list of share in expense by each user")
    print("4: SIMPLIFY: simplify expenses")
    print("5: EXIT - exit the app")

def main():
    splitbook = SplitBook(5)
    command_palette()

    while(True):

        command = input("Enter command: ").split()

        if command[0]=="EXIT":
            break
        elif command[0]=="SHOW":
            if len(command)==1:
                splitbook.show_all()
            else:
                splitbook.show(command[1])
        elif command[0]=="SIMPLIFY":
            splitbook.simplify()
        elif command[0]=="EXPENSE":
            i = 1
            payee = command[i]
            i+=1
            amount = command[i]
            i+=1
            no_of_involved = command[i]
            i+=1
            involved=[]
            for j in range(int(no_of_involved)):
                involved.append(command[i+j])
            i+=int(no_of_involved)
            expense_type = ExpenseType[command[i]]
            i+=1
            shares=[]
            if expense_type!=ExpenseType.EQUAL:
                for j in range(int(no_of_involved)):
                    shares.append(float(command[i+j]))

            splitbook.add_expense(expense_type, payee, involved, float(amount), shares)
