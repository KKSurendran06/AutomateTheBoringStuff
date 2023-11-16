import os, shutil
from pathlib import Path

file_format = input("Enter a file format: ")
   
path = Path.cwd()   
destiantionFolder = path / 'newFile'

if not destiantionFolder.exists():
    destiantionFolder.mkdir()

try:
    for folderName, subFoldername, fileName in os.walk(path):
        for filename in fileName:
            if filename.endswith(file_format):
                file_path = Path(folderName) / filename
                shutil.copy(file_path, destiantionFolder)
except:
    print("The entered file format does not exsist")            
            