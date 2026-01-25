def cook_rice():
    print("place pot of water on the cooker")
    print("add some salt to taste")
    print("pour your washed rice and cover to boil")
    print("pour cooked rice in a sieve once soften")
    print("enjoy your rice")

cook_rice()

def mummy_routine(breakfast):
    print("adhkar and solat")
    print(f"set {breakfast} ")
    print("shower and dressing")
    print("wake up the kids and get them dressed")
    print("come to dinning for " + breakfast)
food = "ogi"
mummy_routine(food)

balance = 5000

def deposit():
    pay = input("enter amount to deposit")
    pay = int(pay)
    comfirmation = input("press 1 to confirm and 2 to exit")
    comfirmation == 1
    if int(comfirmation) == 1:
        print(f"your new balance is {pay + balance}")
    else:
        print ("transaction aborted")

deposit()