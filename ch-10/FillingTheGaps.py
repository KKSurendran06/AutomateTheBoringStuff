import glob, re, shutil
from pathlib import Path

find = glob.glob("*00?.txt")
find.sort()
path = Path.cwd()

fetchName = re.compile(r'[a-zA-Z]+')
mo = fetchName.search(str(find))
file_name_str = mo.group()

for count,file in enumerate(find,1):
    new_name = file_name_str+'00'+f'{count}'+'.txt'
    source = path / file
    destination = path / new_name
    shutil.move(source, destination)
    