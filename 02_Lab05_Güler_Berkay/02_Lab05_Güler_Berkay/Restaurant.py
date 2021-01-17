3# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

infile=open('restaurants.txt','r')

rest={}

for line in infile:
    if line[-1]=='\n':
        line=line[:-1]
    line=line.split(',')
      
    star=line[0]
    if star not in rest:
        rest[star]=[(line[1],line[2])]
    else:
        rest[star].append((line[1],line[2]))

print(rest)
print('1)Update rating of restaurant\n2)Update phone number of restaurant\n3)Exit')
choice = int(input('choice:'))    

while choice!=3:
    if choice==1:
        (restaurant,rating)=input('enter restaurant name:'),input('enter new rating:')
        for key in rest:
            for  tupl in rest[key]:
                if tupl[0]==restaurant:
                    rest[key].remove(tupl)
                    rest[rating].append(tupl)
                    
                    
                    
    elif choice==2:
        (restaurant,num)=input('enter restaurant name:'),input('new phone number:')
        for key in rest:
            for  tupl in rest[key]:
                if tupl[0]==restaurant:
                    rest[key].remove(tupl)
                    tupl=(restaurant,str(num))
                    rest[key].append(tupl)
                    
                    
                    
    print(rest)                    
    print('1)Update rating of restaurant\n2)Update phone number of restaurant\n3)Exit')                
    choice = int(input('choice:'))   
                     
    
        


