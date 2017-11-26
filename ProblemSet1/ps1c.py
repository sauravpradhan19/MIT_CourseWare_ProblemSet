#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Statement for PS1

@author: sauravpradhan19
"""
annual_salary=int(input("Enter your annual salary:"))
high=1;
low=0;
portion_saved=0.5
current_saving=0;
steps=0;
while not(current_saving>=249900 and current_saving<=250100):
    total_cost=1000000
    semi_annual_raise=.07
    portion_down_payment=0.25
    r=0.04
    months=0
    monthly_salary=annual_salary/12
    current_saving=0;
    flag=1
    for i in range(0,36):
        current_saving+=monthly_salary*portion_saved + current_saving*r/12
        months+=1
        if(months%6==0):
            monthly_salary+=monthly_salary*semi_annual_raise
    print(current_saving,portion_saved)
    if(portion_saved==1 and current_saving<=249900):
        print("It is not possible to pay the down payment in three years")
        flag=0
        break
    if(current_saving<=249900):
        low=portion_saved
        portion_saved=(high+low)/2
    elif(current_saving>=250100):
        high=portion_saved
        portion_saved=(high+low)/2      
    steps+=1     
if flag:
    print("Best Savings rate",portion_saved)
    print("Steps in bisection search:",steps)    