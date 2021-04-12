## ex_05 ##
import sys
from pprint import pprint

from Finance import Budget

def main():
    myBudget = Budget("./data.json")
    first_choice = input("Choose between : \n"
                    "1 - consult my balance \n"
                    "2 - add new transaction\n"
                    "3 - consult your transactions history\n"
                    "4 - quit\n")

    if int(first_choice):
        if int(first_choice) == 1:
            print(myBudget.give_balance())
        elif int(first_choice) == 2:
            user_cat = input("Please enter a category:\n")
            if user_cat:
                value_cat = input("Please enter a value:\n")
                if value_cat:
                    myBudget.add_transactions(user_cat, value_cat)
                    print("Your record has been successfully updated!\n")
        elif int(first_choice) == 3:
            pprint(myBudget.history_transactions())
        elif int(first_choice) == 4:
            print('Bye')
        else:
            print('Invalid option')


if __name__ == "__main__":
    main()
