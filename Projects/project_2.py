# Beginning: create variables and zero out
spring_points = 0
summer_points = 0
fall_points = 0
winter_points = 0

print(" ")
input("Welcome to my quiz! There are 10 questions below, answer with a letter when you type your answer! Good Luck!  ")
print(" ")
# Question 1
answer = input("Would you rather have A: lemonade, B: tea, C: hot cocoa, or D: soda?   ")
if answer == "A" or answer == "a":
    spring_points += 1
elif answer == "B" or answer == "b":
    fall_points += 1
elif answer == "C" or answer == "c":
    winter_points += 1
elif answer == "D" or answer == "d":
    summer_points += 1
else:
    print("There was an error, sorry.")
    
print(" ")
# Question 2
answer = input ("Would you rather A: go shopping, B: go swimming or C: stay at home?   ")
if answer == "A" or answer == "a":
    fall_points += 1
    spring_points += 0.5
elif answer == "B" or answer == "b":
    summer_points += 1
    fall_points += 0.5
elif answer == "C" or answer == "c":
    winter_points += 1
else:
    print("There was an error, sorry.")

print(" ")
# Question 3
answer = input ("Do you like A: Peaches, B: Cherries, C: Apples or D: none?   ")
if answer == "A" or answer == "a":
    spring_points += 1
elif answer == "B" or answer == "b":
    summer_points += 1
elif answer == "C" or answer == "c":
    fall_points += 1
elif answer == "D" or answer == "d":
    winter_points += 1
else:
    print("There was an error, sorry.")

print(" ")
# Question 4
answer = input ("Do you like A: darker colors B: lighter colors, C: cooler colors or D: warmer colors?   ")
if answer == "A" or answer == "a":
    winter_points += 1
elif answer == "B" or answer == "b":
    spring_points += 1
elif answer == "C" or answer == "c":
    fall_points += 0.5
    winter_points += 0.5
elif answer == "D" or answer == "d":
    spring_points += 0.5
    summer_points += 0.5
else:
    print("There was an error, sorry.")

print(" ")
# Question 5
answer = input ("Would you rather A: get a cat, B: get a dog C: neither?   ")
if answer == "A" or answer == "a":
    fall_points += 1
elif answer == "B" or answer == "b":
    spring_points += 1
elif answer == "C" or answer == "c":
    winter_points += 0.5
    summer_points += 0.5
else:
    print("There was an error, sorry.")

print(" ")
# Question 6
answer = input ("Would you rather A: go outside to the park, B: hang out with friends, C: stay inside and watch a show?   ")
if answer == "A" or answer == "a":
    summer_points += 1
    spring_points += 0.5
elif answer == "B" or answer == "b":
    spring_points += 1
    summer_points += 0.5
elif answer == "C" or answer == "c":
    fall_points += 1
    winter_points += 1
else:
    print("There was an error, sorry.")

print(" ")
# Question 7
answer = input ("Do you prefer to listen to A: an entire album, B: your own custom playlist or C: rather not listen to music?   ")
if answer == "A" or answer == "a":
    summer_points += 1
elif answer == "B" or answer == "b":
    fall_points += 0.5
    spring_points += 0.5
elif answer == "C" or answer == "c":
    winter_points += 2
else:
    print("There was an error, sorry.")

print(" ")
# Question 8
answer = input ("Would you prefer to get A: new headphones, B: new jewelry, C: new clothes or D: new shoes?   ")
if answer == "A" or answer == "a":
    fall_points += 1
elif answer == "B" or answer == "b":
    spring_points += 1
elif answer == "C" or answer == "c":
    summer_points += 1
elif answer == "D" or answer == "d":
    winter_points += 1
else:
    print("There was an error, sorry.")

print(" ")
# Question 9
answer = input ("Gold or Silver?   ")
if answer == "gold" or answer == "Gold":
    summer_points += 1
    spring_points += 1
elif answer == "Silver" or answer == "silver":
    fall_points += 1
    winter_points += 1
else:
    print("There was an error, sorry.")

print(" ")
# Question 10
answer = input ("Would you rather A: eat with friends or B: eat by yourself or C: depends?  ")
if answer == "A" or answer == "a":
    summer_points += 1
elif answer == "B" or answer == "b":
    winter_points += 1
elif answer == "C" or answer == "c":
    fall_points += 0.5
    spring_points += 0.5
else:
    print("There was an error, sorry.")

# end of quiz

print(" ")
input("Thank you for taking my quiz! Are you ready to see your results? ")
print(" ")
# Results
if spring_points > fall_points and spring_points > winter_points and spring_points > summer_points:
    print("You are more spring person! You thrive in a more spring environment.")
    print("Thanks again, Bye!")
elif fall_points > spring_points  and fall_points > winter_points and fall_points > summer_points:
    print("You are more of a fall person! You thrive in a more fall environment.")
    print("Thanks again, Bye!")
elif summer_points > fall_points and summer_points > winter_points and summer_points > spring_points:
    print("You are more of a summer person! You thrive in a more summer environment.")
    print("Thanks again, Bye!")
elif winter_points > fall_points and winter_points > spring_points and winter_points > summer_points:
    print("You are more of a winter person! You thrive in a more winter environment.")
    print("Thanks again, Bye!")
else:
    print(r"Your quiz was unsuccessful. Please try again. (You might have not answered the questions right.)")

print(" ")
