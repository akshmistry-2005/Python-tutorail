"""
Operatios on lists Part 1:-
a) Slicing
b) Concatenation
c) Repeat
d) Append
e) Insert
"""

""" A) Slicing in lists"""
l1 = [1,2,4,5,6,7,8,9,]
print(l1[1:8:1])
print(l1[2:8:2])

""" B) Concatenation of lists """
""" + operator """
l2=[12,24,45,56,78,98,78,68,78,67,89,78]
print(l2 + l1)

""" * operator (repeator) """
l4 = [12,45,67,56,67,77,88,98,89,80]
print(l4*7)

""" C) Append """
""" Syntax for append function:- 
Syntax:- list.append(item)
         print(list)
"""
l5=["mango", "apple","pineapple","banana"]
l5.append("orange")
print(l5)

"""E) Insert """
"""Syntax for insert in lists
Syntax:- list.insert(index,item)
         print(list)
"""
l6=["ramu","shyam","tara","niresh","sunny","madhur"]
print(l6)
l6.insert(4,"nobil")
print(l6)