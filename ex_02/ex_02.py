## ex_02 ##
class Budget:
    def __init__(self):
        self.__transactions = []
    
    def add_transactions(self, param):
        if(isinstance(param, int) or (isinstance(param, float))):
            self.__transactions.append(param)
        elif(isinstance(param, list)):
            for item in param:
                self.add_transactions(item)
        else:
            raise TypeError("Invalid datatype")
    def show_transactions(self):
        for item in self.__transactions:
            if item > 0:
                print("You've spent " + str(item) + " euros")
            elif item < 0:
                print("You've received " + str(item) + " euros")
            else:
                print("You've received or spent nothing :|")

myBudget = Budget()
myBudget.add_transactions([512 , 42.08 , -12])
myBudget.show_transactions()

