
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
from calendar import different_locale
from cgi import print_form
from collections import namedtuple
from operator import index
from pickle import TRUE
from re import A, X, sub
from secrets import randbits
import string
from time import time
from tkinter import Y
from black import diff

from numpy import append, intp
from pyrsistent import b
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

# item_name = int(input())
# net_price = ''

# for _ in range(item_name):
#     net_price += str((input())) + '\n'

# # print(net_price)

# test = []

# for i in net_price.strip().split("\n"):
#     split = i.rsplit(maxsplit=1)
#     split[1] = int(split[1])
#     test.append(split)
# # print(test)

# list1 = []
# list2 = []
# for x in test:
#     # print(x[0])
#     if x[1] in list1:
#         # print(">",x[0])
#         index = list1.index(x[1])
#         list2[index][1] += x[1]
#         # list2[x[1]][0] += x[1]
#         continue
#     else:
#         list1.append(x[1])
#         list2.append(x)
# # list2[0][0] += 'BANANA'
# # print(list2[0][1])
# # print(list2)

# for x in list2:
#     print(x[0],x[1])
# print(list1)
# index() to get the index in a list

# collection named tuple
# nt = namedtuple('nt', 'ID MARKS CLASS NAME')
# xyz = nt(ID=1, MARKS=97, CLASS=7, NAME='Raymond')
# # print(xyz)
# # print(xyz.MARKS,xyz.CLASS)

# num1 = int(input())
# for _ in num1:
#     xyz.


# collection deque
# from collections import deque
# d = deque()
# # print(d)
# num1 = int(input())
# task = []

# for _ in range(num1):
#     # task += (input('>')) + '\n'
#     task.append(input().split(' '))
# # print(task)

# for x in task:
#     # print(x[0])
#     if x[0] == 'append':
#         d.append(x[1])
#     elif x[0] == 'appendleft':
#         d.appendleft(x[1])
#     elif x[0] == 'pop':
#         d.pop()
#     elif x[0] == 'popleft':
#         d.popleft()
# # print(d)

# str1 = ''
# for x in d:
#     str1 += x + ' '
# print(str1)

# set .discard() pop()
# s = set([1])

# n1 = int(input())
# # nEl = []
# nEl = list(map(int,input().split(' ')))
# # print(nEl)

# n2  = int(input())
# nCom = []
# for _ in range(n2):
#     nCom.append(input().split(' '))
# # print(nEl)
# # print(nCom)

# s = set([])
# for x in nEl:
#     # print(x)
#     s.add(x)
# # print(s)

# for x in nCom:
#     if x[0] == 'pop':
#         s.pop()
#     elif x[0] == 'discard':
#         # print('d',x[1])
#         s.discard(int(x[1]))
#     elif x[0] == 'remove':
#         try:
#             # print('r',x[1])
#             s.remove(int(x[1]))
#         except KeyError:
#             continue
# if not s:
#     s.add(0)

# sum1 = 0
# for x in s:
#     sum1 += x
# print(sum1)

#iterables and iterators
# from itertools import combinations

# num1 = int(input())
# nEl = list(map(str,input().split(' ')))
# k = int(input())
# # print(nEl)
# # print(k)

# str1 = ''
# for x in nEl:
#     str1 += x
# # print(str1)
# per1 = list(combinations(str1, k))
# # print(per1)

# count = 0
# for x in per1:
#     if 'a' in x:
#         count+=1
#     # elif str1[1] in x:
#     #     count+=1

# print(count/len(per1))

# list
# list1 = []
# n = int(input())

# nCom = []
# for _ in range(n):
#     nCom.append(input().split(' '))
# # print(nCom)

