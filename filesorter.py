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

the_list=[('photo', 'My Pictures'), ('video', 'My videos')]

file_list=[f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
for file_to_move in file_list:
    for x in the_list:
        string_to_match=x[0]
        sub_folder=x[1]
        if string_to_match.lower() in (file_to_move.lower()):
            print('File', file_to_move, 'was moved to', destination+sub_folder)
            shutil.move(destination+file_to_move, destination+sub_folder)