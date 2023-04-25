import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil

class ParentWindow (Frame):
    def __init__ (self, master):
        Frame. __init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete (0, END) will clear the content that is inserted in the entry widget
        #this allows the path to be inserted into the entry widget properly.
        self.source_dir.delete(0, END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

        #creates button to select files from source directory
        self.sourceDir_btn=Button(text= "Select Source", width=20, command=self.sourceDir)

        #creates button to select destination of files from destination directory
        self.destDir_btn = Button (text="Select Destination", width=20, command=self.destDir)

    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            shutil.move(source + '/' + i, destination)
            print(i + 'was successfully transferred.')

        #creates button to transfer files
        self.transfer_btn = Button (text="Transfer Files", width=20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

    #creates function to exit program
    def exit_program (self):
        #root is the main gui window, the tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the gui window
        root.destroy()

        self.exit_btn = Button( text="Exit", width=20, command=self.exit_program)
        #position the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        



        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20)
        #Positions source button in the gui using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in gui using tkinter grid() padx and pady are the same
        # the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))                             

        #create button to select destination of files from destination directory
        self.desDir_btn = Button (text="select desitination", width=20)
        #positions destination button in gui using tkinter grid()
        #on the next row under the source button
        self.desDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))
        
 if __name__== "__main__":
     root = tk.Tk()
     App = ParentWindow(root)
     root.mainloop()