# for x in nCom:
#     # print(x)
#     if x[0] == 'insert':
#         list1.insert(int(x[1]),int(x[2]))
#     elif x[0] == 'print':
#         print(list1)
#     elif x[0] == 'remove':
#         list1.remove(int(x[1]))
#     elif x[0] == 'append':
#         list1.append(int(x[1]))
#     elif x[0] == 'sort':
#         list1.sort()
#     elif x[0] == 'pop':
#         list1.pop()
#     elif x[0] == 'reverse':
#         list1.reverse()

# itertolls combination
# text1 = input().split(' ')
# # print(text1)
# name1 = text1[0]
# num1 = text1[1]

# from itertools import combinations
# list1 = list(combinations(name1,int(num1)))
# list1.sort()
# # print(list1)
# list2 = []
# for x in list1:
#     list2.append(list(x))
# # print(list2)
# list3 = []
# for x in list2:
#     x.sort()
#     list3.append(x)
# list3.sort()
# print(list3)
# nameList = []
# for x in name1:
#     nameList.append(x)

# nameList.sort()
# # nameList.append(list2)
# # print(nameList)
# nameStr = ''
# for x in nameList:
#     nameStr += x + '\n'
# str1 = ''
# str2 = ''
# count = 0
# val = 0
# # for x in list3:
# #     for y in x:
# #         str2 += y
# #         count+= 1
# #         if count == int(num1):
# #             str1 += str2 + '\n'
# #             count = 0
# #             str2 = ''

# # for x in range(1,int(num1)+1):
# #     # print(x)
# #     for y in list3:
# #         print(y)

# test1 = []
# for x in list3:
#     # print(x)
#     for y in x:
#         # print(y)
#         if y not in test1:
#             test1.append(y)
# test2 = []
# for x in range(1,int(num1)+1):
#     for y in list3:
#         if len(y[:x]) > 1:
#             test1.append(y[:x])
#         elif len(y[x:]) > 1:
#              test1.append(y[:x])
# # print(test1)

# for x in test1:
#     print("".join(x))

# ------------------------------------------#
# text1 = input().split(' ')
# # print(text1)
# name1 = text1[0]
# num1 = text1[1]

# from itertools import combinations
# list4 = []
# for x in range(1,int(num1)+1):
#     list4.append(list(combinations(name1,int(x))))
# list4.sort()
# # print(list4)
# list5 = []
# for x in list4:
#     # x.sort()
#     for y in x:
#         list5.append(list(y))
#         # print("".join(y))
# print(list5)
# list6 = []
# for x in list5:
#     x.sort()
#     print(x)
#     list6.append(x)
#     # print("".join(x))
# print(list6)
# list6.sort()
# lst1 = sorted(list6, key=len)
# print(lst1)

# for x in lst1:
#     print("".join(x))

# lst1 = sorted(list6, key=len) to sort using len

# check subset
# num1 = int(input())

# aEl = []
# bEl = []
# for _ in range(num1):
#     aNum = int(input())
#     aEl.append(list(map(int, input().split(' '))))
#     bNum = int(input())
#     bEl.append(list(map(int, input().split(' '))))

# # print(aEl)
# # print(bEl[0])
# # # print(aEl[0] in bEl[0])
# # for x in aEl:
# #     print(x)
# #         # print(x in bEl[0])

# # count = 0
# # for x in range(len(aEl)):
# #     # print(aEl[x] in bEl[x])
# #     # print(bEl[x])
# #     for y in aEl[x]:
# #         print(y)
# check1 = []
# for x in range(num1):
#     print(bEl[x])
#     for y in aEl[x]:
#         # print(y in bEl[x])
#         if y in bEl[x]:
#             check = True
#         else:
#             check = False
#             break
#     check1.append(check)

# for x in check1:
#     print(x)


