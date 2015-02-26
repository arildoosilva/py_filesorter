"""
This is a simple script to sort files and move them to their folders.

HOW TO USE:
1. change the source and destination strings.
    On Windows - drive_letter:/the/path/
    On Linux - /the/path/
2. Copy the if statement, changing the key and the folder.
3. Run
"""

import os
import shutil

source='C:/path/to/source/'
destination='C:/path/to/destination/'

for root, dirs, files in os.walk(source, topdown=False):
    for name in dirs:
        print(name)
    for name in files:
        f_name=os.path.join(root, name)
        print(f_name)
        if 'key' in (name):
            shutil.move(f_name, destination+'folder')