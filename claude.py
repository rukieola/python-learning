# Write a loop that prints all numbers from 1 to 20, but only prints the odd numbers.
# for number in range(1, 21):
    # if number % 2 != 0:
        # print(number)
# Create a loop that asks the user to enter a number 5 times, then calculates and prints the sum of all entered numbers.
'''
total = 0

for i in range(5):
    number = int(input("Enter a number: "))
    total += number
print(f"The sum of all entered numbers is: {total}")
'''

# Write a function called repeat_greeting that takes two parameters: a name (string) 
# and a number (integer). The function should print a personalized greeting that many times.

def repeat_greeting(name:str,number:int=4):
    for num in range (number):
        print(f"hello {name}")

name =input("what is your name ")
number=int(input("how many times should i greet you? "))
repeat_greeting(name, number)




