import os
from pathlib import Path

def createFolder():
    name = input("Please tell your folder name: ")
    p = Path(name)
    if not p.exists():
        p.mkdir()
    else:
        print("Folder with this name already exists.")


def ListFolderAndFile():
    p = Path('')
    items = list(p.rglob('*'))
    for i,v in enumerate(items):
        print(f"{i+1}: {v}")

def FolderNameUpdate():
    ListFolderAndFile()
    o_name = input("Which folder u wnt 2 update")
    old_p = Path(o_name)
    if old_p.exists():
        n_name = input("tell folders new name")
        new_path = Path(n_name)
        if not new_path.exists():
            old_p.rename(new_path)

        else:
            print("This folder name already exists")

    else:
        print("No such folder name exists")


def deleteFolder():
    ListFolderAndFile()
    name = input("which folder you want to delete: ")
    p = Path(name)

    if p.exists():
        p.rmdir()

    else:
        print("No such floder exists")



print('press 1 for creating a folder ')
print('press 2 for Listing files and folder ')
print('press 3 for updating a folder name')
print('press 4 for deletig a folder')
print('press 5 for creating a file')
print('press 6 for reading a file')
print('press 7 for updating a file')
print('press 8 for deletig a file')
print('press 0 to exit the application')

res = int(input('Enter your response: '))

if res == 1:
    createFolder()

if res == 2:
    ListFolderAndFile()

if res == 3:
    FolderNameUpdate()

if res == 4:
    deleteFolder()