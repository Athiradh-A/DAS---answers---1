import math 
import random
# #Chris owns an auto repair business and has several employees. If any employee works over
# #40 hours in a week, he pays them 1.5 times their regular hourly pay rate for all hours over 40.
# #Design a simple payroll program that calculates an employee’s gross pay, including any
# #overtime wages.
# #You design the following algorithm:
# #Get the number of hours worked.
# #Get the hourly pay rate.
# #If the employee worked more than 40 hours:
# #Calculate and display the gross pay with overtime.
# #Else:
# #Calculate and display the gross pay as usual.

time = int(input("enter time worked this week:"))
pay = int(input("enter normal pay per week:"))
if time >= 40:
    pay = pay * 1.5
    print("extra pay is:",pay)
else:print('normal pay is:',pay)

# #The date June 10, 1960, is special because when it is written in the following format, the
# #month times the day equals the year: 6/10/60.Design a program that asks the user to enter a month (in numeric form),
# #a day, and a two digit year. The program should then determine whether the month times the day equals the year. If
# #so, it should display a message saying the date is magic. Otherwise, it should display a message saying the 
# # date is not magic.

mont = int(input("enter month in numeric form:"))
day = int(input("enter day:"))
yer = int(input("enter last 2 digits of year:"))
if mont * day == yer:
    print("date is magic")
else:
    print("date is not magic")

# #A software company sells a package that retails for $99. Quantity discounts are given
# #according to the following table:
# #Quantity Discount
# #10-19 20%
# #20-49 30%
# #50-99 40%
# #100 or more 50%
# #Write a program that asks the user to enter the number of packages purchased. The program
# #should then display the amount of the discount (if any) and the total amount of the purchase
# #after the discount.

amt_package = int(input("enter number of packages inputted:"))
if amt_package >= 10 and amt_package <= 19:
    print("discount is 20%")
elif amt_package >= 20 and amt_package <= 49:
    prijt("discount is 30%")
elif amt_package >= 50 or amt_package <= 99:
    print("discount is 40%")
elif amt_package >= 100:
    print("discount is 50%")

# #Write a program that asks the user to enter a number of seconds, and works as follows:
# #• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
# #than or equal to 60, the program should display the number of minutes in that many seconds.
# #• There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater
# #than or equal to 3,600, the program should display the number of hours in that many seconds.
# #• There are 86,400 seconds in a day. If the number of seconds entered by the user is greater
# #than or equal to 86,400, the program should display the number of days in that many seconds.

seconds = int(input("enter number of seconds:"))
if seconds >= 60 and seconds <= 3599:
    print("number of minutes is:",seconds / 60)
elif seconds >= 3600 and seconds <= 86390:
     print("number of hours is ",seconds / 3600)
elif seconds >= 86400:
    print("number of days is", seconds / 86400)
else:print("out of range")

# #Serendipity Booksellers has a book club that awards points to its customers based on the
# #number of books purchased each month.
# #The points are awarded as follows:
# # • If a customer purchases 0 books, he or she earns 0 points.
# # • If a customer purchases 1 book, he or she earns 5 points.
# # • If a customer purchases 2 books, he or she earns 15 points.
# # • If a customer purchases 3 books, he or she earns 30 points.
# # • If a customer purchases 4 or more books, he or she earns 60 points.
# #Write a program that asks the user to enter the number of books that he or she has purchased
# #this month and displays the number of points awarded.

number = int(input("enter number of books purchased:"))
if number == 0 :
    print("you get 0 points")
elif number == 1:
    print("you earned 5 points")
elif number == 2:
    print("earned 15 points")
elif number == 3:
    print("earned 30 points ")
elif number >= 4:
    print("earned 60 points")

# #Positions on a chess board are identified by a letter and a number. The letter identifies the
# #column, while the number identifies the row, as shown below:
# #Write a program that reads a position from the user. Use an if statement to determine if the
# #column begins with a black square or a white square. Then use modular arithmetic to report the
# #colour of the square in that row. For example, if the user enters a1 then your program should
# #report that the square is black. If the user enters d5 then your program should report that the
# #square is white. Your program may assume that a valid position will always be entered. It does
# #not need to perform any error checking.

