import tkinter as tk
from tkinter import *
import webbrowser





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid (padx=(10,10) , pady=(10,10))

        self.submit = Entry (width=75)
        self.submit = Button(text="Submit Custom Text", width=30,height=2, command=self.submit)
        self.submit.grid (row=0, column=1, columnspan=2, padx=(10,10), pady= (15, 15))
    
    
        
            
  #tell the Default bHTML Page button to run this function when clicked on.
                       
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

   
   

if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

