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

def createFile():
    name = input("Tell you file name with extension")
    p = Path(name)
    if not p.exists():
        with open(p,'w') as file:
            data = input("What you want to write inside the file... ")
            file.write(data)
            print("File created successfully!!!")

    else:
        print("The file path already exists!!! Please enter a different name.")

def readFile():
    ListFolderAndFile()
    name = input("Enter the name of file which you want to read.. ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p, 'r') as file:
            print(file.read())
        print("File read successfully :)")

    else:
        print("No such file exists!! :( ")

    
def updateFile():
    ListFolderAndFile()
    name = input("Which file you want to updadte?? ")
    p = Path(name)
    if p.exists() and p.is_file():
        print("press 1 for updating the name of the file")
        print("press 2 for overwriting the content")
        print("press 3 for appending the file ")

        check = int(input("TEll your response: "))

        if check == 1:
            new_name = input("ENter the name of the new file ")
            new_p = Path(new_name)
            if not new_p.exists():
                p.rename(new_p)
                print("Name update successfully!! ")

            else:
                print("This name already exists..")

        
        if check == 2:
            with open(p , "w") as file:
                data = input('Enter the data you want to overwrite: ')
                file.write(data)
                print("FIle updata successfully  :)")

        if check == 3:
            with open(p , "a") as file:
                data = input('Enter the data you want to append: ')
                file.write(data)
                print("data appended successfully  :)")
    else:
        print("No such file exists ...")


def deleteFile():
    name  = input("Enter the name of the file you want to delete. ")
    p = Path(name)
    if p.exists() and p.is_file():
        os.remove(p)
        print('file deleted successfully..')
    else:
        print('No such file exists..')

while True:
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

    if res == 5:
        createFile()

    if res == 6:
        readFile()

    if res == 7:
        updateFile()

    if res == 8:
        deleteFile()

    if res == 0:
        break