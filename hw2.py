"""
2.3 (FILL IN THE MISSING CODE) Replace *** in the following code with a statement that will print a message like 'Congratulations! Your grade of 91 earns you an A in this course'. Your statement should print the value stored in the variable grade:
if grade >= 90:
    ***
"""

grade = 91
if grade >= 90:
    print("Congratulations! Your grade of", grade, "earns you an A in this course.")

"""
2.4 (ARITHMETIC) For each of the arithmetic operators +, -, *, /, // and **, display the value of an expression with 27.5 as the left operand and 2 as the right operand.
"""
age = 27.5
print(age + 2)
print(age - 2)
print(age * 2)
print(age / 2)
print(age // 2)
print(age ** 2)

"""
2.5 (Circle Area, Diameter and Circumference) For a circle of radius 2, display the diameter, circumference and area. Use the value 3.14159 for π. Use the following formulas (r is the radius): diameter = 2r, circumference = 2πr and area = πr2. [In a later chapter, we’ll introduce Python’s math module which contains a higher-precision representation of π.]
"""

radius = 2
pi = 3.14159
r = radius
diameter = 2*r
print("The diameter is:", diameter)
circumference = 2 * pi * r
print("The circumference is:", circumference)
area = pi * r * 2
print("The area is:", area)

"""
2.6 (ODD OR EVEN) Use if statements to determine whether an integer is odd or even. [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by 2.]
"""

number = int(input("Give me a number: "))

if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

"""
2.7 (Multiples) Use if statements to determine whether 1024 is a multiple of 4 and whether 2 is a multiple of 10. (Hint: Use the remainder operator.)
"""

if 1024 % 4 == 0:
    print(1024, "is a multiple of 4")
else:
    print(1024, "is not a multiple of 4")

if 2 % 10 == 0:
    print(2, "is a multiple of 10")
else:
    print(2, "is not a multiple of 10")

"""
2.8 (Table of Squares and Cubes) Write a script that calculates the squares and cubes of the numbers from 0 to 5. Print the resulting values in table format, as shown below. Use the tab escape sequence to achieve the three-column output.
"""
print('number\tsquare\tcube')

print(0, '\t', 0**2, '\t', 0**3)
print(1, '\t', 1**2, '\t', 1**3)
print(2, '\t', 2**2, '\t', 2**3)
print(3, '\t', 3**2, '\t', 3**3)
print(4, '\t', 4**2, '\t', 4**3)
print(5, '\t', 5**2, '\t', 5**3)