import os
import re
import shutil

spam_photos = re.compile(r'(YIFY|YTS)')

for folder, sub, files in os.walk('.'):
    subtitle = 0
    for f in files:

        # if it's the program file
        if(f == 'Movies.py'):
            continue

        print("File: " + f)

        # getting file extension
        filename, extension = os.path.splitext(f)

        # deleting YTS jpegs
        if(extension == '.jpg' and spam_photos.search(filename) != None):
            print("Deleting file: " + f)
            os.remove(os.path.join(os.getcwd(), folder, f))

        else:  # or put continue in above line

            # checking for subtitle files
            if(extension == '.srt'):
                subtitle = 1
                print("Subtitles found")

            # creating source and destination paths
            newname = f'{os.path.basename(folder)}{extension}'
            repstr = os.path.join(os.getcwd(), folder, newname)
            srcstr = os.path.join(os.getcwd(), folder, f)

            #print("\n\nsrc: " + srcstr + "\ndest: " + repstr+"\n\n")

            # renaming files
            if(newname == f'.{extension}'):
                print("Rename failed!")
            else:
                os.rename(srcstr, repstr)

    if(subtitle == 0):
        print("No subtitles found")
