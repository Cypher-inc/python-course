import math
from tabnanny import check
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


point1 = Point()  # declaring the obj for the class
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x, point1.y)

point2 = Point()
point2.x = 30
print(point2.x)

# constructors


class Point:  # capitalise Name
    def __init__(self, x, y):  # constuctor
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
print(point1.x)


class Person:
    def __init__(self, name):  # name argument
        self.name = name

    def talk(self):
        print(self.name, 'can speak')


mike = Person('Mike Scott')
print(mike.name)
mike.talk()

alex = Person('Alex Sparrow')
alex.talk()

# n = int(input())


# hackerrank
# test = ''
# for x in range(1,n):
#     test += str(x)
# print(test)

# def swap_case(s):
#     for x in s:
#         if x in x.upper():
#             print(x.lower())
#         else:
#             print(x.upper())

# if __name__ == '__main__':
#     s = input()
#     swap_case(s)


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))

# # print(n)
# # print(arr)

# max1 = max(arr)
# arr.remove(max1)
# print(arr)
# max2 = max(arr)
# print(max2)
# # for x in arr:
# #     print(x)


# if __name__ == '__main__':
#     n = int(input())
#     integer_list = (map(int,input().split()))
# print(hash(integer_list))

#capitalise
# s = 'chris al'
# def solve(s):
#     l1 = s.split(' ')
#     # print(l1)
#     l2 = []
#     for x in l1:
#         l2.append(x.capitalize())
#         print(x.capitalize())
#         # l2 += x.capitalize()
#     # print(l2)
#     str1 = ' '.join(map(str, l2))
#     str1.join(l2)
#     return str1
    # return s.capitalize()

# discussion
# for x in s[:].split():
#         str1 = s.replace(x, x.capitalize())
# print(str1)


# s = input()


# for x in s:
#     print(x)


#     if checkAlpha:
#         continue
#     else:
#         if x.isalpha():
#             print('Alpha : TRUE')
#             checkAplha = True
#         if x.isdigit():
#             print("Digit: TRUE")
#             checkDigit = True
#         if x.isupper():
#             print('Upper: TRue')
#             checkUpper = True
#         if  x.islower():
#             print('Lower: TRue')
#             checkLower = True

# for x in s:
#     print(x)
#     if x.isalpha() or x.isdigit() or x.isupper() or x.islower():
#         print('TRUE')

# checkLower = False
# checkUpper = False
# checkDigit = False
# checkAlpha = False
# checkAlphaNum = False

# for x in s:
#     if x.isalnum():
#         print(True)
#         checkAlphaNum = True
#         break
# if not checkAlphaNum:
#     print(False)

# for x in s:
#     if x.isalpha():
#         print(True)
#         checkAlpha = True
#         break
# if not checkAlpha:
#     print(False)

# for x in s:
#     if x.isdigit():
#         print(True)
#         checkDigit = True
#         break
# if not checkDigit:
#     print(False)


# for x in s:
#     if x.islower():
#         print(True)
#         checkLower = True
#         break
# if not checkLower:
#     print(False)

# for x in s:
#     if x.isupper():
#         print(True)
#         checkUpper = True
#         break
# if not checkUpper:
#     print(False)

# print('''#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000'''.isalpha())


# list comprehension
# for i in range(1, 11):
#     print(i**2)

# square1 = [i**2 for i in range(1, 11)]
# print(square1)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

# l1 = []    
# for a in range(x+1):
#     for b in range(y+1):
#         for c in range(z+1):
#             # print(a,b,c)
#             if(a+b+c != n):
#                 l1.append([a,b,c])
# print(l1)


#text wrap
# import textwrap

# def wrap(string, max_width):
#     test = ''
#     test1 = ''
#     for x in string:
#         test1 +=x
#         if len(test1) == max_width:
#             test += test1+'\n'
#             test1 = ''
#     return test + test1       

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

#find a string
# def count_substring(string, sub_string):
#     string = string.replace(" ", "")
#     test = ''
#     count = 0
#     for x in string:
#         if x in sub_string:
#             test += x
#     for y in range(0,len(test)):
#         # print(test[y:y+len(sub_string)])
#         if test[y:y+len(sub_string)] == sub_string:
#             print(test)
#             count += 1
#     return count

#hackerrank discussion soln - usestartswith()
# def count_substring(string, sub_string):
#     count = 0
#     for x in range(len(string)):
#         if string[x:].startswith(sub_string):
#             print(string[x:])
#             count += 1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# print('WoW!ItSCoOWoWW'.count('oW'))

# print('ABCDCDC'.startswith('CDC'))

# finds only once
# str1 = ' wellcometopythonprogramingpython'
# subStr = 'python'

# print(str1.find(subStr))

# def findString(str1, subStr):
#     initial= str1.find(subStr)
#     final = len(subStr)
#     return str1[initial:initial+final]

# print(findString(str1,subStr))

#find the runner up
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     arr1 = arr[:]
#     comp1 = arr[0]
#     for x in arr :
#         # print(x)
#         if x > comp1:
#             comp1 = x
#     # print(comp1)        
#     for y in arr1:
#         # print(y)
#         if y != comp1:
#             continue
#         arr.remove(comp1)
#         # print(arr.remove(comp1))
#     comp2 = arr[0]       
#     for x in arr:
#         # print(x)
#         if x >= comp2:
#             comp2 = x           
#     print(comp2)        
    # print(arr)


#itertools.product()
# from itertools import product

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# t1 = tuple(list(product(A,B)))

# # print(' '.join(str(x) for x in t1))
# s1 = ''
# for x in t1:
#     s1 += ''.join(str(x)) + ' '
# print(s1)

#Nested list 

if __name__ == '__main__':
    nameDic = []
    scoreList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameDic.append(name)  
        scoreList.append(score)  

    print(nameDic)    
    print(scoreList)    

    for x in nameDic:
        print(x,y)

    # for x in sco
          