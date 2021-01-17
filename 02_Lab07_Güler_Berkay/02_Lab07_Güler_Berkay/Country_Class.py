# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:37:07 2019

@author: berkay.guler-ug
"""

class Country:
    
    
    def __init__(self,cname,region,m_emp,f_emp,gdp):
        self.__cname=cname
        self.__region=region
        self.__m_emp=m_emp
        self.__f_emp=f_emp
        self.__gdp=gdp
        
        
        
        
    def getcname(self):
        return self.__cname
    def getregion(self):
        return self.__region 
    def getm_emp(self):
        return self.__m_emp
    def getf_emp(self):
        return self.__f_emp
    def getgdp(self):
        return self.__gdp
    
    
    
    def setm_emp(self,y):
        self.__m_emp=y
    def setf_emp(self,y):
        self.__f_emp=y
    def setgdp(self,y):
        self.__gdp=y
        
    
    

    def get_average_employment(self):
        return (self.__m_emp+self.__f_emp)/2
        
    
    def __repr__(self):
        return '\n\n'+self.__cname+'('+self.__region+') :\n'+'Employment Rate:{:.2f}'.format(self.get_average_employment()) +'\nGDP per person :{:.2f}'.format(self.__gdp)
    
    
    def __gt__(self,other):
        return self.__gdp>other.__gdp
    
    def __eq__(self,other):
        return round(self.get_average_employment())==round(other)
    
    
                
        
        
        
    