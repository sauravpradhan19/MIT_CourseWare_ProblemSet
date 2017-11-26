#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Efficient Method to Compute The Fibbonacci Series 
"""

def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d)+fib_efficient(n-2,d)
        d[n]= ans
        return ans

d= {1:1,2:1}
fib_efficient(6 ,d)
print(d)