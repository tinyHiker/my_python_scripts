# import modules
import customtkinter
from customtkinter import *
import winapps
 
 
customtkinter.set_appearance_mode('dark')

# function to attach output 
def app():
    for item in winapps.search_installed(e.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        uninstall_string.set(item.uninstall_string)
        return
    
    
    
    
 
 
# object of tkinter
# and background set for grey
master = CTk()
master.configure(bg='light grey')
 
# Variable Classes in tkinter
name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()
 
 
# Creating label for each information
# name using widget Label
CTkLabel(master, text="Enter App name : ").grid(row=0, sticky=W)
CTkLabel(master, text="Name : ").grid(row=2, sticky=W)
CTkLabel(master, text="Version :").grid(row=3, sticky=W)
CTkLabel(master, text="Install date :").grid(row=4, sticky=W)
CTkLabel(master, text="publisher :").grid(row=5, sticky=W)
CTkLabel(master, text="Uninstall string :").grid(row=6, sticky=W)
 
 
# Creating label for class variable
# name using widget Entry
CTkLabel(master, text="", textvariable=name).grid(row=2, column=1, sticky=W)
CTkLabel(master, text="", textvariable=version).grid(row=3, column=1, sticky=W)
CTkLabel(master, text="", textvariable=Install_date).grid(row=4, column=1, sticky=W)
CTkLabel(master, text="", textvariable=publisher).grid(row=5, column=1, sticky=W)
CTkLabel(master, text="", textvariable=uninstall_string).grid(row=6, column=1, sticky=W)

 
e = CTkEntry(master, width = 350, height = 40)
e.grid(row=0, column=1)
 
# creating a button using the widget
b = CTkButton(master, text="Show", command=app, fg_color=("red", "red"), text_color=("white", "white"), hover_color=("red", "red"))
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)
 
master.mainloop()