# plus minus
# def plusMinus(arr):
#     # print(arr)
#     pos1 = 0
#     neg1 = 0
#     z1 = 0
#     for x in arr:
#         if x > 0:
#             pos1 += 1
#         elif x < 0:
#             neg1 += 1
#         else:
#              z1 += 1
#     print("{0:.5f}".format(pos1/len(arr)))
#     print("{0:.5f}".format(neg1/len(arr)))
#     print("{0:.5f}".format(z1/len(arr)))


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     plusMinus(arr)
# def staircase(n):
#     test = ''
#     for x in reversed(range(1,n)):
#         test += x*' '+'\n'
#         for y in range(1,n+1):
#             test += y*'#'+'\n'
#     print(test)


# n = int(input().strip())

# staircase(n)


# compare the triplets
# n1 = list(map(int,input().split(' ')))
# n2 = list(map(int,input().split(' ')))

# # print(n1,n2)

# n1Count = 0
# n2Count = 0
# for x in range(len(n1)):
#     # print(n1[x] > n2[x])
#     if n1[x] > n2[x]:
#         n1Count += 1
#     elif n1[x] < n2[x]:
#         n2Count += 1
# print(n1Count,n2Count)


# min-max
# n1 = list(map(int,input().split(' ')))

# min1 = n1[0]
# max1 = n1[0]
# for x in n1:
#     if x > max1:
#         max1 = x
#     if x < min1:
#         min1 = x

# # print(min1,max1)
# print(sum(n1)-max1,sum(n1)-min1)


# Grading students
# n1 = int(input())
# El = []
# for _ in range(n1):
#     El.append(int(input()))

# for x in El:
#     # print(x).
#     if x >= 38:
#         if (x % 5) > 2 and (x % 5) < 5:
#             pos = El.index(x)
#             # print(x % 5)
#             while(x % 5 != 0):
#                 x += 1
#             El[pos] = x
# # print(El)

# for x in El:
#     print(x)


# triangles

# n = 5

# for x in range(n+1):
#         print('#'*x)
# for x in reversed(range(n+1)):
#     print('#'*x)

# for i in range(n+1):
#     for j in range(i):
#         print('*',end='') #we dont want to automaticcaly change lines
#     print() #changes lines

# reverse star
# for i in range(n+1):
#     for j in range(i,n): #to reverse
#         print('*',end='') #we dont want to automaticcaly change lines
#     print() #changes lines


# for i in range(1,n+1):
#     for j in range(i,n): #to reverse
#         print(' ',end='') #we dont want to automaticcaly change lines
#     for k in range(i):
#         print('*',end='')
#     print() #changes lines

# n1 = input().split(":")

# def timeConversion(s):
#     lst1 = []
#     print(s)
#     if s[-1][-2:] == 'AM':
#         if s[0] == '12':
#             s[0] = '00'
#         lst1.append(str(s[0]))
#         lst1.append(str(s[1]))
#         lst1.append(str(s[2][:-2]))
#         lst1 = ":".join(lst1)
#         print(lst1)
#     elif s[-1][-2:] == 'PM':
#         if s[0] == '12':
#             s[0] = int(s[0])
#         else:
#             s[0] = int(s[0]) + 12
#         lst1.append(str(s[0]))
#         lst1.append(str(s[1]))
#         lst1.append(str(s[2][:-2]))
#         lst1 = ":".join(lst1)
#         print(lst1)
# timeConversion(n1)


# n1 = int(input())
# lst1 = list(map(int, input().split(' ')))

# print(lst1)

# min1 = lst1[0]
# max1 = lst1[0]
# c1 = 0
# c2 = 0
# for x in lst1:
#     if min1 < x:
#         min1 = x
#         c1 += 1
#     if max1  > x:
#         max1 = x
#         c2 += 1
# # print(max1)
# # print(min1)
# print(c1,c2)


# division sun pairs
# lst1 = list(map(int,input().split(' ')))
# lst2 = list(map(int,input().split(' ')))

# # print(lst1[1])
# print(len(lst2))

# count = 0
# for x in lst2:
#     for y in lst2:
#         # print(x,y)
#         if x < y:
#             if (x+y)%lst1[1] == 0:
#                 # print(x,y)
#                 count += 1
# print(count)

