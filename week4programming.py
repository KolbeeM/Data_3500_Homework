"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user what generation they belong to based on the following rules/years:
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""

birthyear = int(input("What year where you born:"))

if birthyear >= 1997:
    print("You are a Zoomer")
elif birthyear >= 1981:
    print("You are a Millennial")
elif birthyear >= 1965:
    print("You are a GenX")
elif birthyear >= 1946:
    print("You are a Baby Boomer")
else:
    print("You are born before the Baby Boomer generation.")

"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""

age = int(input("what is your age:"))
current_year = 2026

while age  > 1:
    print("you were alive in", current_year)
    age -= 1
    current_year -= 1

else:
    print("you were born in", current_year)



"""
Programming Activity 3

Write a program that prints all the multiples of 5, from 5 to 95 using a for loop. 
"""

for number in range(5, 100, 5):
    print(number)

"""
Programming Activity 4

Write a program that prints all the multiples of 5, from 5 to 95 using a while loop.
"""

number = 5

while number <= 95:
    print(number)
    number += 5