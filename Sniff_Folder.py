
import os
import shutil
from pathlib import Path
import time 

def check(string, char):

    if char in string:
        result=True
    else:
        result=False
    return result


# Driver Code
s = "Folder.txt"
char = '.'

OriginFolder = Path(input("Folder to be monitored\n")) # Path("C:/Users/Floryna/Desktop/Thomas/essai_python/origin") 
DestinationFolder = Path(input("Saving folder\n")) #Path("C:/Users/Floryna/Desktop/Thomas/essai_python/destination") 

while(1):
   OriginFilesList = os.listdir(OriginFolder)
   DestinationFilesList = os.listdir(DestinationFolder)

   for file_name in OriginFilesList:
      if (check(file_name,'.') is True):#Pour ne copier que les fichiers: personne ne met des . dans les noms de dossier ?!?
         if(not(file_name in DestinationFilesList)):#Si le fichier d'origine n'est pas dans la liste des fichiers du dossier de destination
            shutil.copy(os.path.join(OriginFolder,file_name), os.path.join(DestinationFolder,file_name))
            print("Copied file:\n",file_name)
         else:
            print("No new file to copy\n")
         time.sleep(1)

