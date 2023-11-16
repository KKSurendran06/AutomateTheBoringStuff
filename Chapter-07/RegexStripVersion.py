import re

def regexStrip(str, remove):
    if remove == "":
        stripRegex = re.compile(r'^\s+|\s+$')
        mo = stripRegex.sub("", str)
        return mo
    else:
        stripRegex = re.compile(rf'{remove}')
        mo = stripRegex.sub("", str)
        return mo


string = "Hello"
char = "e"
print(regexStrip(string,char))
