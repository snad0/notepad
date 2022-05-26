from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0, END) ##This will delete all the content of this file from ist line zeroth chaar to end


def openFile():
    global file
    file= askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0, END)
        f= open(file, "r" ,encoding="Utf-8")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file== None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file == "":
            file= None
        else:
            #saving new file
            f = open(file, "w", encoding="Utf-8")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file)+ "-notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Pass>>"))
    
def about():
   showinfo("Notepad","This Notepad is created by Nadeem")



if __name__=='__main__':
    root= Tk()
    root.title("Notepad")
    root.geometry("650x400")

    # add text area
    TextArea = Text(root, font= " lucida 12")
    file= None
    TextArea.pack(fill=BOTH,expand=True)


    # menu bar
    menuBar = Menu(root)

    #FILE MENU
    FileMenu= Menu(menuBar, tearoff=0)
    # to open new file 
    FileMenu.add_command(label="New", command= newFile)
    # to open existing file 
    FileMenu.add_command(label="Open", command=openFile)
    # to save existing 
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    menuBar.add_cascade(label="File", menu= FileMenu)
  

    #EDIT MENU
    EditMenu=Menu(menuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu= EditMenu)

    HelpMenu=Menu(menuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    menuBar.add_cascade(label="Help", menu= HelpMenu)



    root.config(menu=menuBar)


    # adding scrollbar
    ScrollBar= Scrollbar(TextArea)
    ScrollBar.pack(side="right",fill=Y)
    ScrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=ScrollBar.set)

    root.mainloop()
