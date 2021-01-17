# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:35:03 2019

@author: berkay.guler-ug
"""

print('this program converts feet and inches to centimeters.')

num_feet=int(input('enter number of feet:'))
num_inches=int(input('enter number of inches:'))
feet_cm=num_feet*12*2.54
inches_cm=num_inches*2.54
total_cm=feet_cm+inches_cm

print('\n{} ft {} in = {} cm '.format(num_feet,num_inches,total_cm))

