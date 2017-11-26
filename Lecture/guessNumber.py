#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:56:38 2017

@author: sauravpradhan19
"""
print("Guessing the root of the number")
number = int(input("Enter the no. whose root you want to find"))
for i in range(number+1):
    if i**3==number:
        print(str(i) + " is the cube root of the number")