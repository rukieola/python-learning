pin = 1234
balance = 5000

def validate_intent(intent):
        prompt = input("press 1 to confirm your " + intent  ) 
        if int(prompt) == 1:
            return True
        else:
            return False
        
def validate_pin (user_pin):
    if int(user_pin) == pin: 
        return True
    else:
        return False

    
def deposit(amount:int):
    if validate_intent("deposit"):
        user_pin = input("please enter your pin")
        if validate_pin(user_pin):
            print(f"pin ok, your new balance is {balance + amount}")
        else:        
           print ("Wrong pin Transaction aborted")
    else:
        print("invalid entry, transaction aborted") 

def withdrawal(amount):
    amount = int(amount)
    if amount <= balance:
        if validate_intent("withdrawal"):
            user_pin = input("please enter your pin")
            if validate_pin(user_pin):
                 print(f"pin ok, withdrawal is successful, your new balance is {balance - amount}")
            else:
                print ("invalid pin")
        else:
            print("transaction aborted")
    else:
        print("insufficient balance")
    
    
def recharge(amount, recharge_type):
        if int(amount)<= balance:
            if validate_intent("recharge"):
                user_pin= input("please enter your pin")
                if validate_pin(user_pin):
                    print("pin ok")
                    if recharge_type ==1:
                        print("mtn recharge is successful")
                    elif recharge_type ==2:
                            print("airtel recharge is successful")
                    elif recharge_type==3:
                            print("glo recharge is successful")     
                    else:       
                        print("invalid entry")
            else:
                print("invalid pin")
        else:
            print("insufficient balance")

        
def cardless(confirm):
        if int(confirm) == 1:
           print('welcome to cardless world')
        else:
           print("invalid entry")
def exit(confirm):
    if int(confirm) == 1:
        print("transaction aborted")
    else:
         print("what do you want to do? ")

