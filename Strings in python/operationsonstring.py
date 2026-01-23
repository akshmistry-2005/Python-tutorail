"""Addition/Concatation of strings"""
language = "python"
version = "9.9.9"
print(language+version)

"""
Subtraction of strings is not possible
s1="abc"
s2="xyz"
print(s1-s2) 
[this code will give error]
"""

"""Multiplication/Repetation of strings"""
language="python"
print(language*2)

"""Membership operation"""
""" in function """
language="python"
print("p" in language)
print("z" in language)


"""not in [opposit of 'in' function]"""
language="python"
print("p" not in language)
print("z" not in language)


""" Comparison of strings in python"""
print("python" == "python")
print("Python" == "python")
print("python " == "python")


""" Removing spaces from string"""
a1="                         Remove all the spaces at the starting and ending of this string     "
a2=a1.strip()
print(a1)
print(a2)


"""Replacing elements from strings in python"""

"""
syntax of replace:-
string.replace("old","new",count)

"""
"""Replacing only one elemet form string"""
b1="Python is high level programming language"
print(b1)
print(b1.replace("h","H",2))

"""Replaceing multiple elements from the string"""
text="now here we have to replace may elements from the string"
print(text)
print(text.replace("now","then").replace("here","there").replace("elements","alphabets"))

"""
syntax for replacing multiple elements from the stringin on print function:-
string.replace("old","new").replace("old","new").replace("old","new")

"""