# soln
# lst1 = list(map(int,input().split(' ')))
# lst2 = list(map(int,input().split(' ')))
# def divisibleSumPairs(n, k, ar):
#     # Complete this function
#     count = 0
#     for i in range(n-1):
#         j = i+1
#         while j < n:
#             if ((ar[i] + ar[j]) % k) == 0:
#                 count += 1
#             j += 1
#     return count

# subarray division
# n1 = input()
# s = list(map(int,input().split(' ')))
# d,m = list(map(int,input().split(' ')))

# # print(s[0:m])
# count = 0
# for x in range(len(s)):
#     # print(s[x:x+m])
#     if len(s[x:x+m]) == m:
#         if sum(s[x:x+m]) == d:
#             count += 1
# print(count)

# sales by match
# n = int(input())
# arr1 = list(map(int,input().split(' ')))

# def sockMerchant(n, ar):
#     # Write your code here
#     lst1 = []
#     test_list = list(set(ar))
#     for x in test_list:
#         if ar.count(x) > 1:
#             lst1.append(x)
#     print(len(lst1))
# sockMerchant(n,arr1)

# import math
# n = int(input())
# arr1 = list(map(int,input().split(' ')))

# def sockMerchant(n, ar):
#     # Write your code here
#     lst1 = []
#     test_list = list(set(ar))
#     for x in test_list:
#         if ar.count(x) > 1:
#             # print(math.floor(ar.count(x)/2))
#             lst1.append(math.floor(ar.count(x)/2))
#     print(sum(lst1))
# sockMerchant(n,arr1)

# bill division
# def bonAppetit(bill, k, cost):
#     # for x in range(k):
#     #     bill.remove(k[x])
#     bill.remove(bill[k])
#     sum1 = sum(bill)/2
#     if cost == sum1:
#         print('Bon Appetit')
#     else:
#         print('{0:.0f}'.format(cost-sum1))

# n, k = list(map(int,input().split(' ')))
# bill = list(map(int, input().split(' ')))
# cost = int(input())

# bonAppetit(bill,k,cost)

#Cat and Mouse (Tom and jerry)

# q = int(input())
# lst1 = []
# for x in range(q):
#     lst1.append(list(map(int,input().split(' '))))

# # print(lst1)
# for x in lst1:
#     # print(abs(x[0]-x[2]),abs(x[1]-x[2]))
#     if abs(x[0]-x[2]) > abs(x[1]-x[2]):
#         print('Cat B')
#     elif abs(x[0]-x[2]) == abs(x[1]-x[2]):
#         print('Mouse C')
#     elif abs(x[0]-x[2]) < abs(x[1]-x[2]):
#         print('Cat A')

# electronic shop
# budget1 = list(map(int, input().split(' ')))
# key1 = list(map(int, input().split(' ')))
# drive1 = list(map(int, input().split(' ')))

# b = budget1[0]
# # print(key1)
# # print(drive1)
# lst1 = []
# for x in key1:
#     for y in drive1:
#         # print(x,y)
#         if x+y <= b:
#             lst1.append(x+y)
# if not len(lst1):
#     print(-1)
# else:
#     print(max(lst1))

# Hurdle race
# arr1 = list(map(int,input().split(' ')))
# arr2 = list(map(int,input().split(' ')))

# # print(arr1)
# # print(arr2)
# k = arr1[1]

# max1 = max(arr2)
# if max1 > k:
#     print(max1 - k)
# else:
#     print(0)

# migratory birds
# n = int(input())
# arr1 = list(map(int,input().split(' ')))

# lst1 = list(set(arr1))
# lst2 = []
# for x in lst1:
#     # print(x)
#     lst2.append(arr1.count(x))
#     pos = lst2.index(max(lst2))

# print(lst1[pos])

# counting vallet
# n1 = int(input())
# arr1 = input()

