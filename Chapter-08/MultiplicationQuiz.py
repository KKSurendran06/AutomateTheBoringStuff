import pyinputplus as pyip
import random
import time

count = 0
max_tries = 3

for i in range(10):
    nos_1 = random.randint(0,9)
    nos_2 = random.randint(0,9)
    try:
        for attempts in range (max_tries):
            problem = pyip.inputNum(f"what is {nos_1} * {nos_2} ",timeout=8)
            if problem == nos_1*nos_2:
                print("Correct")
                count += 1
                time.sleep(1)
                break
            else:
                print("Incorrect try again!")
    except pyip.TimeoutException:
        print("Out of time!")

print(f"Congrats your score is {count}")        
        
            
    