letter = input("enter column name(a - h):")
number = int(input("enter row name(1 - 8):"))
if letter == 'a' or letter == 'c'or letter =='e' or letter == 'g':
    if number % 2 == 0:
        print("column is white")
    else:
        print("column is black")
else:
    if number % 2 != 0:
        print("column is white")
    else:
        print("column is black")

# #A model of worldwide population growth, in billions of people, since 2000 is given by this
# #formula: Population = 6.0 e**0.02[Year - 2000] Using this formula, write a program to estimate the
# #worldwide population in the year 2052

year = int(input("enter year:"))
base = 2.71828
population = 6.0 * (base**(0.02 * (year - 2000)))
print("population by year",year,"is:{:.4f}".format(population))

# #A bakery sells loaves of bread for Rs. 75 each. Day old bread is discounted by 60 percent.
# #Write a program that begins by asking the customer about his choice of bread and read the
# #number of loaves of day old bread or new bread or both being purchased. Then your program
# #should display the regular price for the bread, the discount because it is a day old, and the
# #total price. All of the values should be displayed using two decimal places.

choice = int(input("enter choice of bread (new [1]/ day old [2] / both [3]:"))
discount = 0.6 * 75
total_amt = 0
if choice == 1:
    amt = int(input("enter quantity of bread:"))
    price = amt * 75.00
    print("price is :{:.2f}".format(price))
elif choice == 2:
    amt = int(input("enter quantity of bread:"))
    price = amt * discount
    print("price for ",amt,"day old bread is:{:.2f}".format(price))
elif choice == 3:
    new_brd = int(input("enter amount of new bread:"))
    old_brd = int(input("enter amount of day old bread:"))
    new_price = new_brd * 75
    old_price = old_brd * discount
    total_amt = new_price + old_price
print("total amount:{:.2f}".format(total_amt))

# # Write a program that generates a random number in the range of 1 through 100 and asks the
# # user to guess what the number is. If the user’s guess is higher than the random number, the
# # program should display “Too high, try again.” If the user’s guess is lower than the random
# # number, the program should display “Too low, try again.” If the user guesses the number, the
# # application should congratulate the user.

rando_num = random.randint(0,101)
print(rando_num)
user_input = int(input("guess the number:"))
if user_input == rando_num:
    print("guessed number is the random number")
else:
    print("not the random number")
    while rando_num != user_input:
        user_input = int(input("guess the number:"))
        if user_input > rando_num:
            print("number guessed is greater than given random number")
        elif user_input < rando_num:
            print("number guessed is lesser than given random number ")
        elif user_input == rando_num:
            print("congrats ! you guessed right !")

# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
# scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

side1 = int(input("enter length of side 1 of triangle :"))
side2 = int(input("enter length of side 2 of triangle :"))
side3 = int(input("enter length of side 3 of triangle :"))

