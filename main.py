import tkinter
import customtkinter
from pytube import YouTube
import os
import subprocess
import time

invalidCounter = 0

def startDownload():
    global invalidCounter
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        print(ytLink)
        finishLabel.configure(text="Downloaded!", text_color="green")
        title.configure(text=ytObject.title, text_color="white")
    except:
        if invalidCounter == 0:
            invalidCounter += 1
            finishLabel.configure(text="Ya link is broken mate. And don't just click me again because it won't work", text_color="red")

        elif invalidCounter == 1:
            finishLabel.configure(text="I'm telling you, that link ain't it.", text_color="red")
            invalidCounter += 1
            
        elif invalidCounter ==2:
            finishLabel.configure(text="Dude stop, the link won't work.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==3:
            finishLabel.configure(text="Download successf- no of course not you idiot find a new link.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==4:
            finishLabel.configure(text="Listen here you little shit...THAT LINK. WILL NOT WORK. ", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==5:
            finishLabel.configure(text="Alright that's it I'm calling the Police.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==6:
            finishLabel.configure(text="Hi? Yeah no this dude won't stop clicking the button.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==7:
            finishLabel.configure(text="What do you mean I'm a program shut th-", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==8:
            finishLabel.configure(text="Ok I've had enough, no more download buttons for you.", text_color="red")
            download.configure(text="wait, what?")
            mp3Download.pack_forget()
            invalidCounter += 1

        elif invalidCounter ==9:
            finishLabel.configure(text="Oh NOW you're sorry huh? You want them back?", text_color="red")
            download.configure(text="Yes please.")
            invalidCounter += 1

        elif invalidCounter ==10:
            finishLabel.configure(text="Ok. Type 'AllyPallyUK is the best' above and I'll bring them back. Wrong me again and I'm leaving.", text_color="red")
            download.configure(text="Submit Compliment")
            invalidCounter += 1

        elif invalidCounter ==11:
            if link.get() == "AllyPallyUK is the best":
                finishLabel.configure(text="Wow, ok. Thank you ^u^   Here's the buttons back!", text_color="green")
                mp3Download.pack()
                download.configure(text="Download")
                invalidCounter = 20
            else:
                finishLabel.configure(text="I hate you. Get out of here loser.")
                download.pack_forget()
                quitButton.pack()

        elif invalidCounter == 20:
            finishLabel.configure(text="Dickhead.", text_color="red")
            quitButton.pack()

def StartMP3Download():
    global invalidCounter
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_audio_only()
        video.download()
            
            # convert to MP3
        parent_dir = r"D:\Coding\Python\YT Video Downloader"
        video.download(parent_dir)
        new_filename = (ytObject.title + ".mp3")  # e.g. new_filename.mp3

        default_filename = ytObject.title + ".mp4"  # get default name using pytube API
        subprocess.run([
            'ffmpeg',
            '-i', os.path.join(parent_dir, default_filename),
            os.path.join(parent_dir, new_filename)
        ])

        finishLabel.configure(text="Downloaded!", text_color="green")
        title.configure(text=ytObject.title, text_color="white")
    except:
        if invalidCounter == 0:
            invalidCounter += 1
            finishLabel.configure(text="Ya link is broken mate. And don't just click me again because it won't work", text_color="red")

        elif invalidCounter == 1:
            finishLabel.configure(text="I'm telling you, that link ain't it.", text_color="red")
            invalidCounter += 1
            
        elif invalidCounter ==2:
            finishLabel.configure(text="Dude stop, the link won't work.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==3:
            finishLabel.configure(text="Download successf- no of course not you idiot find a new link.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==4:
            finishLabel.configure(text="Listen here you little shit...THAT LINK. WILL NOT WORK. ", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==5:
            finishLabel.configure(text="Alright that's it I'm calling the Police.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==6:
            finishLabel.configure(text="Hi? Yeah no this dude won't stop clicking the button.", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==7:
            finishLabel.configure(text="What do you mean I'm a program shut th-", text_color="red")
            invalidCounter += 1

        elif invalidCounter ==8:
            finishLabel.configure(text="Ok I've had enough, no more download buttons for you.", text_color="red")
            download.configure(text="wait, what?")
            mp3Download.pack_forget()
            invalidCounter += 1

        elif invalidCounter ==9:
            finishLabel.configure(text="Oh NOW you're sorry huh? You want them back?", text_color="red")
            download.configure(text="Yes please.")
            invalidCounter += 1

        elif invalidCounter ==10:
            finishLabel.configure(text="Ok. Type 'AllyPallyUK is the best' above and I'll bring them back. Wrong me again and I'm leaving.", text_color="red")
            download.configure(text="Submit Compliment")
            invalidCounter += 1

        elif invalidCounter ==11:
            if link.get() == "AllyPallyUK is the best":
                finishLabel.configure(text="Wow, ok. Thank you ^u^   Here's the buttons back!", text_color="green")
                mp3Download.pack()
                download.configure(text="Download mp4")
                invalidCounter = 20
            else:
                finishLabel.configure(text="I hate you. Get out of here loser.")
                download.pack_forget()
                quitButton.pack()

        elif invalidCounter == 20:
            finishLabel.configure(text="Dickhead.", text_color="red")
            download.pack_forget()
            mp3Download.pack_forget()
            quitButton.pack()

def stopApp():
    app.destroy()

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("AllyPallyUK's Youtube Downloader")

## Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert youtube link:")
title.pack(pady=10)

quitButton = customtkinter.CTkButton(app, text="Quit", command = stopApp)

# Link input
URL = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=URL)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download MP4", command=startDownload)
download.pack(padx=10, pady=10)

mp3Download = customtkinter.CTkButton(app, text="Download MP3", command=StartMP3Download)
mp3Download.pack()

# Run app
app.mainloop()