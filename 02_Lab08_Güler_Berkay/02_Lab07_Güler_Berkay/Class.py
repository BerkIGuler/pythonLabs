# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Vehicle(object):
    __deposit=1000
    
    
    
    def __init__(self,plateNo,price,year):
        self.__plate_no=plateNo
        self.__price=float(price)
        self.__year=year
        
    def getplate(self):
        return self.__plate_no
    def getprice(self):
        return self.__price
    def getyear(self):
        return self.__year
    
    
    def setplate(self,y):
        self.__plate_no=y
    def setprice(self,y):
        self.__price=y
    def setyear(self,y):
        self.__year=y  
        
     
    def calculate_total_cost(self,days):
        cost=days*self.__price
        if self.__year>'2015':
            cost+=Vehicle.__deposit
        return cost

    def __repr__(self):
        return '\n'+self.__plate_no+'\n'+'Price: {}  ({})'.format(self.__price,self.__year)+'\n'
    
    
class Car(Vehicle):
    
    def __init__(self,plateNo,price,year,brand,model):
        Vehicle.__init__(self,plateNo,price,year)
        self.__brand=brand
        self.__model=model
        
    def getbrand(self):
        return self.__brand
    def getmodel(self):
        return self.__model
    
    
    def setbrand(self,y):
        self.__brand=y 
    def setmodel(self,y):
        self.__model=y 
        
    def __repr__(self):
        return '\ncar:'+Vehicle.__repr__(self)+'{}({})'.format(self.__brand,self.__model)+'\n'
    
    
class Bus(Vehicle):
    
    
    def __init__(self,plateNo,price,year,seats):
        Vehicle.__init__(self,plateNo,price,year)
        self.__seats=int(seats)
       
        
    def getseats(self):
        return self.__seats
    
    
    def setseats(self,y):
        self.__seats=y 
        
    def find_type(self):
        if self.__seats>40:
            return 'FullSize Bus'
        elif 20<=self.__seats<=40:
            return 'MidiBus'
        else:
            return 'MiniBus'
        
    def __repr__(self):
        return Vehicle.__repr__(self)+Bus.find_type(self)
        
        
        
        
        
        
            
        
        
  
        
        
        
        
        
        
        
