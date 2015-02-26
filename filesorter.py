"""
This is a simple script to sort files and move them to their folders.
HOW TO USE:
1. change the source and destination strings.
 On Windows - drive_letter:/the/path/
 On Linux - /the/path/
2. Add values to the list, the first one is the key string in the file, the second is the destination folder.
3. Run.
"""

import os
import shutil

source='C:/path/to/source/'
destination='C:/path/to/destination/'

the_list=[['photo', 'My Pictures'], ['video', 'My Videos']]

try:
    for root, dirs, files in os.walk(source):
        for name in dirs:
            print(name)
        for name in files:
            f_name=os.path.join(root, name)
            for x in the_list:
                if x[0].lower() in (name.lower()):
                    shutil.move(f_name, destination+x[1])
except Exception:
    pass
