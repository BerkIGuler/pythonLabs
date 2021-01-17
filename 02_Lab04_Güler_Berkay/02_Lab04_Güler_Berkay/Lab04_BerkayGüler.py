# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:14:44 2019

@author: berkay.guler-ug
"""

from ed_functions import *

char=input('enter start and end characters:')



file1=open('education.txt','r')
outfile=open('{}to{}_equel_ed.txt'.format(char[0],char[1]),'w')

for line in file1:   
    if same_education(get_levels(line)[0],get_levels(line)[1]) and char[0]<=line[0]<=char[1]:
        outfile.write(get_country_region(line)[0]+'\t'+get_country_region(line)[1]+'\n')
        
outfile.close()        
file1.close()

