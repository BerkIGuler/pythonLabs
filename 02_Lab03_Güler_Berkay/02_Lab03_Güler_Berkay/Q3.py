# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:41:07 2019

@author: berkay.guler-ug

"""

from random import randint

def flipCoinUntil_X_Heads(x):
    '''
    flipCoinUntil_X_Heads(x)  takes an integer x
    as parameter and repeatedly flips a coin until x heads in a row are seen and 
    prints all the flips in a row until total number of heads reach x also counts 
    the total number of flips 
    
    
    '''
    global count
    count=0
    i=0
    
    while i!=x:
        
    
        if randint(1,2)==1:
            coin='T'
            print(coin,end=' ')
            count+=1
            i=0
        else:    
            coin='H' 
            print(coin,end=' ')
            count+=1
            i+=1
           
              
while True:
                
    num_heads=int(input('Enter how many heads you want in a row:'))  
    if num_heads<0:
        print('bye')
        break
    flipCoinUntil_X_Heads(num_heads)
    print()       
    print('{} heads in a row! \n{} coins flips in total'.format(num_heads,count))  

    

       
        
        
