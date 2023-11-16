import glob
import re

txt_files = glob.glob("*.txt")
print(txt_files)

inputRegex = input("Enter a Regex: \n")
txtRegex = re.compile(inputRegex)

for filename in txt_files:
    file = open(filename, 'r')
    extract = file.read()
    file.close()
    mo = txtRegex.findall(extract)
    
    if mo :
        print(f'a match has been found in {filename}: {mo}')
    else:
        print("the entered regex doesnot match with any textfiles")    