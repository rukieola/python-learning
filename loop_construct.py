# loop construct is the method of repeating or iterating based on if condition is true
# WE MUST FIND A WAY TO MAKE THE CONDITION FALSE SO AS TO BREAK OUT OF THE REPITITION
# while True:
    # execute this
    # we must find a way to make the loop end
'''
count = 0

mult_table = int(input("what multiplication table would you like to learn? "))
mult_length = int(input("where would you like it to end? "))

while count <= mult_length:
    # print("we are now in loop")
    print(f"{mult_table} * {count} = {mult_table * count}")
    count += 1
'''
'''
count = 1
nick_name = "rukie"
guess = input("guess my nickname ")
while guess != nick_name:
    count += 1
    guess = input("you are wrong, guess again ")
    if guess == nick_name:
        print("you are right")
        
    if count ==3:
        print("game over")
        guess = nick_name
'''

# FOR LOOP
# it looks "for item in the list"
'''
user_name= "yusroh"
for item in user_name:
    print(item)
 '''



def consonant_count(my_word):
    count =  0
    for char in my_word:
        vowels = "aeiou"
        if char not in vowels:
            count +=1
    if count <=1:
        print(f"we have {count} consonant in your provided sentence")
    else:
        print(f"we have {count} consonants in your provided sentence")


def vowels_count(my_word):
    count =  0
    for char in my_word:
        vowels = "aeiou"
        if char in vowels:
            count +=1
    if count <=1:
        print(f"we have {count} vowel in your provided sentence")
    else:
        print(f"we have {count} vowels in your provided sentence")

my_word = input("enter your given word: ")
task = input("do you want to know vowels or consonant count?")
if task == "vowels":
    vowels_count(my_word)
else:
    consonant_count(my_word)

list ={2,3,4,5,6,7,8,23,56,34,86}


