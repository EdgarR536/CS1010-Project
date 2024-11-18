import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image #importing Pillow library to manipulate images
window = Tk()
window.geometry("800x600")

windowIcon = PhotoImage(file = "lockLogo.png")#variable that stores Image
window.iconphoto(False, windowIcon)#method that changes the window icon

window.title("PHANTASM")

def clickTrack():
    print("Successful button click")#for our reference in the console

def game_pause(status):
    if status==True:
        
        # configure the pause screen and have resume button call resume function
    else:
        
        # Resume animations or game loop

# Function to resume the game
def resume_game():
    global is_paused
    is_paused = False
    #pause_label.config(text="Game Running")
    resume_button.pack_forget()  # Hide the Resume button? idk how i should go abt this in depth

def start_game(mode): #based on input gives different difficulty of game
    if mode == "regular":
        # Add logic for Regular mode level 1 edgar
    elif mode == "nightmare":
        #hard lvl
        

firstPageImg = Image.open("firstPage.png") #making sure the image is accessible
firstPageImg = firstPageImg.resize((800, 600), Image.LANCZOS)#Image.LANCZOS is from the Pillow Library. It reduces pixalation when resizing idk if we should use it

game_bg = ImageTk.PhotoImage(firstPageImg)#takes an image from Pillow library and converts tkinter image

canvas = Canvas(window, width=800, height=600)#canvas widget adding
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_image(0, 0, anchor="nw", image=game_bg)
canvas.create_text(400, 110, text = "PHANTASM", font=("Fixedsys", 73))#adding text on top of canvas

canvas.create_text(400, 170, text = "Choose game mode:", font=("Fixedsys", 23))#adding text on top of canvas

#Buttons
ButtonImage = Image.open("rectangularButton.png")#loading an image in pillow library to make an image object that can be worked with
ButtonImage = ButtonImage.resize((140, 90), Image.LANCZOS)
ButtonImage = ImageTk.PhotoImage(ButtonImage)#converts image to format working for tkinter(from PIL)/prep to use in tk
buttonReg = tk.Button(window, image = ButtonImage, background="grey", command=lambda: start_game("regular"))
buttonReg.image = ButtonImage #this button object will be referencing sBI image object
canvas.create_window(265, 450, window = buttonReg)

#nightmare button
nightButtonImage = Image.open("nightButton.png")#loading an image in pillow library to make an image object that can be worked with
nightButtonImage = nightButtonImage.resize((140, 90), Image.LANCZOS)
nightButtonImage = ImageTk.PhotoImage(nightButtonImage)
buttonNight = tk.Button(window, image = nightButtonImage, background="grey")
buttonNight.image = nightButtonImage #this button object will be referencing sBI image object
canvas.create_window(565, 450, window = buttonNight)
window.mainloop()



