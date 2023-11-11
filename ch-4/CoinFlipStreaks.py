import random

li = [] 
numberOfStreaks = 0
Hcounter = 0
Tcounter = 0


for experimentNumber in range(10000):
    if random.randint(0, 1) == 1:
        li.append("H")
    else:
        li.append("T")    

for i in li:
    if i=="H":
        Hcounter += 1
        Tcounter = 0
    else:
        Tcounter += 1
        Hcounter = 0
    
    if Hcounter==6 or Tcounter == 6:
        numberOfStreaks += 1
        
print('Chance of streak: %s%%' % (numberOfStreaks / 100))        