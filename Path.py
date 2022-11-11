
import os
import shutil
from pathlib import Path

def check(string, char):

    if char in string:
        result=True
    else:
        result=False
    return result


# Driver Code
s = "Folder.txt"
char = '.'

Origin = Path("C:/Users/Floryna/Desktop/Thomas/essai_python/origin") #input("Folder to be monitored\n")
Destination = Path("C:/Users/Floryna/Desktop/Thomas/essai_python/destination") #input("Saving folder\n")

OriginFilesList = os.listdir(Origin)
DestinationFilesList = os.listdir(Destination)

print(OriginFilesList)

