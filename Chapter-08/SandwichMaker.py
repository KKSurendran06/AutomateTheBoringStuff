import pyinputplus as pyip

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'])
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
wantCheese = pyip.inputYesNo("Do you want cheese?\n")
if wantCheese == 'yes' :
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'])
wantCondiment = pyip.inputYesNo("Want mayo, mustard, lettuce, or tomato?\n") 
sandWiches_Nos = pyip.inputInt("Wow many sandwiches do you want ? ",min = 1)

price = 0

if breadType == 'wheat':
    price += 20 
elif breadType == 'white':   
    price += 10
elif breadType == 'sourdough':
    price += 5

if proteinType == 'chicken':
    price += 40
elif proteinType == 'turkey':   
    price += 30
elif proteinType == 'ham':
    price += 20       
elif proteinType == 'tofu':
    price += 10   

if wantCheese == 'yes' :
    price += 5 
if wantCondiment == 'yes' :
    price += 5   
    
if sandWiches_Nos:
    price = price + sandWiches_Nos*20          

print(f"The price for your order is: {price}")