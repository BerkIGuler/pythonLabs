# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""






def get_levels(data):
    pos=()
    for i in range(len(data)):
        if data[i]=='\t':
            pos+=(i,)
    if '\n' in data:
        pos1=data.find('\n')
        f_ed=data[pos[2]+1:pos1]
    else:
        f_ed=data[pos[2]+1:]        
    m_ed= data[pos[1]+1:pos[2]]
    return (float(m_ed),float(f_ed))

    
   
    
def same_education(m,f):
    if round(m)==round(f):
        return True
    else:
        return False
        
    
    
def get_country_region(data):
    pos=()
    for i in range(len(data)):
        if data[i]=='\t':
            pos+=(i,)
    country=data[:pos[0]]   
    region=data[pos[0]+1:pos[1]]    
    return (country,region)
        
    
    
    
    
    
    
    
    
    
    