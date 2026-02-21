import personal_assessment.mine_atm as ATM
import personal_assessment.pos as pos

balance = 20000
pin = 2468


userintent = input("press 1 for deposit, 2 for withdrawal, 3 for airtime, 4 for cardless, 5 for exit " )
if userintent == "1":
    dep_amt=input("enter amount to deposit ")
    pos.deposit(int(dep_amt))

elif userintent == "2":
    withdrawal_amount = input("enter amount to withdraw ")
    pos.withdrawal(int(withdrawal_amount))
elif userintent == "3":
    recharge_amount = input("enter amount to recharge")
    recharge_type=input("press 1 for mtn, 2 for airtel, 3 for glo")
    recharge_type = int(recharge_type)
    pin = 2468
    pos.recharge(recharge_amount, recharge_type)
elif userintent == "4":
    no_card=input("press 1 to confirm you are performing a cardless transaction")
    pos.cardless(no_card)
elif userintent =="5":
    confirm_exit = input("press 1 to confirm you want to exit") 
    pos.exit(confirm_exit)
else:
    print("invalid input")