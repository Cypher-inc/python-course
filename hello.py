import math
from tkinter.tix import Tree
from matplotlib.pyplot import pink

from numpy import matrix, number

print('Hello World!')

# multiplication
print('*'*10)

# declaring Variable
price = 10
rating = 4.9
name = 'Kris'
isPublished = True

print(price)
# print(type(rating))
# print(type(name))
# print(type(isPublished))

# input
# name1 = input('What is your name? ')
# print('Hi',name1)

# name2 = input('What is your name? ')
# color = input('What is your fav color? ')
# print(name2,'likes',color)

# Clac age

currYr = 2022
dob = 2000

calcAge = 2022 - 2000

# dob1 = int(input('What yr were you born? '))
# month1 = int(input('What month were you born? '))
# calcAge1 = currYr - dob1

# print("Age is :",calcAge1)


# userWeight = int(input('What is your weight? '))

# caclWeight = userWeight * 2.2046

# print(caclWeight)

print('Hello My name jeff')

print("Hello My name jeff")

print('''
Hello,
My name jeff
 ''')

# strings
# course = 'Python for beginners'
# another = course[:] #used to copy a string
# print(course[0])
# print(course[-1])
# print(course[0:3])
# print(course[0:])
# print(course[:5])
# print(another)


# formated string
first = 'Jeff'
last = 'Goldman'

msg = f'{first} [{last}] is a coder'
print(msg)

# methods (functions that belong to objects)
course = 'python for beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course.capitalize())
print(course.find('b'))
print(course.replace('beginners', 'pros'))

# check if string exists in a var
checkIn = 'python' in course
print(checkIn)

# arethmatic operators

sum = 10 + 5
print('Sum is :', sum)

# power
print(10 ** 3)

# order for precedence
# exponentiation
# multiplication or division
# addition or subtraction

x = 10 + 3 * 2
print(x)

# round a number
x = 2.9
print(round(x))

print(abs(-23))

# cieling
y = 2.2
print(math.ceil(y))

z = 2.8
print(math.floor(z))

# if statements
# # if calcAge >= 20 :
# #     print('Can vote')

# dob1 = int(input('What yr were you born? '))
# month1 = int(input('What month were you born? '))
# # calcAge1 = currYr - dob1

# if month1 < 6 :
#     calcAge = 2022 - dob1
# elif month1 > 6:
#     calcAge = (2022 - dob1) - 1
# elif (month1 == 6):
#     day1 = int(input('What day were you born? '))
#     if(day1 >= 17):
#         calcAge = (2022 - dob1) - 1
#     else :
#         calcAge = 2022 - dob1

# print(calcAge)

# print(2022-dob1)
# isHot = 1
# if isHot:
#     print('yes')
# else:
#     print('no')


# if assign1
housePrice = 1000000

# userInputTrue = int(input('To continue ?'))
# userCredit = int(input("Is your credit good? "))

# if userCredit == 1:
#     print(f'${(housePrice * 10)/100} is the credit and the total price is ${housePrice + (housePrice * 10)/100}')
# else:
#     print(f'${(housePrice * 20)/100} is the credit and the total price is ${housePrice + (housePrice * 20)/100}')


# conditionl operators
userSal = 1
userCredit = 0

if userSal or userCredit:
    print('Eligible for loan')
else:
    print('NOT eligible for loan')

userName = 'Kris'
if len(userName) < 2:
    print('Length should be altleast 3! ')
elif len(userName) >= 6:
    print('Length cannot be over 50!')
else:
    print('Name looks good!')


# userWeight = float(input('Enter user weight? '))
# userUnit = input("Do you prefer Kg or Lb? ")

# if userUnit.lower() == 'kg':
#     print(round(userWeight * 0.453592))
# elif userUnit.lower() == 'lb':
#     print(round(userWeight * 2.20462))
# print(userWeight)

count = 0

# while True:
#     i = int(input('Do you want to continue? '))
#     if i:
#         count += 1
#         continue
#     else:break
# print(count)

# while True:
#     i = int(input('Enter a number? '))
#     if i==5:
#         print('You guessed the number!')
#         break
#     else:continue

# shapes using while

# i=5
# while i>=1:
#     print('*'*i)
#     i=i-1

# i=0
# while i<=5:
#     print('*'*i)
#     i=i+1

# Car game
# started = False
# stopped = False
# while True:
#     startInput = input('>')
#     if startInput.lower() == "start":
#         if started == True:
#             print('Warning: Car has ALREADY started!')
#         else:
#             print('Car has started!')
#             started = True
#     elif startInput.lower() == "stop":
#         if stopped == True:
#             print("Warning: Car has ALREADY stopped")
#         else:
#             print("Car has stopped")
#             stopped = True
#     elif startInput.lower() == "quit":
#         break
#     else:
#         print("I don't understand that..")

# for loop

# for x in 'python':
#     print(x)

# arr = ['Kris','John','Mike','James']
# for names in arr:
#     print(names)

# #range
# for items in range(10):
#     print(items)

# for items in range(2,11):
#     print(items)

# steps
# for items in range(0,10,2):
#     print(items)

# nested loop
# print('Nested loops')
# for x in range(1,6):
#     for y in range(1,6):
#         print(f'({x},{y})')

# challenge
numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     print('x'*x)

# for y in numbers:
#     print('x',y)

