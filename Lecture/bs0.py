#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finger Exercise - PythonIsLove
"""

s='1.23,2.4,3.123'
s+=','
counter=0;
summer=0;
for i in range(len(s)):
    if(s[i]==','):
        summer+=float(s[counter:i])
        counter=i+1;
print(summer)