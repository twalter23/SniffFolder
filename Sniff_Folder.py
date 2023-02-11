import os, shutil, time
from pathlib import Path

#solve issue 1

#############################################################################
#                                  Check                                    #
#############################################################################
def Check(string, char):#Check si char est contenu dans string
    if char in string:
        result=True
    else:
        result=False
    return result

#############################################################################
#                    ListMissingFilesInFoldAButInFoldB                      #
#############################################################################
def ListMissingFilesInFoldAButInFoldB(FoldAPath,FoldBPath):

   files_A = set([f for f in os.listdir(FoldAPath) if f.endswith('.pdf')])
   files_B = set([f for f in os.listdir(FoldBPath) if f.endswith('.pdf')])

   files_only_in_B = files_B - files_A

   return files_only_in_B

#############################################################################
#                CopyFilesListFromAToBifNotInB                              #
#############################################################################
def CopyFilesListFromAToBifNotInB(FolderA,FolderB,FilesList):

   files_B = set(os.listdir(FolderB))

   for pdf_file in FilesList:
      if pdf_file not in files_B:
         src = os.path.join(FolderA, pdf_file)
         dst = os.path.join(FolderB, pdf_file)
         shutil.copy2(src, dst)

#############################################################################
#                          CopyPdfFromAinBnotInB                            #
#############################################################################
def CopyPdfFromAinBnotInB(APath,BPath):
   Copiedfiles = 0

   files_a = set([f for f in os.listdir(APath) if f.endswith('.pdf')])
   files_b = set([f for f in os.listdir(BPath) if f.endswith('.pdf')])

   files_only_in_a = files_a - files_b

   for file in files_only_in_a:
      src = os.path.join(APath, file)
      dst = os.path.join(BPath, file)
      shutil.copy2(src, dst)

#############################################################################
#                          RenameUniqueDisappearedFiles                     #
#############################################################################
def RenameUniqueDisappearedFiles(FilesList, FolderPath):

   newFilesList = []
   if FilesList is not None:

      for filename in FilesList:
         # Compose the full file path
         file_path = os.path.join(FolderPath, filename)

         # Get the current timestamp
         timestamp = time.strftime("%Y%m%d-%H%M%S")

         # Compose the new file name
         new_filename = "{}_{}".format(timestamp, filename)
         new_file_path = os.path.join(FolderPath, new_filename)

         # Rename the file
         os.rename(file_path, new_file_path)

         # Add the newly renamed file to the list of new files
         newFilesList.append(new_filename)

      return newFilesList

#############################################################################
#                             CopyFilesFolderAtoB                           #
#############################################################################
def CopyFilesFolderAtoB(FilesList,FoldAPath,FoldBPath):

   print(FoldAPath)
   print(FoldBPath)

   if FilesList is not None:
      for filename in FilesList:
         # Compose the source and destination file paths
         src_file = os.path.join(FoldAPath, filename)
         dst_file = os.path.join(FoldBPath, filename)

         print(src_file)

         # Copy the file
         shutil.copy2(src_file, dst_file)

#############################################################################
#                             DeleteFilesFolderA                           #
#############################################################################
def DeleteFilesFolderA(FilesList,FoldPath):  

   if FilesList is not None:
      for filename in FilesList:
         # Compose the full file path
         file_path = os.path.join(FoldPath, filename)

         # Delete the file
         os.remove(file_path)

#############################################################################
#                                Extract                                    #
#############################################################################
def Extract(SniffedFolderPath,DestinationFolderPath,ExtractFolderPath):
   global ExtractFolder

   print("******Extracting*********")
   DisappearedFiles = ListMissingFilesInFoldAButInFoldB(SniffedFolderPath,DestinationFolderPath)
   print(DisappearedFiles)
   ModifiedList = RenameUniqueDisappearedFiles(DisappearedFiles,DestinationFolderPath)
   CopyFilesFolderAtoB(ModifiedList, DestinationFolderPath, ExtractFolderPath)
   DeleteFilesFolderA(ModifiedList, DestinationFolderPath)

#############################################################################
#                                  main                                    #
#############################################################################
SniffedFolderPath = "E:\\11-Projets_Soft\\Python\\SniffFolder\\Sniffed"
DestinationFolderPath = "E:\\11-Projets_Soft\\Python\\SniffFolder\\destination"
ExtractFolderPath ="E:\\11-Projets_Soft\\Python\\SniffFolder\\destination\\Extract"

Resfresh_Read_s = 5 #The time we wait before checking folder
Refresh_Extract_s = 6 #The time we wait before extracting
Readings = 0

start_time = time.time()

while(1):

   print("iteration :",Readings)
   CopyPdfFromAinBnotInB(SniffedFolderPath,DestinationFolderPath)
   Readings+=1

   time.sleep(Resfresh_Read_s)

   if((time.time() - start_time) >= Refresh_Extract_s):
      Extract(SniffedFolderPath,DestinationFolderPath,ExtractFolderPath)
      start_time = time.time()


