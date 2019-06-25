import os
import tkinter
from tkinter import filedialog
from pathlib import Path
from os.path import isfile, join, splitext, basename

class fileDesc:
    def __init__(self, dirPath, fileObj):
        self.fullPath = dirPath
        self.filePath = dirPath / fileObj
        self.fileName = basename(self.filePath)

def blackDiamondFind(obj):
    if(obj.find("16-") > -1):
        return (obj[obj.find("16-"):])
    elif(obj.find("17-") > -1):
        return (obj[obj.find("17-"):])
    elif(obj.find("18-") > -1):
        return (obj[obj.find("18-"):])
    else:
         return obj
def main():
    tkinter.Tk().withdraw()
    dirPath = Path(filedialog.askdirectory(title = 'Select directory to trim file names...'))
    fileList = []
    for path, folders, _ in os.walk(dirPath):
        for name in folders:
            fileList.append(fileDesc(Path(path),name))
    for folder in fileList:
        os.rename(folder.filePath, folder.fullPath / blackDiamondFind(folder.fileName))
if(__name__ == "__main__"):
    main()