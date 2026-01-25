'''
count = 0
def mult_table (number,length):
    count = 0
    while count <=length:
        print("we are now in loop")
        print(f"{number} * {count} = {number * count}")
        count += 1

number = int(input("what multiplication table would you like to learn? "))
length = int(input("where would you like it to end? "))
# mult_table(number, length)
'''
'''
count = 0
nick_name = "rukie"
def as_far_as (guess):
    while guess != nick_name:
        count += 1
    guess = input("you are wrong, guess again ")
    if guess == nick_name:
        print("you are right")
    if count ==3:
        print("game over")
        guess = nick_name



guess = input("guess my nickname ")
as_far_as (guess)
'''

'''
def count_vowel (word):
    count = 0
    while ('aeiou') in word:
        count +=1
    output = int(count)

word = input ("enter your given word ")
count_vowel (word)
'''
count =  0
my_word = input("enter your given word: ")
while count <= len(my_word):
    vowels = "aeiou"
    


                                                 

