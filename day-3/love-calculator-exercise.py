# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇

#sums matching letters from both names with letters from word true
true_name1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
true_name2 = name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

#prints out a number of matches for each letter
print(f"T occurs {name1.count('t') + name2.count('t')} times")
print(f"R occurs {name1.count('r') + name2.count('r')} times")
print(f"U occurs {name1.count('u') + name2.count('u')} times")
print(f"E occurs {name1.count('e') + name2.count('e')} times")

#sums up matching letters from both given names against the word TRUE, converts result into string and prints it out
total_true = str(true_name1 + true_name2)
print(f"Total = {total_true}")

#sums matching letters from both names with letters from word love
love_name1 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
love_name2 = name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

print(f"L occurs {name1.count('l') + name2.count('l')} times")
print(f"O occurs {name1.count('o') + name2.count('o')} times")
print(f"V occurs {name1.count('v') + name2.count('v')} times")
print(f"E occurs {name1.count('e') + name2.count('e')} times")

#sums up matching letters from both given names against the word LOVE, converts result into string and prints it out
total_love = str(love_name1 + love_name2)
print(f"Total = {total_love}")

#sums up end result and prints out final love score
love_score = total_true + total_love #error because strings and integers can't be compared
print(f"Love Score = {love_score}")

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")