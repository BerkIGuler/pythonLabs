# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 13:52:16 2019

@author: b
"""
import datetime

class Friend:
    
    def __init__(self, fname, surname, birth_date, phone):
        self.__fname = fname
        self.__surname = surname
        self.__phone_number = phone
        self.set_birthday(birth_date)
        
    
    def get_fname(self):
        return self.__fname
    
    def get_surname(self):
        return self.__surname
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_birthday(self):
        return self.__birthday
            
    def set_birthday(self,birthDate):
        self.__birthday=datetime.datetime.strptime(birthDate, '%Y-%m-%d').date()
        
    def __lt__(self,other):
        if self.__birthday>other.__birthday:
            return True
        
    def __repr__(self):
        return '\n({})\t{}\t{}\t({})'.format(self.__surname,self.__fname,self.__birthday,self.__phone_number)
    
    
    
    
