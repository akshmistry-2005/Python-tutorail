name="Aksh Mistry"
age="20"
place="vadodara"
course="Btech"
university="Parul university"
""" print:- Aksh Mistry is a student, his age is 20 and lives in Vadodara, studies in Parul university and has pursued Btech."""
print(f"{name} is a student, his age is {age} and lives in {place}, studies in {university} and has pursued {course}.")

""" Here, the use of fstring is demonstrated, it show how in single line we can use multiple strings and variables"""

vehicle=input("Enter the name of the vehicle: ")
city=input("Enter the city in which vehicle will be used: ")
owner=input("Enter the name of the owner: ")
company=input("Enter the name of the vehicle company: ")

""" Print- Ramesh has a bike of honda company and he wants to transport his bike to Delhi"""
print(f"{owner} has a {vehicle} of {company} company and he wants to transport his {vehicle} to {city}. ")
