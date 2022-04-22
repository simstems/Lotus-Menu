from inspect import unwrap
import os
import sys
import time
import subprocess
import csv
import pandas as pd
from pathlib import Path
from tkinter import Tk as tink
from tkinter import ttk as tinky
from tkinter import Frame, Menu, Entry, IntVar, Checkbutton, Button, PhotoImage, Label, StringVar, END

'''

https://www.flaticon.com/free-icons/lotus Lotus icons created by Freepik - Flaticon (https://www.flaticon.com/free-icon/lotus_184257#)

A modular program that runs programs and scripts placed in it's directory folder.

'''
# Directory controls
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # Script's root directory
CONFIG_PATH = os.path.join(ROOT_DIR, 'Directory') # Programs directory

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title('Lotus Boot Menu')
        self.master.iconphoto(False, PhotoImage(file="./CoreMedia/lotus.png"))
        self.master.geometry('{}x{}'.format(500, 185)) # Width x Height
        self.master.resizable(False, False)

        # allowing the widget to take the full space of the root window
        self.grid()

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu, bg='#fffafa')

        # Add menu member "file"
        file = Menu(menu)
        menu.add_cascade(label="File", menu=file)

        # Add items to "file" member
        file.add_command(label="Open")
        file.add_command(label="Exit", command=self.client_exit)
        

        # Add menu member "edit"
        edit = Menu(menu)
        menu.add_cascade(label="Edit", menu=edit)

        # Add items to "edit" member
        edit.add_command(label="Refresh", command=self.scan_directory)

        # Add menu member "toolbox"
        toolbox = Menu(menu)
        menu.add_cascade(label="Toolbox", menu=toolbox)
        
        # Add items to "toolbox" member
        toolbox.add_command(label="AntiMalware")
            
    def client_exit(self):
        exit()
    
    # Scan for changes in Directory folder in order to update menu
    # Generate CSV of Toolbox menu structure built base on scan
    def scan_directory(self):
        dir_list = []
        def listdirs(CONFIG_PATH):
            for it in os.scandir(CONFIG_PATH):
                if it.is_dir():
                    dir_list.append(it.path)
                    listdirs(it)
                else:
                     dir_list.append(it.path)
        listdirs(CONFIG_PATH)
        self.wrap_CSV(dir_list)
       
    # Wrap CSV using Pandas
    def wrap_CSV(self, myData):
        # Store list in DataFrame
        df = pd.DataFrame(myData)     
        # Save to the DataFrame 
        df.to_csv('.\CoreMedia\dump\dir_list.csv')

    # Unwrap CSV using Pandas
    def unwrap_CSV(self, myCSV):
        # Store data from CSV in DataFrame
        df = pd.read_csv(myCSV)
        return df
    
    def createMenu(self):
        self.scan_directory()
        data = self.unwrap_CSV(".\CoreMedia\dump\dir_list.csv")
        

# Create function for "browse folder" button
def browse_folder():
    subprocess.Popen(r'explorer ' + CONFIG_PATH)

# Initialize "window" with Tkinter
window = tink()

# create all of the main containers
top_frame = Frame(window, bg='#fffafa', width=450, height=40, pady=3)
center = Frame(window, bg='#fffafa', width=450, height=40, pady=3)
btm_frame = Frame(window, bg='#fffafa', width=450, height=40, pady=3)

# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)


top_frame.grid(row=0, sticky="ew")
center.grid(row=1)
btm_frame.grid(row=2, sticky="ew")

# create the widgets for the center
cnButton = Button(center, width=20, height=2, text='Browse Folder', bg='#fff0f0', font=('arial', 10, 'normal'), command=browse_folder) # command=open_Explorer

# layout\Display the center widgets
cnButton.grid(row=0, column=0)

#creation of an instance for window menu
app = Window(window)

#END, Open Window
window.mainloop()
