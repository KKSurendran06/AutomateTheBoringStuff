import re

def isStrong(passw):
    count = 0
    a = b = c = False

    for char in passw:
        if char.isupper():
            a = True   
        
        if char.islower():
            b = True
        
        if char.isdigit():
            c = True          
        
    if a :
        count+=1
    if b :
        count+=1
    if c :
        count+=1        
     

    if count == 3:
         print("Password is strong")
    else:
         print("Password is not strong")        

passwordRegex = re.compile(r'.{8,}')       
mo = passwordRegex.search('AAAAaa0a')
password = mo.group()         
isStrong(password)    
                     
        
        
    
