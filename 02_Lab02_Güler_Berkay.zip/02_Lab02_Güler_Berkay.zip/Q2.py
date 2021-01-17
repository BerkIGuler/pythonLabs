# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:42:36 2019

@author: berkay.guler-ug
"""

 


num=int(input('int?:'))
sum_=0
factor=0
count=0

while num!=0 :
    
    
    digit=num%10
    if count%2==0 and 1<=num<=9:
        factor=count
    
    elif count%2==0:
        factor=count + 1
    else:   
        factor= count - 1
        
    sum_=sum_+digit*(10**factor) 
    count+=1
    num=num//10
print(sum_)        


        
   
    
    
   
    
    
