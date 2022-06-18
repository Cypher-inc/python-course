import math

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

if userSal and userCredit:
    print('Eligible for loan')
else:
    print('NOT eligible for loan')



