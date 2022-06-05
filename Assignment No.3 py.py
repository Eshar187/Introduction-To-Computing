# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 23:48:04 2022

@author: Dell
"""

#1
x = int(input('Enter a number of your choice :'))
y = bin(x)
y=y[2:]
print('Binary equivalent of the number entered:',y)

#2

print("select an operation to perform: ")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")

operation= input()
if operation=="1":
    num1 = input("enter 1st number: ")
    num2 = input("enter 2nd number: ")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation== "2":
    num1=input("enter 1st number: ")
    num2 =input("enter 2nd number: ")
    print("The subtraction is " + str(int(num1) - int(num2)))
elif operation== "3":
    num1=input("enter 1st number: ")
    num2 =input("enter 2nd number: ")
    print("The multiplication is " + str(int(num1) * int(num2)))
elif operation== "4":
    num1=input("enter 1st number: ")
    num2 =input("enter 2nd number: ")
    print("The division is " + str(int(num1) / int(num2)))
else:
    print("Invalid Entry")


#3

#a
print((3+4)*5)

#b
n = int(input("Enter Number"))
ans = (n*(n-1))/2
print(ans)

#c
r = float(input("Enter Number"))

import math
pi= math.pi
m = 4*pi*(r**2)        
print(m)

#d
a = float(input("Enter an angle in degrees ="))
b = float(input("Enter another angle in degrees ="))
r = float(input("Enter a number =" ))
d = math.sqrt(r*(math.cos(math.radians(a)))**2 + r*(math.sin(math.radians(b)))**2)
print(d)


#e
y1 = int(input("Enter Number y1: "))
y2 = int(input("Enter Number y2:"))
x1 = int(input("Enter Number x1:"))
x2 = int(input("Enter Number x2: "))
ansr = (y1 - y2)/(x1 - x2)
print(ansr)


#4

#a)
for a in range(5):
    print(a, end=" ") 
    
print("\n")

#b)
for b in range(3,10):
    print(b, end=" ")
print("\n")   
 
#c)
for c in range(4,13,3):
    print(c, end=" ")
print("\n")

#d)
for d in range(4,13,3):
    print(d, end=' ')
print("\n")

#e)
for e in range(5,3):
    print(e, end=' ')
print("\n")



#5


 
h= int(input("Enter no. of hydrogen atoms: "))
c = int(input("Enter the no. of carbon atoms: "))
o= int(input("Enter the no. of oxygen atoms: "))

wt_h = h*1.00794
wt_c = c*12.0107
wt_o = o*15.9994

ans=(wt_h + wt_c + wt_o)
print("The molecular weightof the given molecule is",ans)