# names = ['john', 'Bane', 'judy', 'Kimmy']
# print(names[0])
# print(names[-1])
# print(names[:3])
# print(names[2:])

# #find largest num
# num1 = [-9, 5, -8, 3, 7, 2]

# samp = num1[0]
# for x in num1:
#     if x < samp:
#         samp = x
# print('Smallest',samp)

# for x in num1:
#     if x > samp:
#         samp = x
# print('Largest',samp)


# 2d list
print('matrix')
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix1[0][0])

# for x in matrix1:
#         print(x)

for x in matrix1:
    for y in x:
        print(y)


# list methods

numbersList = [5, 3, 6, 8, 2, 1, 8]

numbersList.append(12)
print(numbersList)

# adding number in the middle of a list
numbersList.insert(3, 7)
numbersList.insert(2, 9)
print(numbersList)

numbersList.pop()
print(numbersList)

print(numbersList.index(5))
# print(numbersList[0])

# count
print(numbersList.count(8))

# sort
numbersList.sort()
print(numbersList)

# reverse sort list
numbersList.sort()
numbersList.reverse()
print(numbersList)

# copy
numbersList2 = numbersList.copy()
numbersList3 = numbersList

print(numbersList2)
numbersList.pop()
numbersList.pop()
print(numbersList)
print(numbersList2)
print(numbersList3)  # Also changes

numbersList = [5, 3, 6, 8, 5, 2, 1, 8, 3]
# for x in numbersList:
#     if numbersList.count(x) < 2:
#         print(x)
#     if numbersList.count(x) > 1:
#         print('Duplicate',x)

# print( 3 in numbersList)

y = []
for x in numbersList:
    if x not in y:
        y.append(x)

    # if x in y:
    #     print(x)
print("Removing duplicates:", y)

# tuples
# they cannot be changed!
# we use parenthesis to denote tuples

numbersTup = (3, 6, 9, 12)

print(numbersTup.count(3))
print(numbersTup[0])
print(numbersTup.index(9))  # gives the index of a number

# numbersTup[0] = 1 #Gives error

# unpacking
cord1 = (1, 2, 3)

x, y, z = cord1  # like destructuring in js
print(x, y, z)

# dictionary - key, value pairs

customer1 = {
    "name": "Mike",
    "age": 15,
    "isVerified": True
}

print(customer1)
print(customer1['name'])
print(customer1.get('NAME'))  # does not throw an error
print(customer1.get('bd', '12 Dec 2001'))  # default values

customer1['name'] = "Floyd"
print(customer1['name'])

phoneNo = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four'
}

# phone = input('Phone: ')
# # phoneList1 = phone.split()
# # print(phoneList1)
# print(phone)

# a,b,c,d = phone
# print(a,b,c,d)
# print(phoneNo[1],phoneNo[2],phoneNo[3],phoneNo[4])

# phoneList = [1,2,3,4]

# phoneWordList = []
# for x in phone:
#     # print(x)
#     phoneWordList.append(phoneNo[int(x)])
#     # print(phoneNo[int(x)])

# a,b,c,d = phoneWordList
# print(a,b,c,d)
# print(phoneWordList)

# msg = input(">")
# words = msg.split(" ")
# emojis = {
#     ":)": "😀",
#     ":(": "😔",
#     ":/": "😕"
# }

# # print(msg[-2:])
# # print(msg[:-2])
# print(msg[:-2] + emojis[words[-1]])

# for x in words:
# print(x[-2:])

# mystr = "my name jeff :)"
# print(mystr[-2:])

# functions

print('Functions:')


def helloWorld():
    print('Hi there')
    print("Welcome aboard!")


helloWorld()

# passing values


def helloWorld(firstname, lastname):
    print('Hi there,', firstname, lastname)
    print("Welcome aboard!")


helloWorld('Kris', 'D')

# default values


def helloWorld(name='NoName'):
    print('Hi there,', name)
    print("Welcome aboard!")


helloWorld()

# keyword argument


def helloWorld(firstname, lastname):
    print('Hi there,', firstname, lastname)
    print("Welcome aboard!")


helloWorld(lastname='Smith', firstname="Mike")

# return


def helloWorld():
    return "Hello World!"


print(helloWorld())


def squareFunc(num):
    print(num**2)


# by refault all functions retruns none so print(squareFunc(9)) while alredy
# has a print will return none
print(squareFunc(9))


def emojiConverter(msg):
    words = msg.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😔",
        ":/": "😕"
    }
    print(msg[:-2] + emojis[words[-1]])

# textInput = input('> ')
# emojiConverter(textInput)


# exception
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income/age
#     print("age:",age, "income:",risk)
# except ZeroDivisionError:
#     print('Age cannot be zero!')
# except ValueError:
#     print('Invalid Value')

# classes
# complex types: List, Dictonary, classes

class Point:  # capitalise Name
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point() #declaring the obj for the class
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)

point2 = Point()
point2.x = 30
print(point2.x)

#constructors
class Point:  # capitalise Name
    def __init__(self, x, y): #constuctor
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10,20)
print(point1.x)

class Person : 
    def __init__(self, name): #name argument
        self.name = name
    def talk(self):
        print(self.name,'can speak')

mike = Person('Mike Scott')
print(mike.name)
mike.talk()

alex = Person('Alex Sparrow')
alex.talk()