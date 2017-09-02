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



number = "9,223,372,036,854,775,807"
cleanedNumber = ''

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)
print("The number is {} ".format(newNumber))

for state in ["not doing well","no more","a stiff","bereft of life"]:
    print("The parrot is "+ state)

for i in range(0, 100, 5): # third number is a step
    print(i)

for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("=======")