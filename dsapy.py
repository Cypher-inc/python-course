
#Array
lst1 = [ 2, 4, 5, 7]

# To find an element 
print(lst1[2]) #O(1)

# for x in lst1: #O(n)

#for x in lst1:
#for y in x   #O(n^2)

# Using binary search O(log n)

#insert
# lst1.insert(1,256)++

#1
# lst1 = [2200, 2350, 2600, 2130, 2190]

# print(lst1[1]-lst1[0])
# sum1 = 0
# for x in range(len(lst1)):
#     if x <= 2:
#         sum1 += lst1[x]
# print(sum1)      
# check  = False
# for x in lst1:
#     if x == 2000:
#         check = True   
# print(check)        

# lst1.append(1980)
# print(lst1)

# for x in range(len(lst1)):
#     if x == 3:
#         lst1[x] -= 200
# print(lst1)         

#2
# heroes=['spider man','thor','hulk','iron man','captain america']
# print(len(heroes))

# heroes.append('black panther')
# print(heroes)

# heroes.remove('black panther')
# heroes.insert(3, 'black panther')
# print(heroes)

# # heroes.remove(heroes[1])
# heroes[1:3]=['doctor strange']
# print(heroes)

# print(sorted(heroes))

#3
n1 = int(input())
lst1 = []
for x in range(n1):
    # print(x)
    if x%2==1:
        lst1.append(x)
print(lst1)        