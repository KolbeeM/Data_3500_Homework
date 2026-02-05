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
