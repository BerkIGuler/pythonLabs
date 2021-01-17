# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:49:57 2019

@author: berkay.guler-ug
"""

from Country_Class import Country


countries=[]

file1=open('un_data.txt','r')
file1.readline()
for line in file1:
    line = line[:-1].split(',')
    name=line[-2]
    region=line[-1]
    gdp=float(line[0])
    male=float(line[1])
    fem=float(line[2])
    countries.append(Country(name,region,male,fem,gdp))
 
countries.sort()  
  
print(countries)    
    
av=float(input('average employment rate:'))
dummy=Country('DUMMYLAND','DUMM',av,av,10000)
try:
    print(countries[countries.index(dummy.get_average_employment())])
except:
    print('no country found')    








reg=input('enter a region:')
min_gdp,max_gdp=float(input('enter min gdp to search:')),float(input('enter max gdp to search:'))

print('Countries in {} with gdp between {} and {}'.format(reg,min_gdp,max_gdp))

for country in countries:
    if  min_gdp<country.getgdp()<max_gdp and country.getregion()==reg:
        print(country.getcname())
        
        
     
    
    














