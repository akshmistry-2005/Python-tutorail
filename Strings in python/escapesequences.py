"""
\n - new line
\t - new tab
\\ - add \
\' - add '
\" - add "
"""
print("aksh \n mistry")
print("aksh \t mistry")
print("aksh \\ mistry")
print ("aksh \' mistry")
print ("aksh \" aksh mistry")


""" Count of substrings in python"""
c1="Here we are learning python. learning python is easy and fun."
c2="python"
print(c1.count(c2))

""" Examples 2 """
h1="here we are using python where where we are learning how the count function works "
h2="e"
print(f"The occurence of {h2} is {h1.count(h2)}")

""" Change in the cases of string """
t1="the change operations of the STRINGS IS DONE LIKE THIS."
print(t1.upper())
print(t1.lower())
print(t1.title())
print(t1.capitalize())

""" Stratswith and Endswith function"""
i1="we are learning python using tutedude"
print(i1.startswith("w"))
print(i1.endswith("tutedude"))
print(i1.startswith("are"))
print(i1.endswith("we"))
