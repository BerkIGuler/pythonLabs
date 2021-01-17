# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:09:51 2019

@author: berkay.guler-ug
"""

from Class import Vehicle
from Class import Bus
from Class import Car



def read_vehicles(name):
    infile=open(name,'r')
    for line in infile:
        line=line[:-1]
        line=line.split(',')
        if line[0]=='V':
            L.append(Vehicle(line[1],line[2],line[3]))
        elif line[0]=='C':
            L.append(Car(line[1],line[2],line[3],line[4],line[5]))
        else:
            L.append(Bus(line[1],line[2],line[3],line[4]))
            
L=[]    
read_vehicles('vehicles.txt')
print(L)     

days =int(input('Enter number of days to rent bus:'))
limit =float(input('Enter Limit:'))
print('Busses with total rental cost under {}:'.format(limit)) 
countBus=0
for i in L:
    if isinstance(i,Bus):
        countBus+=1
        if i.calculate_total_cost(days)<limit:
            print(i)
            
print('Number of Buses:',countBus)    
        
            
    