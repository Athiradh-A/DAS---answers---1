#Write a program that get information from the user and displays the following information:
#a) Your name
#b) Your address, with city, state and ZIP
#c) Your Mobile Number
#d) Your college major

name = input("enter name:")
address = input("enter address:")
city = input("enter city and state(seperated by commas):")
state = int(input("enter zip code:"))
mobile = int(input("enter mobile number:"))
colge = input("enter college major:")
print(name,address,city,state,mobile,colge,sep=":::")

#A company has determined its annual profit is typically 27% of total sales. Write a program
#that asks the user to enter the projected amount of total sales, and display the profit that will
#be made from that amount. 

sales = int(input("enter total sales:"))
tot_profit = 0.27 * sales
print("tot profit:",tot_profit)

#Write a program that reads an integer and determines and prints whether it’s odd or even.
#Hint: Use modulus operator.

integer = int(input('Enter number:'))
if integer % 2 == 0:
    print("number is even")
else:
    print("number is odd")

#Write a program that calculates the total amount of a meal purchased at a restaurant. The
#program should ask the user to enter the charge for the food, then calculate the amounts of a
#17 percent tip and 6.5 percent sales tax. Display each of these amounts and total.

price = int(input('enter amount in bill:'))
tip = 0.17 * price
serv_tax = 0.065 * price
print('total:',tip + serv_tax + price)
print("Please leave tip:",int(tip)," and service tax:",serv_tax)

#A cookie recipe calls for the following ingredients:
#a) 1.5 cups of sugar
#b) 1 cup of butter
#c) 2.75 cups of flour
#The recipe produces 10 cookies with this amount of the ingredients. Write a program that
#asks the user how many cookies he or she wants to make, then displays the number of cups
#of each ingredient needed for the specified number of cookies.

sug = .15
butter = .1 
flour = 0.275
cookies = int(input("enter number of cookies you want:"))
print("ingredients for",cookies," number of cookies")
print("sugar:",sug*cookies," butter:",butter*cookies," flour:",int(flour*cookies))

#Last month, Mr. A purchased stock in XYZ Software, Inc. Here are the details of the purchase:
# a) The number of shares that A purchased was 3500.
# b) When A purchased the stock, he paid $50.00 per share.
# c) A paid his stockbroker a commission that amount to the 3.5 percent of the amount he paid for the stock
#Two weeks later, A sold the stock. Here are the details of the sale:
# a) The number of shares that A sold was 3500
# b) He sold the stock for $53.75 per share
# c) He paid his stockbroker another commission that amount to 3.5 percent of the amount he received for the stock.
#Write a program that displays the following information:
# a) The amount of money A paid for the stock.
# b) The amount of commission A paid his broker when he bought the stock.
# c) The amount for which A sold the stock.
# d) The amount of commission A paid his broker when he sold the stock.
# e) Displays the amount of money that A had left when he sold the stock and paid his broker (both times).
#    If this amount is positive, then A made a profit. If the amount is negative, the A lost money.

stock_price = 3500*50
print("total stock price:",stock_price)
commsn = stock_price * 0.035
print("commision to broker:",int(commsn))
print("money left:",stock_price - commsn)

new_price = 3500*53.75
print("total sell price:",new_price)
commsn = new_price * 0.035
print("commision to broker",int(commsn))
print("money left:",new_price - commsn)

#A vineyard owner is planting several new rows of grapevine, and needs to know how many
#grapevines to plant in each row. She has determined that after measuring the length of a
#future row, she can use the following formula to calculate the number of vines that will fit in
#the row, along with the trellis end-post assemblies that will need to be constructed at each
#end of the row.
#Where,
# is the number of grapevines that will fit in the row.
# is the length of the row, in feet.
# is the amount of space, in feet, used by an end-post assembly.
# is the space between the vines, in feet.
#Write the program that makes the calculation for the vineyard owner. The program should
#ask the user to input the following:
# i) The length of the row, in feet
# ii) The amount of space used by an end-post assembly, in feet
# iii) The amount of space between the vines, in feet
#Once the input received, the program should calculate and display the number of
#grapevines that will fit in the row.

row_length = int(input("enter length of row(In feet):"))
end_post = int(input("enter amount of space used by the end-post(in feet):"))
space_between = int(input("enter space between grapevines:"))

num_of_vines = (row_length -2 * end_post)/space_between
print("the number of grapevines is :",int(num_of_vines))

#Write a program that asks the user to enter the amount of a purchase and the desired number
#of payment instalments. The program should add 6 percent to the amount to get the total
#purchase amount, and then divide it by the desired number of installments, then display
#message telling the user the total amount of the purchase and how much each instalment will cost.

payment = int(input("enter amount of purchase:"))
install = int(input("enter number of installments:"))

added_install = payment * 0.06 + payment
installement_cost = added_install / install 
print("total new installement:",added_install)
print("Cost of one installements:",installement_cost)

#Design and implement an interactive program that reads an amount in rupees as an integer
#and determines and prints the minimum number of bills of Rs. 50, Rs. 20, Rs. 10, Rs. 5, and
#Rs. 1 denominations in it. For example, if the amount is Rs. 179, your program should print
#that it consists of three 50, one 20, zero 10, one 5, and four 1 bills.

amount = int(input("enmter amount in rupees:"))
fifty_notes = amount // 50 
amount %= 50 

