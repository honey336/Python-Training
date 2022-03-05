#!/c/Users/oyino/Documents/devsearch/honey/Scripts/python

# Write some code to find the sum of all  multiples of 3 and 5 between 0 and 1000.
total_sum = 0
for i in range(0, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
    print(total_sum)

# Write a python program to count the number of occuring characters in a given string.
from collections import Counter

In [3]: Counter('google.com')
Out[3]: Counter({'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1})

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself
 def change_char(str1):
   ...:     char = str1[0]
   ...:     str1 = str1.replace(char, "$")
   ...:     str1 = char + str1[1:]
   ...:
   ...:     return str1
   ...:
   ...:
   ...: print(change_char("restart"))
resta$t

# Given the following list, list1 = [100, 200, 300, 400, 500], reverse the list
In [7]: list1 = [100, 200, 300, 400, 500]

In [8]: list1.reverse()

In [9]: print(list1)
[500, 400, 300, 200, 100]

# Write a program to add two lists index-wise. 
# Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. 
# any leftover items will get added at the end of the new list.
 list1 = ["M", "na", "i", "Ke"]
    ...: list2 = ["y", "me", "s", "lly"]
    ...: list3 = [i + j for i, j in zip(list1, list2)]
    ...: print(list3)
['My', 'name', 'is', 'Kelly']

# # Write a Python program to iterate over dictionaries using for loops.

 d = {"Red": 1, "Green": 2, "Blue": 3}
    ...: for color_key, value in d.items():
    ...:     print(color_key, "corresponds to ", d[color_key])
Red corresponds to  1
Green corresponds to  2
Blue corresponds to  3

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
 n = int(input("Input a number "))
    ...: d = dict()
    ...:
    ...: for x in range(1, n + 1):
    ...:     d[x] = x * x
    ...:
    ...: print(d)
Input a number 10
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d = dict()
    ...: for x in range(1, 16):
    ...:     d[x] = x**2
    ...: print(d)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

#Assign the first number of lst to answer _1 and print it. I have helped  you with some of the code
lst=[11, 100, 99, 1000, 999]
answer_1 = 11
In [35]: print(answer_1)
11

#Now print the second item directly. again I am helping you with some of the code
lst=[11, 100, 99, 1000, 999]
print(lst[1])
100


