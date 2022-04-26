# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# A Python Program to find average of three numbers input by User
#Made by Esharpreet Singh
#SID-21108030
#Branch-Metallurgy
#College-Punjab Engineering College

#Q1
a=int(input("Enter 1st number="))
b=int(input("Enter 2nd number="))
c=int(input("Enter 3rd number="))

print("The average is=",(a+b+c)/3)


#Q2
Gross_Income=int(input("Enter the Gross Income="))
Number_of_Dependents=int(input("Enter the number of Dependents="))

Taxable_Income=Gross_Income-10000-(3000*(Number_of_Dependents))
Tax=Taxable_Income*0.2
print("The Tax to be paid is",Tax)



#Q3
SID=int(input("Enter the SID="))
Name=input("Enter Your Name=")
print("For Male-Enter M")
print("For Female-Enter F")
print("For Unknown-Enter U")
def Gen():
    Gender=input("Enter your Gender")
    if Gender==("M" or "F" or "U"):
       print("Valid Gender has been entered")
       return Gender
    else:
       print("Invalid Gender has been entered")
       print("Enter your Gender again")
       return Gen()
Gender=Gen()
Course_Name=input("Enter the Course Name=")
CGPA=input("Enter your CGPA=")
print("The List is created as-[SID,Name,Gender,Course Name,CGPA]")
lst=[SID,Name,Gender,Course_Name,CGPA]
print(lst)
   

     
#Q4
marks1=int(input("Enter the marks of 1st Student="))
marks2=int(input("Enter the marks of 2nd Student="))
marks3=int(input("Enter the marks of 3rd Student="))
marks4=int(input("Enter the marks of 4th Student="))
marks5=int(input("Enter the marks of 5th Student="))
lst=[marks1,marks2,marks3,marks4,marks5]
print("The list of marks is",lst)


#Q5
colour=["Red","Green","White","Black","Pink","Yellow"]
#A Part
new_list=colour[:]
print(colour)
a=colour.pop(3)
print(colour)
#B Part
new_list[3:5]="Purple"
print(new_list)
