from src.splitbook import SplitBook
from src.enums import ExpenseType

def commandPalette() -> None:
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

def __main__():
    splitbook = SplitBook(5)
    commandPalette()

    while(True):

        command = input("Enter command: ").split()

        if command[0]=="EXIT":
            break
        elif command[0]=="SHOW":
            if len(command)==1:
                splitbook.showAll()
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
            noOfInvolved = command[i]
            i+=1
            involved=[]
            for j in range(int(noOfInvolved)):
                involved.append(command[i+j])
            i+=int(noOfInvolved)
            expenseType = ExpenseType[command[i]]
            i+=1
            shares=[]
            if expenseType!=ExpenseType.EQUAL:
                for j in range(int(noOfInvolved)):
                    shares.append(float(command[i+j]))

            splitbook.addExpense(expenseType, payee, involved, float(amount), shares)

__main__()