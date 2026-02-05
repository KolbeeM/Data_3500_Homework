"""
Programming Activity 1
Write a program which can tell if a 3 digit number is a palindrome. 
 - Create a variable, which stores user input. Prompt the user to enter a 3 digit number. 
 - Convert the user input into a integer (int). To get the first digit alone, floor division by 100. 
 - To get the 3rd digit alone, modulus by 10. 
 - Check if the first digit and 3rd digit are the same. 
 - If they are the same print("palindrome!!!!"). 
 - Else print("not palindrome!")
"""
digits = int(input("Enter a 3 digit number: "))
first_digit = digits // 100
last_digit = digits % 10
if first_digit == last_digit:
    print("palindrome!!!!")
else:
    print("not palindrome!")
"""
Programming Activity 2
Write a program which can adds up the numbers in the series:
1/2 + 1/4 + 1/8 + 1/16 + 1/32 for 1000 iterations.
create a variable for the denominator
for loop for 1000 iterations
start for loop at 1, go to 1000
variable to track the sum
What number is the result?
"""
sum = 0
denominator = 2
for i in range(1000):
    sum += 1/denominator
    denominator *= 2
print("sum: ", sum, "iteration", i)
"""
Programming Activity 3
Write a program which determines whether a child can sit in the front seat  of a car, using the following logic:
- if a child is 12 years old or older, they can sit in the front, regardless of weight.
- if a child is 11 years old, and over 90 pounds, they can sit in the front seat.
- if a child is under 11 years old, and over 100 pounds, they can sit in the front seat
- if a child does meet the criteria above they cannot sit in the front seat.
Your program will ask the user for a child's age and weight. Use Boolean variables to store the results of the criteria above. Use if statements and the Boolean variables created above to print a message to the user whether or not the child may sit in the front seat.
"""
age = int(input("enter childs age: "))
weight = int(input("enter childs weight in pounds: "))

met_1 = age >= 12
met_2 = (age == 11) and (weight > 90)
met_3 = (age < 11) and (weight > 100)

if met_1 or met_2 or met_3:
    print("Your child can sit in the front seat.")
else:
    print("Your child cannot sit in the front seat.")
"""
Programming Activity 4

Write a function named "welcome_fctn" which takes one argument, called "name".  Inside the function, print to the console "Welcome " name.
- Use the def command to define a function "welcome_fctn"
- Add a parameter list with one variable "name", i.e. (name)
- Print "Welcome " name in the function body.
- We don't need a return statement here, but keep in mind python does return nothing.
- Call the function, welcome_fctn(<your_name>)
"""
# def welcome_fctn(name):
#     print("welcome", name)
"""
Programming Activity 5

Update the function in activity one, and create a new string variable in the function called, welcome_message. The variable welcome_message should be 
assigned the value "Welcome " name. The same value printed in activity 1, but here you save it as a variable. Return the variable welcome_message.
- Assuming your function in programming activity 1 works, you will need to:
- Create a variable to store "Welcome " + name
- Return the value welcome_message
- There are a couple ways to test this. you could
         1. Print(welcome_fctn("Bob"))
         2. Create a variable to store what is returned by the function then print that
"""
# def welcome_fctn(name):
#    welcome_message = "Welcome " + name
#    return welcome_message
"""
Programming Activity 6

Update the function in activity one to have 3 variables: name (string),  age (int), favorite_color (string).  Create a new variable called welcome_message and assign it to the value "Welcome <name>, you are <age> years old, and <favorite_color> is your favorite color".  Return the variable welcome_message.
- Add two variables to your parameter list
- Concatenate those two variables in your welcome_message
- Return welcome_message just like you did in activity 2
- To test this, call welcome_fctn with 3 arguments
"""

def welcome_fctn(name, age, favorite_color):
    welcome_message = "Welcome " + name + ". You are " + str(age) + " years old and your favorite color is " + favorite_color
    return welcome_message

print(welcome_fctn("bob", 62, "blue"))