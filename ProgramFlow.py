# for i in range(1, 12):
#     print("No {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

# name = input("Please enter your name: ")
# age = int(input("How old are your, {0}? ".format(name)))
# print(age)
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years ".format(18 - age))


# print("Please guess a number between 1 and 10")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You guessed it on the first try!")

# age = int(input("How old are your? "))
# if age >= 16 and age <= 65:
# if 15 < age < 66:
#     print("Have a good day at work")

# if age < 16 or age > 65:
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")

# if (some_condition) or (some_weird_function_that_does_stuff()):
# do something
# ****************************

# x = input("Please enter some text ")
# if x:
#     print("You entered {0} ".format(x))
# else:
#     print("You did not enter anything")

# parrot = "Norwegian Blue"
# letter = input("Enter a letter: ")
#
# if letter in parrot:
#     print("{0} is in the word".format(letter))
# else:
#     print("{0} is not in the word".format(letter))

# ****  challenge   -  Write a small program to ask for name and age.
# When both values have been entered, check if the person is the right age to go
# on a 18-30 holiday.  IF they are, welcome them. if not politely refuse.

# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
#
# if 17 < age < 31:
#     print("Welcome to your holiday getaway!")
# else:
#     if age < 18:
#         print("{0}, you must be 18 to go on this holiday".format(name))
#     else:
#         print("{0}, you are over age to go on this holiday".format(name))


# ************************
# for i in range(1, 20):
#     print("i is now {}.".format(i))
#
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])
#
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {} ".format(newNumber))

# ******************

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number is {} ".format(newNumber))
#
# for state in ["not doing well","no more","a stiff","bereft of life"]:
#     print("The parrot is "+ state)
#
# for i in range(0, 100, 5): # third number is a step
#     print(i)
#
# for i in range(1,13):
#     for j in range(1,13):
#         print("{1} times {0} is {2}".format(i, j, i*j))
#     print("=======")

# ************************
# shoppingList = ["Milk","Rice","pasta","eggs","spam","bread","peanut butter"]
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy " + item)
# print(" ")
# shoppingList = ["Milk","Rice","pasta","eggs","spam","bread","peanut butter"]
# for item in shoppingList:
#     if item == 'spam':
#         break
#     print("Buy " + item)
#
#
# nastyFoodItem = " "
# meal = ["egg", "bacon", "spam", "sausages"]
#
# for item in meal:
#     if item == "spam":
#         nastyFoodItem = item
#         break
# else:
#     print("I'll have a plate of that, then , please")
#
# if nastyFoodItem == 'spam':
#     print("Can't I have anything without spam in it")
#
# **********************
# Augmented assignment     += number[i]
#
# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in "0123456789":
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print("The number is {} ".format(newNumber))
#
# x = 23
# x += 1
# print(x)
#
# x -= 4
# print(x)
#
# x *= 5
# print(x)
#
# x /= 4
# print(x)
#
# x **= 2
# print(x)
#
# x %= 60
# print(x)

# **********
# Challenge
#
# ipAddress = input("Please enter an IP Address: ")
# numbers = " "
# segment = 1
# segmentLength = 0
# character = " "
#
# for character in ipAddress:
#     if character == ".":
#         print("The number(s) entered are {0}".format(numbers))
#         print("There are {0} numbers in segment {1} ".format(segmentLength, segment))
#         print(" ")
#         segment += 1
#         segmentLength = 0
#         numbers = " "
#     else:
#         numbers += character
#         segmentLength += 1
# #unless final character was a . then we haven't printed the last segment
#
# if character != ".":
#
#     print("The number(s) entered are {0}".format(numbers))
#     print("There are {0} numbers in segment {1}".format(segmentLength, segment))

# Simplified above code  taking out lines with the /:

# ipAddress = input("Please enter an IP Address: ")
# if ipAddress[-1] != ".":
#     ipAddress += "."
# numbers = " "
# segment = 1
# segmentLength = 0
# /character = " "

# for character in ipAddress:
#     if character == ".":
#         print("The number(s) entered are {0}".format(numbers))
#         print("There are {0} numbers in segment {1} ".format(segmentLength, segment))
#         print(" ")
#         segment += 1
#         segmentLength = 0
#         numbers = " "
#     else:
#         numbers += character
#         segmentLength += 1
# unless final character was a . then we haven't printed the last segment

# /if character != ".":
#
#     /print("The number(s) entered are {0}".format(numbers))
#     /print("There are {0} numbers in segment {1}".format(segmentLength, segment))

# **************
# While loops

# for i in range(10):
#     print("i is now {0}".format(i))
#
# i = 0   -- same as above
# while i < 10:
#     print("i is now {0}".format(i))
#     i += 1

# availableExits = ['east', "west", "north", "south"]
#
# chosenExit = ""
# while chosenExit not in availableExits:
#     chosenExit = input("Please choose a direction: ")
#     if chosenExit == "quit":
#         print("Game Over")
#         break
# else:
#     print("aren't you glad you got out of there")

# ********************
# random number generator - in a module (external object) have to import it
# Challenge to make sure the program below to
import random
highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {0}:".format(highest))
guess = 0
counter = 0
while guess != answer:
    guess = int(input())
    counter += 1
    if counter == 5:
        print("Sorry, You ran out of guesses")
        break
    if guess == 0:
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("You guessed correctly")



