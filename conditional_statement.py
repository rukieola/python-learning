# conditional statement
# deals with only true or false . if the condition is true, it will execute whatever is in the if statement but if its false, it will execute whatever in the else statement 
# the syntax is 
#  if condition: 
#     execute this  
#  else:
#       execute this
wallet = 200
recharge_card = input("how much do you want to buy?: ")
# print(recharge_card)
if wallet >= int(recharge_card): 
# if wallet >= recharge_card:
    print("successfully bought recharge card")
else:
    print("invalid amount or your balance is low")

# there are other conditions that will lead us to do else if, such as
# student grade, 
wallet.conjugate()
grade = input("what is your maths scores?: ")

if grade.isnumeric():
    grade = int(grade) 
    if grade <40:
        print("you failed woefully")
    elif grade >=40 and grade <50:
        print("you score E")
    elif grade >= 50 and grade <60:
        print("you score D")
    elif grade >= 60 and grade <70:
        print("you score C")
    elif grade >= 70 and grade <80:
        print("you score B")
    elif grade >= 80 and grade <100:
        print("you score A")
    else:
        print("invalid score")
else:
    print("invalid score, please input number")






