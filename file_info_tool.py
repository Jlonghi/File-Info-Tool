
#!/usr/bin/env python
import hashlib


# File Info Tool 
def md5File(filePath):
    try:
        file = open(filePath)
        hash = hashlib.md5()
        hash.update(file.read())
        return hash.hexdigest()
    except IOError:
        print('Could not find file')