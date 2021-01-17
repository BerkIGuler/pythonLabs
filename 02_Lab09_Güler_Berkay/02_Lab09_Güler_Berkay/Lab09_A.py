# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:16:42 2019

@author: berkay.guler-ug
"""

from Friend import Friend
import calendar 
import datetime

def sort_surname(FriendsList):
    suffixStart = 0
    while suffixStart != len(FriendsList):
        for i in range(suffixStart, len(FriendsList)):
            if FriendsList[i].get_surname() > FriendsList[suffixStart].get_surname():
                FriendsList[suffixStart], FriendsList[i] = FriendsList[i], FriendsList[suffixStart]
        suffixStart += 1
        
def find_friend(FriendsList,start,month):
    if len(FriendsList)==start:
        return 
    elif FriendsList[start].get_birthday().month==month:
        print(FriendsList[start])
    find_friend(FriendsList,start+1,month)






def load_friends(filename,List):
    file=open(filename,'r')
    for line in file:   
        line=line[:-1]
        line=line.split() 
        name=line[0]
        surname=line[1]
        birth=line[2]
        no=line[-1]
        List.append(Friend(name,surname,birth,no))
        





        
L=[]       
load_friends('birthday_list.txt',L)    
print('Friends:\n')    
print(L)
print()  
L.sort()
print('Friends by descending birthday:\n')

print(L)
print()
sort_surname(L)
print('Friends by descending surname:\n')
print(L)

month=datetime.datetime.today().month
month_name=calendar.month_name[month]
print('Friends with birthdays in:{}'.format(month_name))
find_friend(L,0,month)



      
        