""" OPERATIONS ON STRING PART 3 
a) reverse()
b) sort()
c) count()
d) membership operation [in]
"""
""" A) REVERSE() """
days_of_week = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(days_of_week)
days_of_week.reverse()
print(days_of_week)

""" B) SORT() """
NUMS= [1,2,4,5,6,7,8,9]
print(NUMS)
NUMS.sort()
print("The Sorted list is: ", NUMS)
NUMS.sort(reverse=True)
print(NUMS)

""" C) COUNT() """
HERE = [1,2,12,122,55,444,56,54,45,45,4,55,66,65,56,12,12,21,222,2,22,11,66,77,88,88,888,8,8,77,77,]
print(f"The list is: {HERE}")
ITEM_TO_COUNT= int(input("Enter the number to be counted :"))
c = HERE.count(ITEM_TO_COUNT)
print(f"The occurence of {ITEM_TO_COUNT} is : {c} ")


""" D) in OPERATION """
ALPHABETS = ["PYHTON","JAVA","C++","C","KOTLIN","REACT"]
print("javascrpt" in ALPHABETS) 