twnety_notes = amount // 20 
amount %= 20

ten_bills = amount // 10 
amount %= 10 

one_bill = amount
print("fifty notes:",fifty_notes,"twenty notes:",twnety_notes,"ten notes:",ten_bills,
"one notes:",one_bill,sep="\n")

#Write a program that asks for your height in feet and inches and your weight in pounds.
#Report your BMI (Body Mass Index). To calculate the BMI, first convert your height in feet
#and inches to height in only inches. Convert your height in inches to your height in meters by
#multiplying by 0.0254. Then, convert your weight in pounds into your mass in kilograms by
#dividing by 2.2.

height = float(input("enter height (in feet):"))
weight = float(input("enter weight (in pounds):"))

new_height = height * 0.3048
new_weight = weight * 0.453592

bmi = new_weight / (new_height ** 2)
formatted_value = "{:.2f}".format(bmi)
print("BMI --",formatted_value)

#Write a program to convert the length of the rope in centimeter to
# a) inch
# b) foot
# c) yard
# d) mile
# e) kilometer
#Note: Print the results with five decimal approximation.

value = float(input("enter length of rope(In cm):"))
inch = value / 2.54
foot = value / 30.48
yard = value / 91.44
mile = value / 160934
kilom = value / 100000

print("values:",value,inch,foot,yard,mile,kilom)

#Write a program that asks the user for the number of males and the number of females
#registered in the class. The program should display the percentage of males and females in the class.
#Hint: Suppose there are 24 males and 26 females, percentage of males can be calculated as .

males = int(input("enter number of males:"))
femal = int(input("enter number of females:"))
total = males + femal

percent_males = males / total 
percent_femal = femal / total 
print("percntage of males :: females - ",percent_males*100,percent_femal*100)

#Write a program to find simple interest and compound interest. Get the required details from
#the user (i.e) principle, rate of interest, number of years.

principal = int(input("enter principal amount:"))
time = int(input("enter time(in years)"))
rate = int(input("enter rate of interest:"))

simple = (principal * time * rate) / 100 

compound = principal * (1 + rate/100) ** 2
print("simple interest:",simple,"compound interest:",int(compound))

#Write a program to get radius as input from the user and print the following results with
#three decimal approximation
# a) Diameter
# b) Area
# c) Circumference of the circle
#Hint: Use value of pi as 3.1415927

radius = float(input("enter radius:"))
diameter = radius * 2
area = 3.1415297 * (radius**2)
circumf = 2 * 3.1415297 * radius
print("diameter:",diameter,"area:",area,"circumference:",circumf,sep='\n')

#Write a program to calculate the speed, get distance travelled in kilometers and time in
#hours, Convert the speed in km/hr to m/s.

dist = int(input("enter distance (in km):"))
time = int(input("enter time (in hours):"))
speed = dist / time
new_speed = speed * (5/18)
print("speed :",new_speed)

#Given an airplane’s acceleration a and take-off speed v, you can compute the minimum
#runway length needed for an airplane to take off using the following formula:length = v**2/ 2a
#Write a program that prompts the user to enter in meters/second (m/s) and the acceleration
#in meters/second squared and displays the minimum runway length.

velocity = int(input("enter velocity(in m/s):"))
accele = int(input("enter takeoff acceleration(in m/s2):"))

run_length = (velocity**2) / (2*accele)
print("runway length:",run_length)

#The US Census Bureau projects population based on the following assumptions.
# i) One birth every 7 seconds
# ii) One death every 13 seconds
# iii) One new immigrant every 45 seconds
#Write a program to display the population of the next year. Assume the current population
#is 312032486 and one year has 365 days.

current_pop = 312032486
secons = 31536000
birth = 1 / 7
deaths = 1 / 13
immgr = 1 / 45
net_pop = (birth + deaths + immgr) * float(secons)
next_pop = current_pop + net_pop

print("next year population:",next_pop)

#Write a program that reads a positive integer, , from the user and then displays the sum of all
#of the integers from to . The sum of the first positive integers can be computed using this
#formula:

number = int(input("enter POSITIVE integer:"))
sum_number = (number * (number+1)) // 2
print("sum from 1 to n:", sum_number)

#In many jurisdictions a small deposit is added to drink containers to encourage people to
#recycle them. In one particular jurisdiction, drink containers holding one liter or less have a
#$0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.
#Write a program that reads the number of containers of each size from the user. Your
#program should continue by computing and displaying the refund that will be received for
#returning those containers. Format the output so that it includes a dollar sign and always
#exactly two decimal places.

small_bottle = int(input("enter amount of small bottles(less than one litre):"))
large_bottle = int(input("enter amount of large bottles(more than one litre):"))

amt_small = small_bottle * 0.10
amt_large = large_bottle * 0.25
total_ref = amt_small + amt_large

print('total refund for small bottles:${:.2f}'.format(amt_small))
print('total refund for large bottles:${:.2f}'.format(amt_large))
print("total refund:{:.2f}".format(total_ref))

#In the United States, fuel efficiency for vehicle is normally expressed in miles-per-gallon
#(MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km).
#Create a program that reads a value from the user in American units and displays the
#equivalent fuel efficiency in Canadian Units.

eff = float(input("enter fuel efficieny (in miles per gallon):"))
kmph = eff * 0.425144
print("MPG unit in Canadian units:",kmph)
