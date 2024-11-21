import tkinter as tk
from tkinter import *
import pygame
from tkinter.ttk import *
from PIL import ImageTk, Image #importing Pillow library to manipulate images
windowMain = Tk()
windowMain.geometry("800x600")

windowIcon = PhotoImage(file = "lockLogo.png")#variable that stores Image
windowMain.iconphoto(False, windowIcon)#method that changes the window icon

windowMain.title("PHANTASM")

pygame.init() #pygame initialization

#Sounds
mainScreenBg = "mainMusic.wav"
pygame.mixer.music.load(mainScreenBg) #loads long audios into pygame music player and makes it playable

click_sound = pygame.mixer.Sound("button_click.wav")#using pygame, makes a sound object that can be then played, stopped, etc



def clickTrack():
    print("Successful button click")#for our reference in the console

def start_game(mode):
    """Switch from start screen to game screen."""
    # Stop background music
    pygame.mixer.music.stop() #stops the music module from playing the loaded file

    # Play button click sound
    click_sound.play()
    
    
    windowMain.withdraw() 
    level1_window.deiconify()  # restores/shows the hidden window
    if mode == "regular":
        print()
        # Add logic for Regular mode level 1 edgar
    elif mode == "nightmare":
        print()
        #hard lvl
        #drop down for pause and quit
        
        # configure the pause screen and have resume button call resume function

# Function to resume the game
 # Hide the Resume button? idk how i should go abt this in depth

    
        

firstPageImg = Image.open("firstPage.png") #making sure the image is accessible
firstPageImg = firstPageImg.resize((800, 600), Image.LANCZOS)#Image.LANCZOS is from the Pillow Library. It reduces pixalation when resizing idk if we should use it

game_bg = ImageTk.PhotoImage(firstPageImg)#takes an image from Pillow library and converts tkinter image

canvas = Canvas(windowMain, width=800, height=600)#canvas widget adding
canvas.pack(fill=tk.BOTH, expand=True)

pygame.mixer.music.play(-1)#makes the music loaded into

canvas.create_image(0, 0, anchor="nw", image=game_bg)
canvas.create_text(400, 110, text = "PHANTASM", font=("Fixedsys", 73))#adding text on top of canvas

canvas.create_text(400, 170, text = "Choose game mode:", font=("Fixedsys", 23))#adding text on top of canvas

#Buttons
ButtonImage = Image.open("rectangularButton.png")#loading an image in pillow library to make an image object that can be worked with
ButtonImage = ButtonImage.resize((140, 90), Image.LANCZOS)
ButtonImage = ImageTk.PhotoImage(ButtonImage)#converts image to format working for tkinter(from PIL)/prep to use in tk
buttonReg = tk.Button(windowMain, image = ButtonImage, background="grey", command=lambda: start_game("regular"))
buttonReg.image = ButtonImage #this button object will be referencing sBI image object
canvas.create_window(265, 450, window = buttonReg)

#nightmare button
nightButtonImage = Image.open("nightButton.png")#loading an image in pillow library to make an image object that can be worked with
nightButtonImage = nightButtonImage.resize((140, 90), Image.LANCZOS)
nightButtonImage = ImageTk.PhotoImage(nightButtonImage)
buttonNight = tk.Button(windowMain, image = nightButtonImage, background="grey", command=lambda: start_game("nightmare"))
buttonNight.image = nightButtonImage #this button object will be referencing sBI image object
canvas.create_window(565, 450, window = buttonNight)
windowMain.mainloop()

level1_window = tk.Toplevel(windowMain)  # Makes it a secondary window in the layers
level1_window.title("PHANTASM")
level1_window.geometry("600x800")
level1_window.withdraw()  # just hides the window but it still exists
level1_window.mainloop()
#write your widgets for the level1 here and stuff


#Level 2