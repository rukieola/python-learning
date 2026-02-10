# function is a set of functional routine that we write and call anytime we need it to execute whatever in it
    # standard step: contains the exact things we need
'''
def greet(time_of_the_day):
    print(f"good {time_of_the_day} ")
    


def sum_numbers(num_1, num_2 ):
    print(f"{num_1} + {num_2} = {int(num_1) + int(num_2)}")



# timing = input("what is the time of the day: ")
# greet(timing)
# greet()
# greet()
# number_1 = input("enter first number you want to sum: ")
# number_2 = input("enter second number you want to sum: ")
'''

# sum_numbers(number_1, number_2)54
def arithmetic(first_number:int, second_number:int, operator:str):
    if operator == "+" or operator == "add" or operator == "addition":
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    elif operator == "-" or operator == "minus" or operator == "subtract" or operator =="deduct" or operator == "subtraction":
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    elif operator == "*" or operator == "multiply" or operator == "multiplication" or operator == "times":
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    elif operator == "/" or operator == "divide" or operator == "division" or operator == "split":
        print(f"{first_number} / {second_number} = {first_number / second_number}")
    else:
        print("invalid operation")

first_number = int(input("enter the first number you want to compute"))
second_number = int(input("enter the second number you want to compute"))
operator =input("what operator would you like to perform")
arithmetic(first_number, second_number, operator)



# number_1 = input("enter first number you want to compute: ")
# number_2 = input("enter second number you want to compute: ")
# operation = input("what arithmetic operation would you like to perform?: ")

# arithmetic(number_1, number_2, operation)

def addition(first_number:int, second_numbe:int):
    print(f"{first_number} + {second_number} = {first_number + second_number}") 

def subtraction(first_number:int, second_number:int):
    print(f"{first_number} - {second_number} = {first_number - second_number}") 

def multiplication(first_number:int, second_number:int):
    print(f"{first_number} * {second_number} = {first_number * second_number}") 

def division(first_number:int, second_number:int):
    print(f"{first_number} / {second_number} = {first_number / second_number}") 

number_1 = int(input("enter first number you want to compute: "))
number_2 = int(input("enter second number you want to compute: "))


addition(number_1, number_2)
division(number_1, number_2)

'''
if operation == "+":
    addition(number_1, number_2)
elif operation == "-":
    subtraction(number_1, number_2)
elif operation == "*":
    multiplication(number_1, number_2)
elif operation == "/":
    division(number_1, number_2)
else:
    print("invalid entry")

# local and global variable
# local variables are variable which are accessible within their locality declaration
# global variables are variable which are accessible insideand outside of  any function

# wallet = 2000

def make_payment():
    purchase = 1200
    if wallet >= purchase:
        print("your payment has been confirmed")
    else:
        print("insufficient fund")

# return- keyword -anything written after it will have no response
def addition(number_1, number_2):
    return number_1 + number_2
int(addition(2,3))
# print(result)



# make_payment()
# print(wallet)

# default parameters
# they are parameters we set value for even when they didnot input any argument at the point of calling the function
def greet_user(username="bobby"):
    print("hello, good day " + username)
'''

# greet_user("ayinla")

# kwarg- key words argument
# they are specifying particular parameter name to pass an argument

# addition(first_number=34, 12)