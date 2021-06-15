# question 1
def hello_user(username):
    print("Hello " + username + "!")

hello_user('username')

#-----------------------------------------------

# question 2

current_number = 0 
while current_number < 100:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#-----------------------------------------------

#question 3

def max_num_in_list(a_list):
    max = a_list[0]

    for x in a_list:
        if x > max :
             max = x
      
    return max

a_list = [7, 8, 14, 21, 54]
print("max: ", max_num_in_list(a_list))

#-----------------------------------------------

#question4 

def is_leap_year(a_year):
    year = int(input('which year would you like to know? '))
    leap = False

    if year % 4 ==0:
        if year % 100 != 0 or year % 400 ==0:
            leap = True
    if leap:
        print(year, ' is a leap year.')
    else:
        print(year, ' is not a leap year.')

is_leap_year(2021)


#-----------------------------------------------


#question 5

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
      
first = [2, 3, 1, 4, 5]
second = [5, 6, 9, 2, 5]
print(is_consecutive(first))
print(is_consecutive(second))

