#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun June
@author: sauravpradhan19
"""
#Modified Program to predict the root of a num
print("Guessing the root of the number")
number = int(input("Enter the no. whose root you want to find"))
epsilon =0.01
increment=0.01
no=1
guess=0
while abs(no**3-number)>=epsilon and number>=no**3:
    guess+=1
    no+=increment
print("The no. of guesses = ",guess)
if (no**3-number)>=epsilon:
    print("Could not predict the cube root with accuracy")
else:
    print("The Cube root of the number",no)