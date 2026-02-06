"""
3.4 (Fill in the Missing Code) In the code below

for ***:
    for ***:
        print('@')
    print()
replace the *** so that when you execute the code, it displays two rows, each containing seven @ symbols, as in:

@@@@@@@
@@@@@@@
"""

for row in range(2):
    for column in range(7):
        print('@', end=' ')
    print()

"""
3.9 (Separating the Digits in an Integer) In Exercise 2.11, you wrote a script that separated a five-digit integer into its individual digits and displayed them. Reimplement your script to use a loop that in each iteration “picks off” one digit (left to right) using the // and % operators, then displays that digit.
Update: For 3.9, have the user enter an integer between 7 and 10 digits (not five-digit).
Remember, you’ll need to convert the inputted string to an integer. Here is an example output:
Enter a number 7 to 10 digits: 
"""
number = int(input("Enter a number 7 to 10 digits: "))
digits = len(str(number))
div = 10 ** (digits - 1)
print("the digits are:")

while div > 0:
    digit = number // div
    print(digit)

    number %= div
    div //= 10
"""
3.11 (Miles Per Gallon) Drivers are concerned with the mileage obtained by their automobiles. One driver has kept track of several tankfuls of gasoline by recording miles driven and gallons used for each tankful. Develop a sentinel-controlled-repetition script that prompts the user to input the miles driven and gallons used for each tankful. The script should calculate and display the miles per gallon obtained for each tankful. After processing all input information, the script should calculate and display the combined miles per gallon obtained for all tankfuls (that is, total miles driven divided by total gallons used).
Enter the gallons used (-1 to end): 12.8
Enter the miles driven: 287
The miles/gallon for this tank was 22.421875
Enter the gallons used (-1 to end): 10.3
Enter the miles driven: 200
The miles/gallon for this tank was 19.417475
Enter the gallons used (-1 to end): 5
Enter the miles driven: 120
The miles/gallon for this tank was 24.000000
Enter the gallons used (-1 to end): -1
The overall average miles/gallon was 21.601423
"""

miles = 0
gallons = 0

gallons_used = int(input("Enter the gallons used (-1 to end): "))
while gallons_used != -1:
    miles_used = int(input("Enter the miles driven: "))

    mpg = miles_used / gallons_used
    print("The mpg for this tank was", mpg)
    miles += miles_used
    gallons += gallons_used
    print()
    gallons_used = int(input("Enter the gallons used (-1 to end): "))
if gallons != 0:
    overall_mpg = miles / gallons
    print("The overall average mpg was: ", overall_mpg)
else:
    print("enter data dummy.")

"""
3.12 (Palindromes) A palindrome is a number, word or text phrase that reads the same backwards or forwards. For example, each of the following five-digit integers is a palindrome: 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate the number into its digits.]
"""

digits = int(input("Enter a 5 digit number: "))
first_digit = digits // 10000
last_digit = digits % 10

second_digit = (digits // 1000) % 10
fourth_digit = (digits // 10) % 10

if first_digit == last_digit and second_digit == fourth_digit:
    print("palindrome!!!!")
else:
    print("not palindrome!")


"""
3.14 (Challenge: Approximating the Mathematical Constant π) Write a script that computes the value of π from the following infinite series. Print a table that shows the value of π approximated by one term of this series, by two terms, by three terms, and so on. How many terms of this series do you have to use before you first get 3.14? 3.141? 3.1415? 3.14159?
You do not need to approximate to 3.1415 and 3.14159. You can
just approximate to 3.14 and 3.141, but please tell me at what iteration of the loop you see
3.14 twice in a row, not just once. Same for 3.141, tell me at which iteration in the loop you
3.141 twice in a row, not just once.
Hint: your for loop shouldn’t have to go more than 3000 iterations.
Another hint: The reason I updated this requirement is because people’s AWS has been
crashing when you run a for loop above 10000. Setting it to 3000, should not crash the
server, and be enough to allow you to approximate to 3.14 and 3.141.
"""
pi = 0
denominator = 1

pi_2 = 0
pi_3 = 0
look_314 = False
look_3141 = False
print("term\tPI Number")

for i in range(3000):
    if i % 2 != 0:
        pi -= 4 / denominator
    else:
        pi += 4 / denominator
        
    denominator += 2

    if i <= 10:
        print(i, "\t", round(pi, 5))
    pi_314 = str(round(pi, 2))
    pi_3141 = str(round(pi, 3))

    if pi_314 == "3.14" and pi_2 == "3.14" and not look_314:
        print("3.14 is in a row at iteration", i + 1)
        look_314 = True

    if pi_3141 == "3.141" and pi_3 == "3.141" and not look_3141:
        print("3.141 is in a row at iteration", i + 1)
        look_3141 = True
        
    pi_2 = pi_314
    pi_3 = pi_3141