# count = 1
# count1 = 0
# for x in arr1:
#     # print(x)
#     if x == 'U':
#         count += 1
#     elif x == 'D':
#         count -=1

#     if count == 1:
#        if x == 'U':
#           count1 += 1

# print(count1)

# utopian tree initial value starts at 0
# n = int(input())
# arr1 = []
# for _ in range(n):
#     arr1.append(int(input()))

# lst1 = []
# for x in arr1:
#     size1 = 0
#     for y in range(x+1):
#         if y%2 == 1:
#             size1 *= 2
#         else:
#             size1 += 1
#     lst1.append(size1)
# for x in lst1:
#     print(x)


# Designer PDF viewer
# print(ord('a')-97)

# arr1 = list(map(int,input().split(' ')))
# word1 = input()

# # print(arr1,word1)
# lst1 = []
# for x in word1:
#     # print(ord(x)-97)
#     n1 = ord(x)-97
#     # print(arr1[n1])
#     lst1.append(arr1[n1])

# max1 = max(lst1)
# print(len(word1)*max1)


# Angry professor
# n1 = int(input())
# arr1 = []
# arr2 = []
# for _ in range(n1):
#     arr1.append(list(map(int,input().split(' '))))
#     arr2.append(list(map(int,input().split(' '))))

# lst1 = []
# for x in range(len(arr1)):
#     n,k = arr1[x]
#     lst1.append(k)
# # print(lst1)

# lst2 = []
# for x in arr2:
#     count1 = 0
#     for y in x:
#         if y <= 0:
#             count1 += 1
#     lst2.append(count1)
#     # print(lst1[y])

# print(lst1,lst2)
# for x in range(len(lst1)):
#     if lst1[x] > lst2[x]:
#         print("YES")
#     else:
#         print('NO')

# viral advert
# import math
# n1 = int(input())

# k1 = math.floor(5/2)
# print(k1)
# k1 = k1*3
# print(math.floor(k1/2))

# arr1 = []
# for x in range(n1):
#     if x == 0:
#         k1 = math.floor(5/2)
#         arr1.append(k1)
#     # print(x)
#     else:
#         k1 = k1*3
#         k1 = math.floor(k1/2)
#         arr1.append(k1)
# print(sum(arr1))


# buitiful day at movies
# arr1 = list(map(int, input().split(' ')))

# # print(arr1)

# ini1 = arr1[0]
# fin1 = arr1[1]
# k = arr1[2]

# count1 = 0
# for x in range(ini1,fin1+1):
#     # print(x)
#     rev1 = str(x)[::-1]
#     # print((x-int(rev1))%k)
#     check1 = (x-int(rev1))%k
#     if check1 == 0:
#         count1 += 1
# print(count1)


# jumping on the clouds
# n,k = list(map(int,input().split(' ')))
# arr2 = list(map(int,input().split(' ')))

# count1 = 100
# y = 0
# for x in range(1,len(arr2)+1):

#     y += 1
#     if y == k:
#         y = 0
#         if x == 0:
#             continue
#         if x == n:
#             x = 0
#         # print(x)
#         if arr2[x] == 1:
#             count1 -= 2
#         count1 -= 1
#         y = 0
# print(count1)

# n,k = list(map(int,input().split(' ')))
# arr2 = list(map(int,input().split(' ')))
# count1 = 100

# for x in range(0,len(arr2),k):
#     # print(x)
#     if arr2[x] == 1:
#         count1 -= 2
#     count1 -= 1
# print(count1)


# sequence equation
# It took me a while to find this as well, so I'll leave this here for others facing the same frustration. Let's use sample input 0 as our example.
# the input is:
# 3
# 2 3 1
# Our expected output is also [2, 3, 1]
# The first value 3 in our input is the length of the list, so it's not important for the purpose of finding our objective.
# Our list, [2, 3, 1] needs to be used to define a new list. The new list starts from the minimum of the list (1), and ends with the maximum of the list (3).
# n = int(input())
# arr1 = list(map(int, input().split(' ')))

