import tkinter as tk
from tkinter import *
import pygame
from tkinter.ttk import *
from PIL import ImageTk, Image #importing Pillow library to manipulate images
import random, time

pygame.init() #pygame initialization
#Main window
windowMain = Tk()
windowMain.geometry("800x600")
windowMain.resizable(False, False)
windowIcon = PhotoImage(file = "lockLogo.png")#variable that stores Image
windowMain.iconphoto(False, windowIcon)#method that changes the window icon
windowMain.title("PHANTASM")

#Sounds
mainScreenMusic = "mainMusic.wav"
pygame.mixer.music.load(mainScreenMusic) #loads long audios into pygame music player and makes it playable
pygame.mixer.music.play(loops=-1)#makes the music loaded into mixer loop
click_sound = pygame.mixer.Sound("button_click.wav")#using pygame, makes a sound object that can be then played, stopped, etc
global sound_puzzle 
sound_puzzle = pygame.mixer.Sound("soundpuzzle.wav")
flip_sound = pygame.mixer.Sound("flip_sound.wav")

def clickTrack():
    print("Successful button click")#for our reference in the console

# Function to Start Level 1. 
def go_to_lvl1():
    #Switch from start screen to game screen
    pygame.mixer.music.stop() #stops the music module from playing the loaded file

    windowMain.withdraw()  # Hide main window
    level1.deiconify()  # Show Level 1 window
    

# Triggers Level 2 window
def go_to_lvl2():
    click_sound.play()
    level1.withdraw()
    level2.deiconify()
    level2_UI()

# Level2 Easy, its logic and puzzle component
def level2_UI():
    global tarot_back_resized, card_images_resized
    dropdown(level2)
    #Loaded the back image of the card
    card_back_image = Image.open("tarot_back.png")
    # Resized card back image
    tarot_back_resized = ImageTk.PhotoImage(card_back_image.resize((150, 180), Image.LANCZOS))
     # Iterating over the card_images dictionary and creating a new one with the same keys but resized values
    card_images = [
        ImageTk.PhotoImage(Image.open(f"easy_tarot{i}.png").resize((150, 180), Image.LANCZOS)) for i in range(2, 5)
    ]
    level2_logic(card_images)

