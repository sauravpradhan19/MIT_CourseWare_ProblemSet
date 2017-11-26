#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem Statement for PS1

@author: sauravpradhan19
"""
annual_salary=int(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=int(input("Enter the cost of your dream home:"))
portion_down_payment=0.25
r=0.04
months=0
monthly_salary=annual_salary/12
current_saving=0;
while(portion_down_payment*total_cost>=current_saving):
    current_saving+=monthly_salary*portion_saved
    months+=1
    current_saving+=current_saving*r/12
    print(months,current_saving)
print("Number of months:" ,months)