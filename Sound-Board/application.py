from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from settings import *
import pygame
from PIL import Image, ImageTk


class Application(Frame):
    title = "title"

    pygame.mixer.init()
    def __init__(self, root):
        super(Application, self).__init__()
        #create Widgets
        self.initUI(root)
        self.pack()









    def initUI(self, root):
        #app
        self.master.title(Application.title)
        self.style = Style()
        self.style.theme_use(themename= theme)

        #open cartoon images
        self.runIcon = PhotoImage(file=r"images/cartoon/run_icon.png")
        self.bonkIcon = PhotoImage(file=r"images/cartoon/bonk_icon.png")
        self.jumpIcon = PhotoImage(file=r"images/cartoon/boing_icon.png")
        self.slipIcon = PhotoImage(file=r"images/cartoon/slip_icon.png")
        self.sneakIcon = PhotoImage(file=r"images/cartoon/sneak_icon.png")

        #open audience images
        self.laughIcon = PhotoImage(file=r"images/audience/laugh_icon.png")
        self.clapIcon = PhotoImage(file=r"images/audience/clap_icon.png")
        self.booIcon = PhotoImage(file=r"images/audience/boo_icon.png")
        self.awwIcon = PhotoImage(file=r"images/audience/aww_icon.png")
        self.angryIcon = PhotoImage(file=r"images/audience/angry_icon.png")


        #create widgets
        self.createWidgets(root)



        # self.centerWindow()


    def createWidgets(self, root):
        Label(text="Choose a Sound Board:").pack(side=TOP, fill=X)

        # create sound window buttons
        self.buttonList = ["Cartoon Sounds", "Audience Sounds", "Misc. Sounds"]

        cartoonButton = Button(self, text="Cartoon Sounds", width=20, command=lambda:self.cartoonSounds()).pack(
            side=LEFT,padx=10, pady=10)
        audienceButton = Button(self, text="Audience Sounds", width=20, command=lambda: self.audienceSounds()).pack(
            side=LEFT, padx=10, pady=10)
        miscButton = Button(self, text="Misc. Sounds", width=20, command=lambda: self.miscSounds()).pack(
            side=LEFT, padx=10, pady=10)


    def cartoonSounds(self):
        #create soundboard window
        top = Toplevel()
        top.title('Cartoon Sound Board')
        # button lists
        sounds = ["sounds/cartoon/cartoon_running.wav", "sounds/cartoon/bonk.wav"
            ,"sounds/cartoon/boing.wav", "sounds/cartoon/slip.wav", "sounds/cartoon/sneak.wav"]
        icons = [self.runIcon, self.bonkIcon, self.jumpIcon, self.slipIcon, self.sneakIcon]
        # create sound buttons
        if len(sounds) == len(icons):
            for i in range(len(sounds)):
                self.cartoonButton = Button(top,text="", image=icons[i],
                                        command=lambda i=i: self.playSound(sounds[i]))
                self.cartoonButton.pack(side=LEFT)
        else:
            messagebox.showerror("Something went wrong!", "Error: len(sounds) != len(icons)")
            top.destroy()


        # self.cartoonRun = Button(top, text="Bonk Sound", image=self.runIcon,
        #                          command=lambda: self.playSound("sounds/cartoon_running.wav"))
        # self.cartoonRun.pack()

    def audienceSounds(self):
        # create soundboard window
        top = Toplevel()
        top.title('Audience Sound Board')
        # button lists
        sounds = ["sounds/audience/laugh.wav", "sounds/audience/clap.wav","sounds/audience/boo.wav",
                  "sounds/audience/aww.wav", "sounds/audience/angry.wav"]
        icons = [self.laughIcon, self.clapIcon, self.booIcon, self.awwIcon, self.angryIcon]
        # create sound buttons
        if len(sounds) == len(icons):
            for i in range(len(sounds)):
                self.cartoonButton = Button(top, text="", image=icons[i],
                                            command=lambda i=i: self.playSound(sounds[i]))
                self.cartoonButton.pack(side=LEFT)
        else:
            messagebox.showerror("Something went wrong!", "Error: len(sounds) != len(icons)")
            top.destroy()

    def miscSounds(self):
        # create soundboard window
        top = Toplevel()
        top.title('Misc Sound Board')
        # button lists
        sounds = ["sounds/misc/alert.mp3", "sounds/misc/buzzer.mp3", "sounds/misc/boom.wav",
                  "sounds/misc/money.wav", "sounds/misc/taco_bell.mp3"]
        icons = [self.laughIcon, self.clapIcon, self.booIcon, self.awwIcon, self.angryIcon]
        # create sound buttons
        if len(sounds) == len(icons):
            for i in range(len(sounds)):
                self.cartoonButton = Button(top, text="Sound" + str((i+1)),
                                            command=lambda i=i: self.playSound(sounds[i]))
                self.cartoonButton.pack(side=LEFT)
        else:
            messagebox.showerror("Something went wrong!", "Error: len(sounds) != len(icons)")
            top.destroy()

    def playSound(self, sound):
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play(loops=0)



    def centerWindow(self, top):
        w = 0
        h = 0
        sw = top.winfo_screenwidth()
        sh = top.winfo_screenheight()
        perW = (w/sw)
        adjustedWidth = sw*perW
        print(int(adjustedWidth))
        perH = (h / sh)
        adjustedHeight = sh * perH
        print(int(adjustedHeight))

        x = (sw - adjustedWidth)/2
        y = (sh - adjustedHeight)/2

        top.geometry("%dx%d+%d+%d" %(adjustedWidth, adjustedHeight,x,y))






    def __change_Title__(title):
        Application.title = title