# Function for Puzzle Level logic
def level2_logic(card_faces):
    sound_puzzle.play(loops=-1)
    facesWPairs = card_faces * 2 #A list with dupes/pairs
    random.shuffle(facesWPairs)
    flipped_cards = []
    attempt = 0
    for i, image in enumerate(facesWPairs):#i is index given through enumerate and image is temp var that holds each image from the list
        card = tk.Button(level2, image=tarot_back_resized, width=150, height=180, borderwidth=0, highlightthickness=0)
        card.config(command=lambda btn=card, img=image: flip_card(btn, img, flipped_cards))
        card.place(x=(i % 3) * 145 + (200), y=(i // 3) * 200 + (100))
    
     # Function to flip a card when button is pressed
    def flip_card(button, image, flipped_cards):
        flip_sound.play()
        if len(flipped_cards) < 2 and button.cget("image") == tarot_back_resized:
            button.config(image=image)
            flipped_cards.append((button, image))

            if len(flipped_cards)==2:
                for button, image in flipped_cards:
                    button.config(state="disabled")
                level2.after(1000, lambda: check_match(flipped_cards))
                print("leaving flip card")

    # Function to check for a match
    def check_match(flipped_cards):
        if len(flipped_cards) == 2:
            button1, card1_img = flipped_cards[0]  
            button2, card2_img = flipped_cards[1]
            global attempt

            if card1_img != card2_img:
                reset(button1, button2)
                attempt+=1
                if attempt>3:
                    show_game_over()
            else:
                button1.config(state="disabled")
                button2.config(state="disabled")
            
            flipped_cards.clear()

    def reset(button1, button2):
        button1.config(image=tarot_back_resized)
        button2.config(image=tarot_back_resized)
        button1.config(state="normal")
        button2.config(state="normal")

def show_game_over():
    level2.withdraw() 
    game_over_screen.deiconify()

# Restart button
def restart_game():
    game_over_screen.withdraw()  # Close the game-over screen
    windowMain.deiconify()  # Show the main screen again

def show_proceed_button():
    proceedImage = Image.open("proceedButton.png")#loading an image in pillow library to make an image object that can be worked with
    proceedImage = ButtonImage.resize((210, 105), Image.LANCZOS)
    proceedImage = ImageTk.PhotoImage(ButtonImage)#converts image to format working for tkinter(from PIL)/prep to use in tk
    proceed_button = tk.Button(level2, image=proceedImage, command=go_to_lvl3)
    proceed_button.place(relx=0.5, rely=0.9, anchor="center")  

def go_to_lvl3():
    pygame.mixer.music.stop()
    level2.withdraw()

#MAIN SCREEN Canvas
firstPageImg = Image.open("firstPage.png") #making sure the image is accessible
firstPageImg = firstPageImg.resize((800, 600), Image.LANCZOS)#Image.LANCZOS is from the Pillow Library. It reduces pixalation when resizing idk if we should use it

game_bg = ImageTk.PhotoImage(firstPageImg)#takes an image from Pillow library and converts tkinter image

canvas = Canvas(windowMain, width=800, height=600)#canvas widget adding
canvas.pack(fill=tk.BOTH, expand=True)

canvas.create_image(0, 0, anchor="nw", image=game_bg)
canvas.create_text(400, 110, text = "PHANTASM", font=("Fixedsys", 73))#adding text on top of canvas

canvas.create_text(400, 170, text = "Choose game mode:", font=("Fixedsys", 23))#adding text on top of canvas

#Buttons
ButtonImage = Image.open("startButton.png")#loading an image in pillow library to make an image object that can be worked with
ButtonImage = ButtonImage.resize((210, 105), Image.LANCZOS)
ButtonImage = ImageTk.PhotoImage(ButtonImage)#converts image to format working for tkinter(from PIL)/prep to use in tk
buttonStart = tk.Button(windowMain, image = ButtonImage, background="grey", command= go_to_lvl1)
buttonStart.image = ButtonImage #this button object will be referencing BI image object
canvas.create_window(400, 450, window = buttonStart)


# Level 1 canvas or however u want to structure it

# Level 2 Window
level2 = tk.Toplevel(windowMain)
level2.geometry("800x600")
level2.title("PHANTASM")
level2.withdraw()
level2.iconphoto(False, windowIcon)
#Level 2 Canvas
level2_bg = Image.open("puzzle.png") #making sure the image is accessible
level2_bg = level2_bg.resize((800, 600), Image.LANCZOS)

puzzle_bg = ImageTk.PhotoImage(level2_bg)#takes an image from Pillow library and converts tkinter image

level2_canvas = Canvas(level2, width=800, height=600)#canvas widget adding
level2_canvas.pack(fill=tk.BOTH, expand=True)

level2_canvas.create_image(0, 0, anchor="nw", image=puzzle_bg)

#Lvl 3 canvas

# Game over window
game_over_screen = tk.Toplevel()
game_over_screen.geometry("800x600")
game_over_screen.resizable(False, False)
game_over_screen.title("PHANTASM")
game_over_screen.withdraw()
game_over_image = Image.open("gameoverscreen.png").resize((800, 600), Image.LANCZOS)
game_over_tk_image = ImageTk.PhotoImage(game_over_image)
    
# game over canvas
game_over_canvas = Canvas(game_over_screen, width=800, height=600)
game_over_canvas.pack(fill=tk.BOTH, expand=True)
game_over_canvas.create_image(0, 0, anchor="nw", image=game_over_tk_image)
game_over_canvas.image = game_over_tk_image #referencing the image that it is itself to avoid loss

#Restart Button
restartImage = Image.open("restartButton.png")
restartImage = restartImage.resize((140, 90), Image.LANCZOS)
restartImage = ImageTk.PhotoImage(restartImage)
restart_button = tk.Button(game_over_screen, image=restartImage, command=restart_game)
restart_button.place(relx=0.5, rely=0.9, anchor="center")

#Pause window
#pause 

#Dropdown menu for quit and main menu. use it for your levels
def dropdown(yourLevel):
    menu_bar = tk.Menu(yourLevel)
    game_menu = tk.Menu(menu_bar, tearoff=0)
    game_menu.add_command(label="MAIN MENU", command=lambda: show_home(yourLevel))
    game_menu.add_command(label="PAUSE", command=lambda: show_pause(yourLevel))
    game_menu.add_command(label="QUIT", command=yourLevel.quit)
    menu_bar.add_cascade(label="MENU", menu=game_menu)
    yourLevel.config(menu=menu_bar)
def show_home(currentLevel):
    currentLevel.withdraw()
    windowMain.deiconify()
def show_pause(currentLevel):# i want to hide this level but remember to show it after resume button is hit
    currentLevel.withdraw()
    pause.deiconify()
dropdown(windowMain)
windowMain.mainloop()