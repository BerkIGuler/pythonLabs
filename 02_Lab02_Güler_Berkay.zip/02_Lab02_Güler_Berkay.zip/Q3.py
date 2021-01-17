# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:18:23 2019

@author: berkay.guler-ug
"""


num_rec=int(input('how many rectangles?:'))
sum_area=0
rec=1
for a in range(num_rec):
    w=int(input('width {} ?:'.format(rec)))
    l=int(input('lenght {} ?:'.format(rec)))
    for x in range(1,w+1):
        
        for a in range(1,l+1):
            print('*',end='')
        print()  
    rec+=1    
        
    
    
    sum_area+=w*l
    
print('\nTotal area:',sum_area)    