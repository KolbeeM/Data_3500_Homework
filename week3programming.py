"""
Programming Activity 
 1. make a variable called apple_price (set it to whatever you want)
 2. make a variable called number_purchased (set it to whatever you want)
 3. make a variable called tax and set it equal to 1.07
 4. make a variable, total_bill and calculate it by: total_bill = apple_price * number_purchased * tax
 5. print clearly and cleanly how many apples were purchased and the total_bill
 6. add a check before the final print statement to see if total_bill is equal to 0.  If so, print a message to the user to check their inputs.
"""
apple_price = 127
number_purchased = 5
tax = 1.07
total_bill = apple_price * number_purchased * tax
if total_bill == 0:
    print("You cannot buy apple stock at $0.")
else:
    print("You just purchased", number_purchased, "apple shares at", apple_price, "for a total of", total_bill,".")
"""
Programming Activity 2
Write a program that asks the user how old they are, and what age they would like to live to. Calculate how long they have left to live (approximately), and then print a friendly message telling the user how long they have to 
live.
"""
current_age = int(input("How old are you? "))
death_age = int(input("What age would you like to live to? "))
years_remaining = death_age - current_age
print("you have approximately", years_remaining, "Years left to live. Don't waste them.")
"""
Programming Activity 3
Write a program that gets a user's score in this class, as a percentage i.e. 90 or 95. Write an if statement that checks to see if their score is equal to or greater than 93.  If so, print "Congratulations you got an A" else print "Congratulations, you still learned a ton!!!!"
"""
score = int(input("What is your score in this class as a percentage? "))
if score >= 93:
    print("Congratulations you got an A")
else:
    print("Congratulations, you still learned a ton!!!!")

