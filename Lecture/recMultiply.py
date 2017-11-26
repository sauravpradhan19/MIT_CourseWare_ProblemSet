#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 21:59:40 2017

@author: sauravpradhan19
"""

def mul(a,b):
    if b==1:# Base Case 
        return a;
    else:
        return a + mul(a,b-1)  

print(mul(5,4)) 