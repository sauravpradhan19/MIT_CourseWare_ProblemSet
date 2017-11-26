 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:08:12 2017

@author: sauravpradhan19
"""

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(3)) 