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


def recharge(amount, recharge_type):
        if int(amount) <= balance:
            if validate_intent(recharge_type):
                user_pin= input("please enter your pin")
                if validate_pin(user_pin):
                  print("pin ok, recharge is successful")
                else:
                    print("invalid pin")
            else:
                 print("invalid entry")
        else:
            print("insufficient balance")


