# SniffFolder

Code that monitors the content of a folder with the directory variable SniffedFolderPath variable.

If a new pdf file arrives it makes a copy to DestinationFolderPath variable.

If the newly arrived pdf in SniffedFolderPath is deleted, a copy of it is made in ExtractFolderPath.

For final user, interesting files are then stored in ExtractFolderPath. DestinationFolderPath is 

only needed for good working of the script.

![PinMaker Doc](Doc/Doc.png "Doc")