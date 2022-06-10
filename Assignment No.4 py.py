# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 22:59:08 2022

@author: Dell
"""

a=int (input ("Enter your marks"))
if a>80 :

     print ("Your grade is A")
elif 60<a<=80 :

     print("Your grade is B")

elif 50<a<=60 :

     print ("Your grade is C")

elif 45<a<=50:

     print ("Your grade is D")

elif 25<a<=45 :

     print("Your grade is E")
     
else :
     print("your grade is F")
     
     
     
     
     

b= int (input("\n \n Enter a year")) 
if (b%4==0 and b%100 !=0) or b%400==0:
    print("It is a leap year")

else:    
    print("It is not a leap year")
      
      
      
      

import random
print("\n \n You will get 10 random multiplication questions")

n=0

for n in range (0,10):
    c=random.randint(1,30)

    d=random.randint(1,10)

    print("First number is : ", c) 
    print("Second number is : ", d)
    f=int (input("Your answer is: "))
    e=c*d

    if f==e:
        print ("Your answer is right")

    else:
        print("Your answer is wrong in The correct answer is: ",e)
    n=n+1

    


r=1
while r<200:

    if (r%5==2) and (r%6==3) and (r%7==2):

       print("in in The number of candies in a halloween bowl are",r)
    r=r+1   