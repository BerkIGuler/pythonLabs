# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:13:48 2019

@author: berkay.guler-ug
"""

def persistence(num):
    '''
    the function ,persistence, takes a positive parameter num and 
    returns its multiplicative persistence, which is the number of times you 
    must multiply the digits in num until you reach a single digit.
    '''
    count=0
    last_digit=0
    new_num=1
    while num>10:
        new_num=1
        while True:
            
            last_digit=num%10
            new_num*=last_digit
            num=num//10
            if num==0:
                num=new_num
                count+=1
                break
                
    return count 



integer=int(input('enter an int:'))

print('multiplicative persistence of {} is {}'.format(integer,persistence(integer)))           