# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:01:09 2019

@author: berkay.guler-ug
"""

mon=int(input('enter the month (between 1 and 12 inclusive):'))
if mon>0 and mon <= 12:
    if mon == 2:
        print('\n28 days')    
    elif mon == 4 or mon == 6 or mon == 9 or mon == 11 :
        print('\n30 days')
    else:
        print('\n31 days')   
else:
    print('invalid input')
        