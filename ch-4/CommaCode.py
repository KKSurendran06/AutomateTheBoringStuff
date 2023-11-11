def lis(li):
    try:
        s = ""
        for i in li:
            if i == li[0]:
                s += (f" '{i}, ")
            if i != li[-1] and i!= li[0]:
                s += (f"{i}, ")
        s+= (f"and {li[-1]}'. ")
    except:
        print("give proper input")            

    return s
    
spam = ['apples', 'bananas', 'tofu', 'cats']   
print(lis(spam))
