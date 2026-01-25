balance = 5000
pin = 1234
def validate_intent(intent):
    prompt = input("press 1 to confirm your "+ intent)
    if int(prompt) == 1:
        return True
    else:
        return False


def validate_pin (user_pin):
    if int(user_pin) == pin: 
        return True
    else:
        return False
    
def deposit(amount):
    amount = int(amount)
    if validate_intent("deposit"):
        print(f"your new balance is {amount + balance}")
    else:
        print ("transaction aborted")

def withdrawal(amount):
    if int(amount) <= balance:
        if validate_intent("withdrawal"):
            user_pin = input("please enter your pin")
            if validate_pin(user_pin):
                print("pin ok, withdrawal is successful")
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
             
    
    
    
    



        
def cardless():
        if validate_intent("comfirmation"):
           print('welcome to cardless world')
        else:
           print("invalid entry")
def exit():
        if validate_intent("comfirmation"):
            print("transaction aborted")
        else:
            print("what do you want to do")
userintent = input("press 1 for deposit, 2 for withdrawal, 3 for airtime, 4 for cardless, 5 for exit")
if userintent == "1":
    pay = input("enter amount to deposit")
    deposit(pay)
elif userintent == "2":
    withdrawal_amount = input("enter amount to withdraw")
    withdrawal(withdrawal_amount)
elif userintent == "3":
    recharge_amount = input("enter amount to recharge")
    recharge_type=input("press 1 for mtn, 2 for airtel, 3 for glo")
    recharge_type = int(recharge_type)
    recharge(recharge_amount, recharge_type)







    
elif userintent == "4":
    cardless=input("are you sure you want to perform a cardless transaction")
    cardless()
elif userintent =="5":
    exit()
else:
     print("invalid input")