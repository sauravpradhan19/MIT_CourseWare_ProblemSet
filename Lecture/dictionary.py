#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:21:25 2017

@author: sauravpradhan19
"""
def lyrics_to_frequency(lyrics):
    lyricF={}
    for word in lyrics:
        if word in lyricF:
            lyricF[word]+=1
        else:
            lyricF[word]=1
    return lyricF

lyrics="Heal the world make it a better place for you and for me and the entire human race"
lyrics=lyrics.split()
lyricF=lyrics_to_frequency(lyrics)
print(lyricF)