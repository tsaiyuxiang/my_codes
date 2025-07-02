'''
In a file called extensions.py, implement a program that prompts the user
for the name of a file and then outputs that file’s media type if the file’s
name ends, case-insensitively, in any of these suffixes:

.gif    .jpg    .jpeg   .png    .pdf    .txt    .zip

If the file’s name ends with some other suffix or has no suffix at all, output
 application/octet-stream instead, which is a common default.
'''
from unittest import case

file_name = input("Enter file name: ")
len = len(file_name)
dot_index = file_name.rfind(".")
if (dot_index == -1) or (dot_index == len-1) :
    extension = ""
else:
    extension = file_name[dot_index:]
    print(f"File extension: {extension}")

match extension:
    case ".gif":
        media_type = "image/gif"
    case ".jpg":
        media_type = "image/jpeg"
    case ".jpeg":
        media_type = "image/jpeg"
    case ".png":
        media_type = "image/png"
    case ".pdf":
        media_type = "application/pdf"
    case ".txt":
        media_type = "text/plain"
    case ".zip":
        media_type = "application/zip"
    case _:
        media_type = "application/octet-stream"

print(f"File media_type: {media_type}")

