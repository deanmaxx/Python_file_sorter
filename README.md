# Python_file_sorter
Version 1 of Python file sorter built on 3.9.0

dependancies: OS, Pathlib - Path

has dictinoary for file types:

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

will not override files that already exist with matching file names - code breaks and throws error.
