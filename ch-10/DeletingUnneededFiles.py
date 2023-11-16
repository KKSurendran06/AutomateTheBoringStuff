import os
from pathlib import Path

path = Path.cwd()

for folderName,subFolder,fileNames in os.walk(path):
    for filename in fileNames:
        file_path = Path(folderName) / filename 
        fileSize = os.path.getsize(file_path)
        sizeInMb = fileSize/ (1024*1024) 
        if sizeInMb > 100:
           absPath = Path(folderName) / filename
           print(f" the path where large files are stored are{absPath}")
        