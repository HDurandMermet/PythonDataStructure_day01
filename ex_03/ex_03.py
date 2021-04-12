## ex_03 ##
import json 

class Budget:
    def __init__(self, path=None):
        if path is not None:
            with open(path) as f:
                self.__transactions = json.load(f)
        else:
            self.__transactions = {}

    def get_categories(self):
        cat_list = []
        transactions = self.__transactions['transactions']
        for item in transactions:
            for x in item:
                if x == "category":
                    cat_list.append(item[x])
        return cat_list
    def show_transactions(self, category):
        transactions = self.__transactions['transactions']
        for item in transactions:
            if item['category'] == category:
                print(item['value'])

myBudget = Budget("./data.json")
for category in myBudget.get_categories():
    print(category)
    myBudget.show_transactions(category)