if side1 == side2 == side3:
    print("triangle is equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("triangle is isoceles")
elif side1 != side2 != side3:
    print("triangle is scalene")

# Write a program that determines the name of a shape from its number of sides. Read the
# number of sides from the user and then report the appropriate name as part of a meaningful
# message.
# Your program should support shapes with anywhere from 3 up to (and including) 10 sides. If
# a number of sides outside of this range is entered then your program should display an
# appropriate error message.

side = int(input('enter number of sides:'))
if side <= 2:
    print("only point or plane exists")
else:
    if side == 3:
        print("triangle")
    elif side == 4:
        print("quadrilateral")
    elif side == 5:
        print('pentagon')
    elif side == 6:
        print("hexagon")
    elif side == 7:
        print('heptagon')
    elif side == 8:
        print('octagon')
    elif side == 9:
        print("nonagon")
    elif side == 10:
        print("decagon")

# It is commonly said that one human year is equivalent to 7 dog years. However this simple
# conversion fails to recognize that dogs reach adulthood in approximately two years. As a
# result, some people believe that it is better to count each of the first two human years as 10.5
# dog years, and then count each additional human year as 4 dog years.
# Write a program that implements the conversion from human years to dog years described
# above. Ensure that your program works correctly for conversions of less than two human
# years and for conversions of two or more human years. Your program should display an
# appropriate error message if the user enters a negative number.

age = int(input("enter age of human:"))
if age < 0:
    print("no negative age!!")
else:
    two_yrs = 10.5
    dog_age = 10.5 + ((age - 2)*4)
    print("human age in dog years:",dog_age)

# The year is divided into four seasons: spring, summer, fall and winter. While the exact dates
# that the seasons change vary a little bit from year to year because of the way that the calendar
# is constructed, we will use the following dates for this exercise:
# Season  First Day
# Spring  March 20
# Summer  June 21
# Fall    September 22
# Winter  December 21
# Create a program that reads a month and day from the user. The user will enter the name of
# the month as a string, followed by the day within the month as an integer. Then your program
# should display the season associated with the date that was entered.


# Get input from the user
month = input("Enter the month: ")
day = int(input("Enter the day: "))
month = month.upper()
if (month == "March" and day >= 20) or (month == "April" or month == "May") or (month == "June" and day < 21):
    season = "Spring"
elif (month == "June" and day >= 21) or (month == "July" or month == "August") or (month == "September" and day < 22):
    season = "Summer"
elif (month == "September" and day >= 22) or (month == "October" or month == "November") or (month == "December" and day < 21):
    season = "Fall"
else:
    season = "Winter"
print(f"The season associated with {month} {day} is {season}.")

# It is common for images of a country’s previous leaders, or other individuals of historical
# significance, to appear on its money. The individuals that appear on banknotes in the United
# States are listed in Table. Write a program that begins by reading the denomination of a
# banknote from the user. Then your program should display the name of the individual that
# appears on the banknote of the entered amount. An appropriate error message should be
# displayed if no such note exists.

money = int(nput("enter denomination(1,2,5,10,20,50,100):"))
if money == 1:
    print("GEorge Washington")
elif money == 2:
    print("Thomas Jefferson")
elif money == 5:
    print("Abraham Lincoln")
elif money == 10:
    print("Alexander Hamilton")
elif money == 20:
    print("Andrew Jackson")
elif money == 50:
    print("Ulysses S Grant")
elif money == 100:
    print("Benjamin Franklin")
else:
    print("NO SUCH DENOMINATION")

# Write a program that computes the real roots of a quadratic function. Your program should
# begin by prompting the user for the values of a, b and c. Then it should display a message
# indicating the number of real roots, along with the values of the real roots (if any). These
# roots can be computed using the quadratic formula, shown below:

coeff_1 = int(input("enter coefficient of x^2:"))
coeff_2 = int(input("enter coefficient of x:"))
coeff_3 = int(input("enter constant term:"))
# x = (-b ± √ (b2 - 4ac) )/2a
real_root = - coeff_2 + ((((coeff_2**2) - 4 * coeff_1 * coeff_3))** -1)/(2 * coeff_1)
real_root_positve =  coeff_2 + ((((coeff_2**2) - 4 * coeff_1 * coeff_3))** -1)/(2 * coeff_1)
print("real - root:{:.3f}".format(real_root))
print("real + root:{:.3f}".format(real_root_positve))

# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is shown in
# the table below. The pattern repeats from there, with 2012 being another year of the dragon,
# and 1999 being another year of the hare.

# Year Animal
# 2000 Dragon
# 2001 Snake
# 2002 Horse
# 2003 Sheep
# 2004 Monkey
# 2005 Rooster
# 2006 Dog
# 2007 Pig
# 2008 Rat
# 2009 Ox
# 2010 Tiger
# 2011 Hare

# Write a program that reads a year from the user and displays the animal associated with that
# year. Your program should work correctly for any year greater than or equal to zero, not just
# the ones listed in the table.

year = int(input("enter year:"))
zodiac_index = (year - 2000) % 12

zodiac_animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]
zodiac_sign = zodiac_animals[zodiac_index]
print("zodiac sign is:",zodiac_sign)

