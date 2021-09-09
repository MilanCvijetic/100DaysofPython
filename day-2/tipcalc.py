#Write a simple tip calculator:
#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12
#Round the result to 2 decimal places = 33.60

print ("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_splitting = int(input("How many people are splitting the bill? "))

end_result = (total_bill + ((tip_percentage / 100) * total_bill))/people_splitting 
cashmoney = '${:,.2f}'.format(end_result)
print(f"Each person should pay {cashmoney}")