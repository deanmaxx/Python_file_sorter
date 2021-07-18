import os
from pathlib import Path
#dictionary of file typles and how to sort them
SUBDIRECTORIES = {
    "DOCUMENTS":['.pdf','.rtf','.txt'],
    "AUDIO":['.m4a','.m4b','.mp3','.wav'],
    "VIDEOS":['.mov','.avi','.mkv','.mp4'],
    "IMAGES":['.jpg','.jpeg','.png','.psd'],
    "RDP":['.rdp'],
    "ISO":['.iso'],
    "APPLICATIONS":['.exe','.msi'],
    "COMPRESSED FILES":['.zip','.tar','.7z'],
    "DATABASE":['.bak','.sql'],
    "PROGRAMMING":['.py','.js']
}
#asking user if they would like to run organizer on directory
dir_path = os.path.dirname(os.path.realpath(__file__))
print("File Organizer will be run on the directory " + dir_path)
print("Enter Yes to continue.. or No to exit")
answer = input()
if answer == "yes": 
        #category  sorter code
    def pickDirectory(value):
        for category, suffixes in SUBDIRECTORIES.items():
            for suffix in suffixes:
                if suffix == value:
                    return category
        return 'MISC'
    #text for humans
    print("Organizer ran")
    #scanning, making directories and moving files code
    def organizeDirectory():
        for item in os.scandir():
            if item.is_dir():
                continue
            filePath = Path(item)
            filetype = filePath.suffix.lower()
            directory = pickDirectory(filetype)
            directoryPath = Path(directory)
            if directoryPath.is_dir() != True:
                directoryPath.mkdir()
            filePath.rename(directoryPath.joinpath(filePath))
    #program run
    organizeDirectory() 
elif answer == "no": 
    quit()
else: 
    print("Please enter yes or no.") 


