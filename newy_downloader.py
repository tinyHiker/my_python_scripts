import tkinter 
import customtkinter
from pytube import YouTube


#System Settings
def startDownload():
    try: 
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download(r'C:\Users\tahai\Documents\offline_vids')
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error", text_color = 'red')
   
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
customtkinter.set_appearance_mode('dark')

#Creating frame
app = customtkinter.CTk()
app.geometry('720x480')


#Adding UI elements
title = customtkinter.CTkLabel(app, text = "Insert a youtube link")
title.pack(padx= 10, pady = 10)


# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height = 40, textvariable= url_var)
link.pack()


#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack()

#Download Button
download = customtkinter.CTkButton(app, text = "Download", command = startDownload)
download.pack(padx=10, pady=10)

app.mainloop()