# for x in range(len(arr1)):
#     # print(arr1[x],x+1)
#     # if x == arr1[x]:
#     # print(arr1.index(x+1)+1)
#     pos1 = arr1.index(x+1)+1
#     # print(arr1.index(x+1)+1 , arr1.index(pos1)+1)
#     print(arr1.index(pos1)+1)


# find digits
# n = int(input())
# arr1 = []
# for _ in range(n):
#     arr1.append((input()))
# # print(arr1)
# lst1 = []
# for x in arr1:
#     count = 0
#     for y in x:
#         # print(y)
#         if int(y) == 0:
#             continue
#         elif int(x) % int(y) == 0:
#             count += 1
#     lst1.append(count)
# for x in lst1:
#     print(x)


# cut the sticks
# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))

# print(n1,arr1)

# min1 = min(arr1)
# lst1 = []
# lst2 = []
# for x in arr1:
#     if x == min1:
#         # print('yes')
#         arr1.remove(x)
#     else:
#         x -=min1
#         lst1.append(x)
# # lst2.append(len(lst1))
# print(lst1)

# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))
# min1 = min(arr1)
# lst1 = arr1[:]


# for x in range(len(lst1)-1):
#         if arr1[x] == min1:
#                 lst1.remove(min1)
# for x in range(len(lst1)):
#         lst1[x] -= min1
# print(lst1)

# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))
# min1 = min(arr1)
# lst1 = arr1[:]

# while(len(lst1) != 0):
#         print(len(lst1))
#         if len(lst1) < n1:
#             min1 = min(lst1)
#             arr1 = lst1[:]
#         for x in range(len(lst1)):
#             if arr1[x] == min1:
#                 lst1.remove(min1)
#         for x in range(len(lst1)):
#             lst1[x] -= min1

# jumping on clouds
# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))

# count = 0
# for x in range(0,n1,2):
#     if arr1[x] != 1:
#         print(x)
#         count += 1
#     elif arr1[x] == 1:
#         print(x)
#         count += 1
# print(count)


# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))
# count = 0
# for y in range(0,n1+1):
#     # print(y)
#     # if y%2 == 0:
#     #     print(y)
#     if count%2 == 0:
#         # print(y)
#         if arr1[count] != 1:
#             print(count)
#     count += 1

#     if y == n1 and n1%2 != 0:
#         print(y)

# eqalise the array
# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))

# lst1 = []
# for x in arr1:
#     lst1.append(arr1.count(x))

# max1 = max(lst1)
# pos = lst1.index(max1)
# pos1 = arr1[pos]

# lst3 =[]
# for x in arr1:
#     if x != pos1:
#         lst3.append(x)
# print(len(lst3))

# max1 = max(arr1)
# lst1 = []
# for x in arr1:
#     if x != max1:
#         lst1.append(x)
# print(len(lst1))


# service lane
# n,t = list(map(int,input().split(' ')))
# arr2 = list(map(int,input().split(' ')))

# lst1 = []
# for _ in range(t):
#     lst1.append(list(map(int,input().split(' '))))
# # print(lst1)
# for x in lst1:
#     # print(x[0],x[1])
#     print(min(arr2[x[0]:x[1]+1]))


# str1 = input()

# print(len(str1)/3)
# # count = 0
# # for x in str1:
# #     # print(x)
# #     if x != 'S' and x!= 'O':
# #         count += 1
# # print(count)

# c1 = ''
# lst1 = []
# for x in str1:
#     c1 += x
#     if len(c1) == 3:
#         lst1.append(c1)
#         c1 = ''

# # print(lst1)
# count = 0
# for x in lst1:
#     print(x)
#     if x != 'SOS':
#         if x[0] != 'S' :
#             count += 1
#         if x[1] != 'O' :
#             count += 1
#         if x[2] != 'S' :
#             count += 1
# print(count)


