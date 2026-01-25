balance = 5000
pin = 1234
userintent = input("press 1 for deposit, 2 for withdrawal, 3 for airtime, 4 for cardless, 5 for exit")
if userintent == "1":
    deposit_amount = input("enter amount to deposit")
    deposit_amount = int(deposit_amount)
    confirmation = input("press 1 to confirm, 2 to  cancel")
    if confirmation == "1":
        new_balance = deposit_amount + balance
        print(f"your new balance is {new_balance}")
    else:
        print(f"your balance remain {balance}")
elif userintent == "2":
    withdrawal_amount = input("enter amount to withdraw")
    if int(withdrawal_amount) <= balance:
        user_pin = input("please enter your pin")
        if int(user_pin) == pin:
            print("pin ok, withdrawal is successful")
        else:
            print ("invalid pin")
    else:
        print("insufficient balance")
elif userintent == "3":
    recharge = input("press 1 for mtn, 2 for airtel, 3 for glo")
    if recharge =="1":
        mtn =input("enter amount for mtn recharge")
        if int(mtn) <= balance:
            user_pin= input("please enter your pin")
            if int(user_pin) == pin: 
                print("pin ok, recharge is successful")
            else:
                print ("invalid pin")
        else:
            print("insufficient balance")
    elif recharge =="2":
        airtel =input("enter amount for airtel recharge")
        if int(airtel) <= balance:
            user_pin= input("please enter your pin")
            if int(user_pin) == pin: 
                print("pin ok, recharge is successful")
            else:
                print ("invalid pin")
        else:
            print("insufficient balance")
    elif recharge =="3":
        glo=input("enter amount for glo recharge")
        if int(glo) <= balance:
            user_pin= input("please enter your pin")
            if int(user_pin) == pin: 
                print("pin ok, recharge is successful")
            else:
                print ("invalid pin")
        else:
            print("insufficient balance")
elif userintent == "4":
       cardless = input("you are about to do a cardless transaction, press 1 to confirm")
       if cardless == '1':
           print('welcome to cardless world')
       else:
           print("invalid entry")
elif userintent =="5":
    exit = input("press 1 to confirm exit and 2 to cancel")
    if exit == "1":
        print("transaction aborted")
    else:
        print("what do you want to do")