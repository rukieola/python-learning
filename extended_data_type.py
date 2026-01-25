# list is a data type that hold more than one value and we access each value in the list with index number
'''
my_list = [3, 5, 6, 65, 25, 10, 40]
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[-3])
print(my_list[0:3])
# my_list.append(14)
print(my_list)
# remove_data = my_list.pop()
# print(my_list)
# print(remove_data)
list_copy = my_list.copy()
print (list_copy)
# my_list.clear()
# print(my_list)
my_list.insert(1, 234)
print(my_list)
'''
'''
def count_even(my_list):
  count = 0
  for item in my_list:
      if item %2 == 0:
        count +=1
  print(f"we have {count} even numbers")



my_list = [3, 5, 6, 65, 25, 10, 40]
count_even(my_list)



def total_list(yusroh_list):
  count = 0
  for item in yusroh_list:
    count += item
  print(count)


yusroh_list =[2,3,4,5,6,7,8,45,34,67,1]
total_list(yusroh_list)

def lowest_value(yusroh_list):
  count = 100
  for item in yusroh_list:
    if item < count:
      count = item
  print(count)

lowest_value(yusroh_list)
 '''
def highest_value(*our_list):
  count = 1
  for item in our_list:
    if item > count:
      count = item
  print(count)

highest_value(24,17,13)

'''

def sum_even(even):
  count = 0
  for item in even:
    if item % 2 ==0:
      count += item
  print(count)

sum_even(yusroh_list)

def odd_no(odd):
  count = 0
  for item in odd:
    if item%2 != 0:
      count += item
  print(count)


odd_no(yusroh_list)

print(yusroh_list[-3])

count = 5
def me(no):
  count = 5
  for item in yusroh_list:
    if item in yusroh_list >count:
      count += item
print(count)

me(yusroh_list)

yusroh_list =[2,3,4,5,6,7,8,45,34,67,1]

def middle(number):
  count = 0
  length = len(number)//2
  middle_value = number[length]
  print(middle_value)

middle(yusroh_list)
'''


