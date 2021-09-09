# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int=int(age)
year_of_birth = 2021 - age_int 
year_of_death = year_of_birth + 90

years_left = year_of_death - year_of_birth - age_int

weeks_left = years_left * 52

days_left = years_left * 365

print(f"You have roughly {years_left} years to live, which is {weeks_left} weeks or {days_left} days. Use them wisely!")

#print(years_left)
#print(weeks_left)
#print(days_left)
