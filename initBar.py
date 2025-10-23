#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 11:59:26 2025

@author: kaiserlee
"""

import numpy as np


# bar represents an initialized bar where tempratures at each particle is determined
# hot sites are coordinates where the temprature is hot
# cold sites are coordinates where the temprature is cold
# Apply hot cold sets the value on hot sites and cold sites to hot and cold on the bar respectively
def applyHotCold(bar,hotSites, coldSites):
    Hot = 50
    Cold = 0
    
    newBar = bar
    
    #set hot and cold
    for x in hotSites:
        newBar[x[1],x[0]] = Hot
    
    for x in coldSites:
        newBar[x[1],x[0]] = Cold
    
    return newBar


# m and n represent coordinates
# hot sites are coordinates where the temprature is hot
# cold sites are coordinates where the temprature is cold
# init bar creates a square grid of height m and width n and applies hot cold to it
def initBar(m,n,hotSites, coldSites):
    Ambient = 25
    
    #initialize bar
    bar = np.full((m,n),Ambient)
    #set bar temp
    bar = applyHotCold(bar,hotSites,coldSites)
    
    return bar

#test
#print(initBar(5,6,[[0,0],[0,1]],[[4,4],[5,4]]))