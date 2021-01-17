# -*- coding: utf-8 -*-

from random import randint

def randomOdd(lower,upper):
    '''
    randomOdd takes two parameters, the lower and upper bounds of a range, 
    generates and returns a random odd integer in that
    range inclusive
    '''
    i=0
    
    while i==0:
        num=randint(lower,upper)
        if not num%2==0:
            i=1
            return num
            
        
print(randomOdd(1,10))


lower_bound=int(input('Enter the lower bound of the range:'))
upper_bound=int(input('Enter the upper bound of the range:'))
number_of_odds=int(input('How many odd integers do you want in this range:'))
print()

odd_numbers=''
for x in range(number_of_odds):
    odd=randomOdd(lower_bound,upper_bound)
    odd_numbers+=str(odd)
    odd_numbers+='  '
    
       
print('Here are {} random odd integers in range[{}, {}]:'.format(number_of_odds,lower_bound,upper_bound),odd_numbers )
