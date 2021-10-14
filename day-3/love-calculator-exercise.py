# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
true_name1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
true_name2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

print(f"T occurs {name1.count('t') + name2.count('t')} times")
print(f"R occurs {name1.count('r') + name2.count('r')} times")
print(f"U occurs {name1.count('u') + name2.count('u')} times")
print(f"E occurs {name1.count('e') + name2.count('e')} times")

total_true = true_name1 + true_name2
true_str = str(print(f"Total = {total_true}"))

love_name1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
love_name2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

print(f"T occurs {name1.count('l') + name2.count('l')} times")
print(f"R occurs {name1.count('o') + name2.count('o')} times")
print(f"U occurs {name1.count('v') + name2.count('v')} times")
print(f"E occurs {name1.count('e') + name2.count('e')} times")

total_love = love_name1 + love_name2
love_str = str(print(f"Total = {total_love}"))

love_score = print(f"Love Score = {true_str + love_str}")

print(f"Your score is {total_true + total_love}.")