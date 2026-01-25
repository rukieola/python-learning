pins = 12345
pin = input("welcome to zanziber bank, please enter your pin")
print(pin)
if pins == int(pin):
    print("pin accepted")
    userintent = input("press 1 for deposit, 2 for withdrawal, 3 for airtime purchase, 4 for cardless transaction")
    if userintent == "1":
        print("you are about to make a deposit")
    elif userintent == "2":
        print("you are about to withdraw")
    elif userintent == "3":
        print("you are about to buy airtime")
    elif userintent == "4":
        print("you are about to make a cardless transaction")
    else:
        print("invalid entry, please try again")
else:
    print("Invalid Pin, try again")
