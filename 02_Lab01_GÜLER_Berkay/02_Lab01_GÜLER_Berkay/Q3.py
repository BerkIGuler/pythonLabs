# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 14:14:33 2019

@author: berkay.guler-ug
"""

a=int(input('enter the first integer:'))
b=int(input('enter the second integer:'))
c=int(input('enter the third integer:'))



if a<=b and b<=c:
    if (a+c)/2==b:
        print('\n'+str(b),'is the midpoint of {}, {}, {}'.format(a,b,c))
    else:
        print('\nnone is a midpoint of the others')
        
        
elif a<c and c<b:
    if (a+b)/2==c:
        print('\n'+str(c),'is the midpoint of {}, {}, {}'.format(a,c,b))
    else:
        print('\nnone is a midpoint of the others')
        
      
elif b<c and c<a:
    if (a+b)/2==c:
        print('\n'+str(c),'is the midpoint of {}, {}, {}'.format(b,c,a))
    else:
        print('\nnone is a midpoint of the others')


elif b<a and a<c:
    if (c+b)/2==a:
        print('\n'+str(a),'is the midpoint of {}, {}, {}'.format(b,a,c))
    else:
        print('\nnone is a midpoint of the others')        
        
        
elif c<a and a<b:
    if (b+c)/2==a:
        print('\n'+str(a),'is the midpoint of {}, {}, {}'.format(c,a,b))
    else:
        print('\nnone is a midpoint of the others') 


elif c<b and b<a:
    if (a+c)/2==b:
        print('\n'+str(b),'is the midpoint of {}, {}, {}'.format(c,b,a))
    else:
        print('\nnone is a midpoint of the others')
        
        
else:
    print('\nnone is a midpoint of the others')        