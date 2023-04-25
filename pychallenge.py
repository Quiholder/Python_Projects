import tkinter as tk
from tkinter import *

class ParentWindow (Frame):
    def __init__ (self, master):
        Frame. __init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")




if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    


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
    
