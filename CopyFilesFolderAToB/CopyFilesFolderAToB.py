import shutil,os

def Copy(List,A,B):

    for filename in List:
        # Compose the source and destination file paths
        src_file = os.path.join(A, filename)
        dst_file = os.path.join(B, filename)
        
        print(src_file)

        # Copy the file
        shutil.copy2(src_file, dst_file)


folderA = "E:\\11-Projets_Soft\\Python\\SniffFolder\\destination"
folderB = "E:\\11-Projets_Soft\Python\\SniffFolder\\CopyFilesFolderAToB\\FoldB"
filesList = ["1.pdf"]

print(filesList)

Copy(filesList,folderA,folderB)