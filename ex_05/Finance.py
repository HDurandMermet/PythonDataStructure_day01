import json

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False


class Budget:
    def __init__(self, path=None):
        if path is not None:
            self.path = path
            with open(path) as f:
                self.__transactions = json.load(f)
        else:
            self.__transactions = {}

    
    def add_transactions(self, cat, val):
        if isinstance(cat, str) and isfloat(val):
            new_obj = {"category" : cat, "value" : float(val)}
            self.__transactions['transactions'].append(new_obj)
            self.save_to_json(self.__transactions)
        else:
            raise TypeError("Invalid datatype")

    def get_categories(self):
        cat_list = []
        transactions = self.__transactions['transactions']
        for item in transactions:
            for x in item:
                if x == "category":
                    cat_list.append(item[x])
        return cat_list

    def give_balance(self):
        if self.__transactions:
            balance = 0
            transactions = self.__transactions['transactions']
            for item in transactions:
                balance += float(item["value"])
            return "Your balance is currently of " + str(balance) + " euros"
        else:
            return "No record of your transactions has been found"

    def history_transactions(self):
        return self.__transactions['transactions']

    def show_transactions(self, category):
        transactions = self.__transactions['transactions']
        for item in transactions:
            if item['category'] == category:
                print(item['value'])

    def save_to_json(self, data):
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)