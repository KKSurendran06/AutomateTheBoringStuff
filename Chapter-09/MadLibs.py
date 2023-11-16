import re

content = open('Madlibs.txt', 'w')
content.write('The ADJECTIVE panda walked to the NOUN and then VERB.\n A nearby NOUN was, unaffected by these events.')
content.close()

content = open('Madlibs.txt', 'r')
data = content.read()
content.close()

dataRegex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")
mo = dataRegex.findall(data)

replaceData = data 

for i in mo:
        replaceStr = input(f"Enter an {i.lower()}: ")
        replaceRegex = re.compile(rf'{i}')
        replaceData = replaceRegex.sub(replaceStr, replaceData, count =1)
        
        
print(f"Here is the replaced sentance\n{replaceData}")
replacedContent = open('Madlibs2.txt', 'w')
replacedContent.write(replaceData)
replacedContent.close()