# A particular cell phone plan includes 50 minutes of air time and 50 text messages for $15.00 a
# month. Each additional minute of air time costs $0.25, while additional text messages cost
# $0.15 each. All cell phone bills include an additional charge of $0.44 to support 911 call
# centres, and the entire bill (including the 911 charge) is subject to 5 percent sales tax.
# Write a program that reads the number of minutes and text messages used in a month from the
# user. Display the base charge, additional minutes charge (if any), additional text message
# charge (if any), the 911 fee, tax and total bill amount. Only display the additional minute and
# text message charges if the user incurred costs in these categories. Ensure that all of the
# charges are displayed using 2 decimal places.

BASE_CHARGE = 15.00
ADDITIONAL_MINUTE_CHARGE = 0.25
ADDITIONAL_TEXT_CHARGE = 0.15
nine11_FEE = 0.44
SALES_TAX_RATE = 0.05

minutes_used = int(input("Enter the number of minutes used: "))
text_messages_used = int(input("Enter the number of text messages used: "))
additional_minute_cost = max(0, minutes_used - 50) * ADDITIONAL_MINUTE_CHARGE
additional_text_cost = max(0, text_messages_used - 50) * ADDITIONAL_TEXT_CHARGE

subtotal = BASE_CHARGE + additional_minute_cost + additional_text_cost + nine11_FEE
sales_tax = subtotal * SALES_TAX_RATE
total_bill = subtotal + sales_tax
print("Base charge: $%.2f" % BASE_CHARGE)
if additional_minute_cost > 0:
    print("Additional minute charge: $%.2f" % additional_minute_cost)
if additional_text_cost > 0:
    print("Additional text message charge: $%.2f" % additional_text_cost)
print("911 fee: $%.2f" % nine11_FEE)
print("Sales tax: $%.2f" % sales_tax)
print("Total bill amount: $%.2f" % total_bill)

# The length of a month varies from 28 to 31 days. In this exercise you will create a program
# that reads the name of a month from the user as a string. Then your program should display
# the number of days in that month. Display “28 or 29 days” for February so that leap years are
# addressed.

mont  = input("enter full name of month(don't put space after month name):")
if mont.upper() == 'JANUARY' or mont.upper() == 'MARCH' or mont.upper() == 'MAY' or mont.upper() == 'JULY' or mont.upper() == 'AUGUST' or mont.upper() == 'OCTOBER' or mont.upper() == 'DECEMBER':
    print(mont," has 31 days")
elif mont.upper() == 'FEBRUARY':
    print("February has 28 or 29 days depending on the leap year")
else:
    print(mont,"has 30 days")

# Write a program that reads a date from the user and computes its immediate successor. For
# example, if the user enters values that represent 2013-11-18 then your program should display
# a message indicating that the day immediately after 2013-11-18 is 2013-11-19. If the user
# enters values that represent 2013-11-30 then the program should indicate that the next day is
# 2013-12-01. If the user enters values that represent 2013-12-31 then the program should
# indicate that the next day is 2014-01-01. The date will be entered in numeric form with three
# separate input statements; one for the year, one for the month, and one for the day. Ensure
# that your program works correctly for leap years.

year = int(input("Enter the year: "))
month = int(input("Enter the month(in numbers): "))
day = int(input("Enter the day: "))

leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if leap_year:
    days_in_month[2] = 29

if day < days_in_month[month]:
    next_year = year
    next_month = month
    next_day = day + 1
else:
    next_day = 1
    if month < 12:
        next_year = year
        next_month = month + 1
    else:
        next_year = year + 1
        next_month = 1
print("The day immediately after {}-{}-{} is {}-{}-{}.".format(year, month, day, next_year, next_month, next_day))

# In this exercise you will create a program that reads a letter of the alphabet from the user. If
# the user enters a ,e, i, o or u then your program should display a message indicating that the
# entered letter is a vowel. If the user enters y then your program should display a message
# indicating that sometimes y is a vowel, and sometimes y is a consonant. Otherwise your
# program should display a message indicating that the letter is a consonant.

vowels = ['a','e','i','o','u']
user_word = input("enter any letter from a - z :")
if user_word in vowels:
    print("entered letter",user_word,"is a vowel!")
elif user_word.upper() == 'Y':
    print("y is sometimes a vowel and sometimes a consonant")
else:
    print(user_word, "is a consonant")