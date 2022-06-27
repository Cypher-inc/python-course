
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

# capitalise
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


# text wrap
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

# find a string
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

# hackerrank discussion soln - usestartswith()
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

# find the runner up
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


# itertools.product()
# from itertools import product

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# t1 = tuple(list(product(A,B)))

# # print(' '.join(str(x) for x in t1))
# s1 = ''
# for x in t1:
#     s1 += ''.join(str(x)) + ' '
# print(s1)

# Nested list

# if __name__ == '__main__':
#     nameDic = []
#     scoreList = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         nameDic.append(name)
#         scoreList.append(score)

#     print(nameDic)
#     print(scoreList)

#     for x in nameDic:
#         print(x,y)


# string formatter

# def print_formatted(number):
#     for x in range(1,number+1):
#         print(f'{x} {oct(x)} {hex(x)} {bin(x)} ')

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)


# Row,Col = map(int,input().split(' '))

# print(Row,Col)
# for x in range(1,Row,2):
#     print(('.|.'*x).center(Col,'-'))
# print(('WELCOME').center(Col,'-'))
# for x in reversed(range(1,Row,2)):
#     print(('.|.'*x).center(Col,'-'))


# alphabet rangoli
# def print_rangoli(size):
#     for x in range(1, (size*2)-1, 2):
#         print(('-'+'a-'*x).center((size*3), '-'))
#     # for x in range(1, (size*2)-1, 2):
#     #     x = ('a'+'-a'*x)
#     # print(x)
#     # print(('-'*x).center((size*2)+1,'a'))
#     for x in reversed(range(1, (size*2)-1, 2)):
#         print(('-'+'a-'*x).center((size*3), '-'))


# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)


# import string
# alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))


# from itertools import permutations
# string1,num1 = map(str,input().split(' '))

# list1 = list(permutations(string1,int(num1)))

# str1 = ''
# count = 0
# list2= []
# for x in list1:
#     # print(x)
#     for y in x:
#         str1+=y
#         count += 1
#         if count == int(num1):
#             list2.append(str1)
#             count = 0
#             str1 = ''
# sortedList = sorted(list2)
# for x in  sortedList:
#     print(x)

# intro to sets
# def average(array):
#     set1 = set(array)
#     # print(set(array))
#     sum1 = sum(set1)
#     avg = sum1 / len(set1)
#     return '%.3f' % avg


# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

# take multiple inputs on seperate lines
# n = int(input())
# list1 = list(map(int, input().split(' ')))

# print(n)
# print(list1)

# multiple inputs on the same line
# string1,num1 = map(str,input().split(' '))
# print(string1, int(num1))

# strip
# string = input().strip()
# sub_string = input().strip()

# print(string,sub_string)

# mutation
# def mutate_string(string, position, character):
#     return(string[:position]+character+string[position+1:])

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# percentage
# if __name__ == '__main__':
#     n = int(input())
#     name = []
#     for _ in range(n):
#         name = map(str,input().split())
#     print(name)
#     # set1 = set(name)
#     # print(set1)
#     # for x in name:
#     #     print(x)

# multi line input
# for _ in range(n):
#         name.append(input())

# if __name__ == '__main__':
#     n = int(input())
#     name = []
#     for _ in range(n):
#         name.append(input())
#     # print(name)
#     print(len(set(name)))

# list1 = []
# for x in name:
#     for y in x:
#         print(y)
#         list1.append(y)
# print(set(list1),len(set(list1)))

# set difference
# totalEng = int(input())
# eng = input().split(' ')
# totalFrench = int(input())
# french = input().split(' ')
# # print(totalEng, eng)
# # print(totalFrench,french)
# s1 = set(eng)
# print(len(s1.difference(french)))

# set union
# engTotal = int(input())
# eng = input().split(' ')
# frenchTotal = int(input())
# french = input().split(' ')

# set1 = set(eng)
# print(len(set1.union(french)))

# string formatting
print('-------Day 9-------')
# def print_formatted(number):
#     num1 = '    '
#     for x in range(number):
#         print(x)
#     print(num1)
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# nested lists
# if __name__ == '__main__':
#     name = []
#     score = []
#     for _ in range(int(input())):
#         name.append(input())
#         score.append(float(input()))
#     # print(name)
#     # print(score)
# res = list(zip(name, score))
# # print(res)
# list1 = []
# for x in res:
#     list1.append(list(x))
#     # print(x[0])
# # print(list1)

# listNum = []
# for x in list1:
#     listNum.append(x[1])
# # print(listNum)
# list2 = list(set(listNum))
# list2.sort()
# # print(list2[1])

# listName = []
# for x in list1:
#     # print(x[1])
#     if list2[1] == x[1]:
#         listName.append(x[0])
# # print(sorted(listName))

# for x in sorted(listName):
#     print(x)

# zip (binds two arrays) list(zip(x,y))
# sort (sorts a list of numbers from smallest to largest) .sort()
# sorted (alphabetically sorts items in a list) sorted(x)


# collection
# noShoes = int(input())
# shoeSize = list(map(int,input().split(' ')))
# noCustoms = int(input())
# sp = []
# for _ in range(noCustoms):
#     vals = list(map(int,input().split(' ')))
#     sp.append(vals)
# # print(noShoes)
# # print(shoeSize)
# # print(noCustoms)
# # print(sp)
# cost1 = 0
# for x in sp:
#     # print(x[0])
#     if x[0] in shoeSize:
#         # print(x[1])
#         cost1 += x[1]
#         shoeSize.remove(x[0])
# print(cost1)

# collection ordered dictionary
# item_name = int(input())
# net_price = []

# for _ in range(item_name):
#     net_price.append((input()))

# print(net_price)

item_name = int(input())
net_price = ''

for _ in range(item_name):
    net_price += str((input())) + '\n'

print(net_price)

test = []

for i in net_price.strip().split("\n"):
    split = i.rsplit(maxsplit=1)
    split[1] = int(split[1])
    test.append(split)
# print(test)

list1 = []
for x in test:
    # print(x[0])
    if x[0] in list1[0]:
        continue
    else:
        list1.append(x)
print(list1)
