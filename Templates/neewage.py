
'''
abc = xyz = 'mango'
print(abc,xyz)
print(type(abc))
'''
'''
x = 'hello World day'
print(x,type(x))
print(len(x))
print(x[2:8])
print(x.replace("hello","Soght"))
'''

'''
Anime = ["Jojo","boruto","naruto","onepiece"]
Anime[2] = "himmawari"
print(Anime,(type(Anime)))
print(Anime[2])
'''
"""
Student = {
    "Name" : "Sudha",
    "Id" : "251",
    "Age" : "19",
    }
print(Student,type(Student))
Student.update({"Name" : "Sandeep"})
print(Student["Name"])
x = Student.keys()
y = Student.values()
print(x)
print(y)
Employee = dict(Student)
print(Employee,type(Employee))

car = ["BmW","Thar","mahindra","honda"]
print(car,type(car))
"""
'''
class myhobby:
    def __init__(self,carname,color,year):
        self.carname = carname
        self.color = color
        self.year = year
    def __str__(self):
        return f"{self.carname}{self.color}{self.year}"
firstcar = myhobby("Honda","White", 2011)
print(firstcar)
'''
'''
import math

x = min(2,4,5)
y = max(4,5,6)
z = abs(-856)
a = math.sqrt(9)
b = math.ceil(1.8)
c = math.floor(1.8)
print(x,y,z)
print(a,b,c)

'''
'''
import json


Anime = ["Jojo","boruto","naruto","onepiece"]
y = json.dumps(Anime)
print(y,type(y))
'''
'''
f = open("rad.txt","r")
print(f.read())
'''
'''
import numpy as np

arr = np.array(["person1","person2","person2"],ndmin=2)
print(arr,type(arr))
print(arr.ndim)
print(arr[0:1:2])
'''

#Printing Hello World
print("Hello World")

#Add Two Numbers
num1 = 2
num2 = 3
print(num1+num2)

#To Find the Square Root
import math

Num3 = int(input("Enter A Number"))
Result = math.sqrt(Num3)
print(Result)

#To Generate Random Numbers
import random
print(random.randrange(0,50))

