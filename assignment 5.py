# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 22:31:09 2022

@author: Dell
"""

 #Question1

s = input("Enter the string that you want tu reverse: ")
 
str=""
for i in s:
    
    str = i + str 
print ("The reversed string is : ",str)
    



#Question2

a=int(input("Enter the lower range: "))
b=int(input("Enter the upper range: "))
c=int(input("Enter the number: "))

for i in range(a,b+1):
    if i%c==0:
        print("The number is divisible by: ",c,i)



#Question3

a = float(input('Please Enter the First side of a Triangle: '))
b = float(input('Please Enter the Second side of b Triangle: '))
c = float(input('Please Enter the Third side of c Triangle: '))
 
s = (a + b + c) / 2
 
Area = (s*(s-a)*(s-b)*(s-c)) 
if (a+b)>c and (b+c)>a and (a+c)>b :
    print(" The Area of a Triangle is %0.2f" %Area)

else: 
    print("Triangle is not possible")        




#Question4

n=int(input("Enter the number: "))

for i in range(n): 
    for j in range(i): 
      print("*", end="") 
    print('') 
for i in range(n, 0, -1): 
    for j in range(i): 
      print( '*' ,end="" ) 
    print('') 


#Question5

n = int(input("Enter the number of rows: "))
value = 65
for i in range(0,n+1):
    for j in range(0,i):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
        if(value>90):
            value=65
    print()
    
    
    
#Question6


a = int(input ( "Please, Enter the Lower Range value : " )) 
b = int(input ( "Please, Enter the Upper Range Value : ")) 

print ("The Prime Numbers in the range are: " ) 
for num in range (a,b+1): 
    if num>1 : 
        for i in range (2, num): 
            if (num % i)==0 : 
                break 
        else: 
             print (num) 


#Question7


n1=[] 
for x in range(0 , 500): 
    if (x%7==0) and (x%11==0) : 
        n1.append (str(x))
print (",".join(n1))



#Question8


lst = []
n = 10

for i in range (0,n):
    ele = int(input ("Enter The Number: "))
    lst.append(ele)

#a) postive numbers

print("Positive numbers in", lst, "are: ")
for i in lst:
    if i >= 0:
       print (i, end = " ")

#b) negative numbers
print("\nNegative numbers in", lst, "are: ")
for i in lst:
    if i <= 0:
       print (i, end= " ")

#c) odd numbers
print ("\nodd numbers in", lst, "are: ")
for i in lst:
    if i%2 != 0:
       print (i, end=" ")

#d) even numbers
print("\nEven numbers in", lst, "are: ")
for i in lst:
    if i%2== 0:
        print (i, end = " ")

#e) Number of times each number occurs in the List
for i in lst:
    g=0
    n=0
    if (i=="----"):
        continue

    for j in lst:
        if(i==j):
            n=n+1
            lst [g]='----'
        g=g+1
    print("\n", i," occured ",n," times")




#Question9



user_list = input("Enter the list of words seperated by comma(,):")

word_list = user_list.split(",")

counts = dict()

for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print("Number of occurrences found in the string:",counts[word])