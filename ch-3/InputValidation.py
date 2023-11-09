# 2
def collatz(number):
    if number % 2 == 0:
        a = number//2
        print (a) 
        return a
    else:
        b = 3*number+1
        print (b) 
        return b
         
try :
    n = int(input("Enter number: \n"))
    a = collatz(n)
    
    while a != 1:
        a = collatz(a)
       
except ValueError :
    print("Enter a valid integer")
