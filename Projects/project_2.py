# Beginning: create variables
spring_points = 0
fall_points = 0

input("Welcome to my quiz! There are 9 questions below, answer as honestly as possible! Good Luck!  ")

answer = input("Would you rather have A: lemonade or B: hot cocoa?   ")
if answer == "A" or answer == "a":
    spring_points += 1
elif answer == "B" or answer == "b":
    fall_points += 1
    
print(" ")

answer = input ("Would you rather A: go shopping or B: go swimming?   ")
if answer == "A" or answer == "a":
    fall_points += 1
    spring_points += 0.5
elif answer == "B" or answer == "b":
    spring_points += 1
    fall_points += 0.5

print(" ")

answer = input ("Do you like A: Peaches or B: Apples better?   ")
if answer == "A" or answer == "a" and spring_points > 2:
    spring_points += 1
elif answer == "B" or answer == "b" and fall_points > 2:
    fall_points += 1
elif answer == "A" or answer == "a":
    spring_points += 0.5
elif answer == "B" or answer == "b":
    fall_points += 0.5

print(" ")

answer = input ("Do you like A: darker colors or B: lighter colors?   ")
if answer == "A" or answer == "a":
    fall_points += 1
elif answer == "B" or answer == "b":
    spring_points += 1
elif answer == "A" or answer == "a" and fall_points > 2.5:
    fall_points += 2
elif answer == "B" or answer == "b" and spring_points > 2.5:
    spring_points += 2

print(" ")

answer = input ("Would you rather A: get a cat or B: get a dog?   ")
if answer == "A" or answer == "a":
    fall_points += 1
elif answer == "B" or answer == "b":
    spring_points += 1

print(" ")

answer = input ("Would you rather A: go outside to the park or B: stay inside and watch a show?   ")
if answer == "A" or answer == "a":
    spring_points += 1
    fall_points += 0.5
elif answer == "B" or answer == "b":
    fall_points += 1
    spring_points += 0.5

print(" ")

answer = input ("Do you prefer to listen to A: an entire album or B: your own custom playlist?   ")
if answer == "A" or answer == "a":
    spring_points += 1
    fall_points += 0.5
elif answer == "B" or answer == "b":
    fall_points += 1
    spring_points += 0.5

print(" ")

answer = input ("Would you prefer to get A: new headphones or B: new jewelry?   ")
if answer == "A" or answer == "a" and fall_points > 4:
    fall_points += 1
elif answer == "B" or answer == "b" and spring_points > 4:
    spring_points += 1
else:
    spring_points += 0.5
    fall_points += 0.5

print(" ")

answer = input ("Gold or Silver?   ")
if answer == "gold" or answer == "Gold":
    fall_points += 1
    spring_points += 0.5
elif answer == "Silver" or answer == "silver":
    fall_points += 0.5
    spring_points += 1

# end of quiz

print(" ")
input("Thank you for taking my quiz! Are you ready to see your results? ")
print(" ")

if spring_points > fall_points:
    print("You are more spring person! You thrive in a more spring environment.")
    print("Thanks again, Bye!")
elif fall_points > spring_points:
    print("You are more of a fall person! You thrive in a more fall environment.")
    print("Thanks again, Bye!")
elif spring_points == fall_points:
    print("You enjoy both fall and spring! Maybe a winter or summer person?")
    print("Thanks again, Bye!")

print(" ")
