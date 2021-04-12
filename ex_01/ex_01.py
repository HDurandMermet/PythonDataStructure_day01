## ex_01 ##

def show_transactions(param):
    if(isinstance(param, list)):
        for item in param:
            if isinstance(item, int) or isinstance(item, float):
                if item > 0:
                    print("You've spent " + str(item) + " euros")
                elif item < 0:
                    print("You've received " + str(item) + " euros")
                else:
                    print("You've received or spent nothing :|")
            else:
                print("That's not a number you dingus!")
    else:
        print("I want a list!")


show_transactions ([512 , 42.08 , -12])
