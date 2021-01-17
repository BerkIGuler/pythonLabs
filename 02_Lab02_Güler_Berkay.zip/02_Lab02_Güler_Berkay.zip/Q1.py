# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

message=input('enter your message:')
message=message.lower()

key=int(input('encoding key?:'))
key=key%26


encyrpted_message=''

for i in message:
    i=ord(i)
    if i>=ord('a') and i<=ord('z'):
        i=i+key
        if i>ord('z'):
            i-=26
        encyrpted_message+=chr(i)
    else:
        encyrpted_message+=chr(i)
        
        
        
            
print(encyrpted_message.upper())        
        
            
        
    
