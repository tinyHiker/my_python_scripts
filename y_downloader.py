import tkinter
import customtkinter 
from pytube import YouTube
import pytube.exceptions

customtkinter.set_appearance_mode('dark')

def startDownload():
    try:
        ytLink = url_var.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color = "white")
        video.download(r'C:\Users\tahai\Documents\offline_vids')
        finishLabel.configure(text = "Downloaded")
    except pytube.exceptions.AgeRestrictedError:
        finishLabel.configure(text= "Video cannot be downloaded due top age restriction ", text_color = "red")
    except pytube.exceptions.RegexMatchError:
        finishLabel.configure(text = "Please enter a valid link")



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text = per + "%")
    pPercentage.update()
    
    progressBar.set(float(percentage_of_completion) / 100)
    
def startDownloadTest():
    ytLink = url_var.get()
    ytObject = YouTube(ytLink)
    video = ytObject.streams.get_highest_resolution()
    title.configure(text=ytObject.title, text_color = "white")
    video.download(r'C:\Users\tahai\Documents\offline_vids')
    finishLabel.configure(text = "Downloaded")
    

# Our app frame 
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


#Adding UI elements
title = customtkinter.CTkLabel(app, text= "Insert youtube link ")
title.pack(padx = 10, pady=10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width = 350, height = 40, textvariable = url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text = "")
finishLabel.pack(padx=10, pady= 10)

#Progress percentage 
pPercentage = customtkinter.CTkLabel( app, text = '0%')
pPercentage.pack()
#progressBar = customtkinter.CTkProgressBar(app, width = 400)
#progressBar.set(0)
#progressBar.pack(padx = 10, pady = 10)

download = customtkinter.CTkButton(app, text = "Download", command = startDownload)
download.pack(padx= 10, pady = 10)
# Run app
app.mainloop()