# camelCase
# word1 = input()

# str1 = ''
# count = 1
# for x in word1:
#     # print(ord(x))
#     if ord(x) < 97:
#         # print(x)
#         str1 += '\n'
#         count += 1
#     str1 += x
# # print(str1)
# print(count)


# minimum distance
# n1 = int(input())
# arr1 = list(map(int,input().split(' ')))

# # print(n1,arr1)
# lst1 = []
# for x in arr1:
#     if arr1.count(x) >= 2:
#         # print(x)
#         lst1.append(x)
# set1 = list(set(lst1))

# lst2 = []
# for x in range(len(set1)):
#     # print(x)
#     dif1 = ''
#     for y in range(len(arr1)):
#         if set1[x] == arr1[y]:
#             # print(arr1.index(x))
#             if dif1 == '':
#                 dif1 = y
#             else:
#                 dif1 -= y
#                 lst2.append(abs(dif1))
#     # print(sum1)
# if lst2:
#     print(min(lst2))
# else:
#     print(-1)


# hackerrank in a string
# n1 = int(input())

# arr1 = []
# for _ in range(n1):
#     arr1.append(input())
# print(arr1)

# for x in arr1:
#     # for y in x:
#     #     print(y)
#     check = False
#     if 'h' in x:
#         if 'a' in x:
#             if 'c' in x:
#                 if 'k' in x:
#                     if 'e' in x:
#                         if 'r' in x:
#                             if 'r' in x:
#                                 if 'a' in x:
#                                     if 'n' in x:
#                                         if 'c' in x:
#                                             if 'k' in x:
#                                                 check = True
#     print(check)


# gemstone
# n1 = int(input())
# arr1 = []
# for _ in range(n1):
#     arr1.append(input())
# # print(arr1)
# lst1 = []
# for x in arr1:
#     for y in x:
#         lst1.append(y)
# lst2 = list(set(lst1))
# # print(lst2)

# count1 = 0
# for x in lst2:
#     count = 0
#     # print(x)
#     for y in arr1:
#         if x in y:
#             # print(x,y)
#             count += 1
#             if count == n1:
#                 count1 += 1
# print(count1)


# pangrams
# str = input()
# check = True
# for x in str:
#     # print(x)
#     for y in range(65,123):
#         # print(x,y)
#         if ord(x) == y:
#             continue
#         else:
#             # print(y)
#             check = False
# print(check)

# str1 = input()

# str1 = str1.lower()
# str2 = str1.split(' ')
# # print(str2)
# lst = []
# for x in str2:
#     for y in x:
#         lst.append(ord(y))

# lst = list(set(lst))
# # print(lst)
# # print(ord('a'),ord('z'))
# check = True

# for x in range(97,123):
#     if x in lst:
#         continue
#     else:
#         check = False
# # print(check)

# if check:
#     print('pangram')
# else:
#     print('not pangram')


# scoring
# n1 = int(input())
# arr1 = []
# for _ in range(n1):
#     arr1.append(input())
# # print(arr1)

# lst1 = []
# for x in arr1:
#     lst1.append(list(set(x)))
# # print(lst1)

# for x in lst1:
#     print(len((x)))


# data structures
# arrays
n1 = int(input())
arr1 = list(map(int, input().split(' ')))
# print(arr1)

lst1 = []
for x in reversed(arr1):
    lst1.append(x)
# print(lst1[:])

str1 = ''
for x in lst1:
    str1 += str(x) + ' '
print(str1)


#sparse arrays
n1 = int(input())
arr1 = []
for _ in range(n1):
    arr1.append(input())
# print(arr1)    

n2 = int(input())
arr2 = []
for _ in range(n2):
    arr2.append(input())
# print(arr2)    

# print(arr1.count(arr2[0]))

for x in arr2:
    print(arr1.count(x))