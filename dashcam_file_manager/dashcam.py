'''
dashcam.py
Multi-use script to rename and move files from my dashcam
'''
import os
import tkinter as tk
from tkinter import StringVar, filedialog
import shutil
import re

class Main:
    
    def __init__(self):
        # initialize window and define properties
        self.i = 0
        self.root = tk.Tk()
        self.root.title("Python dascham file management script v1.0")
        self.directories = [None, None]
        self.srcStrVar = StringVar()
        self.destStrvar = StringVar()
        self.srcStrVar.set("None")
        self.destStrvar.set("None")
        return None

    def getDirectory(self):
        # get directory through file dialog
        if self.i == 0:
            self.directories[self.i] = filedialog.askdirectory()
            self.srcStrVar.set(self.directories[self.i])
            self.i += 1
            return self.directories
        else:
            self.directories[self.i] = filedialog.askdirectory()
            self.destStrvar.set(self.directories[self.i])
            self.i = 0
            return self.directories

    def addUI(self):
        # title text
        titleFrame = tk.Frame(self.root)
        titleText = tk.Label(titleFrame, text="Python Dashcam Management Script", font=("Helvetica",20)).pack(padx=20, pady=20)
        titleFrame.pack(side=tk.TOP)
        # source directory
        sourceFrame = tk.Frame(self.root)
        sourceText = tk.Label(sourceFrame, text="Source directory: ", font=("Helvetica", 15)).pack(side=tk.LEFT)
        sourceBtn = tk.Button(sourceFrame, text="Select Directory", command=self.getDirectory).pack(side=tk.RIGHT)
        self.currentSource = tk.Label(sourceFrame, textvariable=self.srcStrVar).pack(side=tk.BOTTOM, padx=5)
        sourceFrame.pack(side=tk.TOP)
        # destination directory
        destinationFrame = tk.Frame(self.root)
        destinationText = tk.Label(destinationFrame, text="Destination directory: ", font=("Helvetica", 15)).pack(side=tk.LEFT)
        destinationBtn = tk.Button(destinationFrame, text="Select Directory", command=self.getDirectory).pack(side=tk.RIGHT)
        self.currentDestination = tk.Label(destinationFrame, textvariable=self.destStrvar).pack(side=tk.BOTTOM, padx=5)
        destinationFrame.pack(side=tk.TOP)
        # start script
        scriptFrame = tk.Frame(self.root)
        scriptBtn = tk.Button(scriptFrame, text="Run script", command=self.root.destroy).pack()
        scriptFrame.pack(side=tk.BOTTOM, padx=20, pady=20)
        return self.root

    def moveFiles(self):
        # move files from source to destination
        print(f"Moving files from {self.directories[0]} to {self.directories[1]}...\n")
        for file in os.scandir(self.directories[0]):
            if file.is_file():
                shutil.move(file, self.directories[1])
            else:
                # if the file doesnt exist (for some reason)
                print(f"{file} Does not exist.\n")
            pass
        # confirmation
        print("Move operation successful\n")
        return None

    def renameFiles(self):
        return None
    pass

classObj = Main()
classObj.addUI()
classObj.root.mainloop()
classObj.moveFiles()
classObj.renameFiles()