# Question1 - Write a program myfamily.py and try out the following piece of code. 

myfamily = ("mother", "father", "sister", "brother", "sister") 
print(myfamily) 
print(type(myfamily))
print(myfamily[2])
# print(myfamily.append("me"))  does not work
# print(myfamily.pop(3))        it is also not working
print("**************************************")
# Q2: Write a program laptop.py and try out the following piece of code.

laptop = { "brand": "dell", "model": "alienware", "year": 2010 }
print(laptop["brand"])
laptop["home"]=True
laptop["year"]=2019
print(laptop)

print("****************************************")
# Q3- Write a program user.py that stores information about a user into a dictionary, and performs exactly as follows:

user = {"What is the user's name":None, "What is the user's age":None, "What is the user's country of birth": None, "What is the user known for":None}
for i in user:
    value = input(f" '{i}': ")
    user[i] = value
print(user)
