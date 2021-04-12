## ex_04 ##
from Finance import Budget

myBudget = Budget("./data.json")
for category in myBudget.get_categories():
    print(category)
    myBudget.show_transactions(category)
