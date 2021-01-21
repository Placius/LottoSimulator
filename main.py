from tkinter import *
import random

class Lotto:
    def __init__(self, root):
        # --------------------------- losowanie 6 zwycięzkich liczb ---------------------------
        self.winnumbers = [1,2,3,4,5,6]
        self.mynumbers = [1,2,3,4,5,6]

        menu = Menu(root)
        root.config(menu=menu)

        # --------------------------- górny pasek menu opcji ---------------------------

        gameMenu = Menu(menu)
        menu.add_cascade(label="Game", menu=gameMenu)
        gameMenu.add_command(label="New game", command=self.NewGame)
        gameMenu.add_separator()
        gameMenu.add_command(label="Quit", command=menu.quit)

        helpMenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="How to play?", command=self.HowtoPlay)
        helpMenu.add_command(label="Info...", command=self.Info)

        # --------------------------- górny pasek informacyjny ---------------------------

        topstatus = Label(root, text="Welcome to my first lottery simulator, good luck with your game.",
                          bd=4, relief=SUNKEN, anchor=S, bg="black", fg="white")
        topstatus.pack(side=TOP, fill=X)

        # --------------------------- Dolny pasek informacyjny ---------------------------

        status = Label(root, text="Good luck my friend!", bd=2, relief=SUNKEN, anchor=S, bg="black", fg="white")
        status.pack(side=BOTTOM, fill=X)

        # --------------------------- prawy pasek przycisków funkcyjnych ---------------------------

        toolbar = Frame(root, bg="grey")
        self.StartButton = Button(toolbar, text="Start", command=self.Start, bg="black", fg="white", width=10, height=5)
        self.StartButton.pack(side=TOP, padx=10, pady=2)

        self.TryButton = Button(toolbar, text="Try", command=self.Try, bg="black", fg="white", width=10, height=5)
        self.TryButton.pack(side=TOP, padx=10, pady=2)

        self.RestartButton = Button(toolbar, text="Restart", command=self.Restart, bg="black", fg="white", width=10, height=5)
        self.RestartButton.pack(side=TOP, padx=10, pady=2)

        self.QuitButton = Button(toolbar, text="Quit", command=toolbar.quit, bg="black", fg="white", width=10, height=5)
        self.QuitButton.pack(side=TOP, padx=10, pady=2)

        toolbar.pack(side=RIGHT, fill=Y)

        # --------------------------- lewy pasek przycisków funkcyjnych ---------------------------

        lefttoolbar = Frame(root, bg="grey")

        self.infonumber = Label(lefttoolbar, text="Here put your happy numbers", padx=10, pady=2, bg="grey")
        self.infonumber.pack()

        self.firstnumber = Label(lefttoolbar, text="'1'", padx=10, pady=2)
        self.firstnumber.pack(anchor=E, padx=10)
        self.entry_1 = Entry(lefttoolbar, width=5, justify=CENTER)
        self.entry_1.pack(pady=5, padx=10, anchor=E)

        self.secondnumber = Label(lefttoolbar, text="'2'", padx=10, pady=2)
        self.secondnumber.pack(anchor=W, padx=10)
        self.entry_2 = Entry(lefttoolbar, width=5, justify=CENTER)
        self.entry_2.pack(pady=5, padx=10, anchor=W)

        self.thirthnumber = Label(lefttoolbar, text="'3'", padx=10, pady=2)
        self.thirthnumber.pack(anchor=E, padx=10)
        self.entry_3 = Entry(lefttoolbar, width=5, justify=CENTER)
        self.entry_3.pack(pady=5, padx=10, anchor=E)

        self.fourthnumber = Label(lefttoolbar, text="'4'", padx=10, pady=2)
        self.fourthnumber.pack(anchor=W, padx=10)
        self.entry_4 = Entry(lefttoolbar, width=5, justify=CENTER)
        self.entry_4.pack(pady=5, padx=10, anchor=W)

        self.fifthnumber = Label(lefttoolbar, text="'5'", padx=10, pady=2)
        self.fifthnumber.pack(anchor=E, padx=10)
        self.entry_5 = Entry(lefttoolbar, width=5, justify=CENTER)
        self.entry_5.pack(pady=5, padx=10, anchor=E)

        self.sixthnumber = Label(lefttoolbar, text="'6'", padx=10, pady=2)
        self.sixthnumber.pack(anchor=W, padx=10)
        self.entry_6 = Entry(lefttoolbar, width=5, justify=CENTER)
        self.entry_6.pack(pady=5, padx=10, anchor=W)

        self.Number6Button = Button(lefttoolbar, text="CHECK", bg="black", fg="white", command=self.Try)
        self.Number6Button.pack(side=TOP, padx=5, pady=10)

        lefttoolbar.pack(side=LEFT, fill=Y)

        # --------------------------- ZASOBY: obrazki itp ---------------------------

        File1 = "lotto.png"
        self.img1 = PhotoImage(file=File1)

        # --------------------------- RAMKA GLOWNA ---------------------------

        self.frame = Frame(root, width=400, height=350)
        self.canvas = Canvas(self.frame, width=400, height=400)
        self.canvas.pack()
        self.canvas.create_text(198, 50, text="Welcome in my second window game!")
        self.canvas.create_text(198, 80, text="Click Start")
        self.canvas.create_image(198, 250, image=self.img1)
        self.frame.pack(side = RIGHT)



    def NowThis(self):
        print("Wait for my destiny....")

    def NewGame(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(198, 50, text="Welcome in my second window game!")
        self.canvas.create_text(198, 80, text="Click Start")
        self.canvas.create_image(198, 250, image=self.img1)

    def Start(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(135, 120, justify=CENTER, text="""
                                     Enter the six numbers of your choice

                                     in the boxes on the left,

                                    then press the "Try" button on right side or "CHECK" on left

                                    to start the drawing machine,

                                    which will check if and how much you have won.
                                    

                                    REMEMBER!!!

                                    Only 1 - 49 numbers.

                                    """, font="TimesNewRoman, 10")

        self.canvas.create_text(198, 280, text="Good luck!", font="TimesNewRoman, 20")

    def Try(self):
        self.canvas.delete(ALL)
        winnumbers = []
        i = 1
        while i <= 6:
            win = random.randint(1,49)
            if win in winnumbers:
                continue
            else:
                winnumbers.append(win)
                i += 1

        self.winnumbers = winnumbers

        try:
            list = [int(self.entry_1.get()), int(self.entry_2.get()), int(self.entry_3.get()),
                          int(self.entry_4.get()), int(self.entry_5.get()), int(self.entry_6.get())]

            my_numbers = []

            for el in list:
                if el < 1 or el > 49:
                    self.canvas.create_text(198, 150, text="You must enter six diffrent numbers!",
                                            font="TimesNewRoman, 15")
                    
                    self.canvas.create_text(198, 170, text="Only 1 - 49 numbers!",
                                            font="TimesNewRoman, 15")
                    break

                elif el in my_numbers:
                    self.canvas.create_text(198, 150, text="You must enter six diffrent numbers!",
                                            font="TimesNewRoman, 15")
                    
                    self.canvas.create_text(198, 170, text="Only 1 - 49 numbers!",
                                            font="TimesNewRoman, 15")
                    break

                else:
                    my_numbers.append(el)

            if len(my_numbers) == 6:
                self.mynumbers = my_numbers

                print(my_numbers)

                hit = 0

                for i in self.mynumbers:
                    if i in self.winnumbers:
                        hit += 1
                    else:
                        continue

                first_text = "Won numbers: " + str(self.winnumbers)
                second_text = "Your numbers: " + str(self.mynumbers)

                third_text = "You hit " + str(hit) + " numbers!"

                self.canvas.create_text(198, 40, text=first_text, font="TimesNewRoman, 15")
                self.canvas.create_text(198, 150, text=second_text, font="TimesNewRoman, 10")

                self.canvas.create_text(198, 240, text=third_text, font="TimesNewRoman, 15")

        except ValueError:
            self.canvas.create_text(198, 150, text="You must enter six diffrent numbers!", font="TimesNewRoman, 15")
            self.canvas.create_text(198, 170, text="Only 1 - 49 numbers!",
                                            font="TimesNewRoman, 15")


    def Restart(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(198, 50, text="Welcome in my second window game!")
        self.canvas.create_text(198, 80, text="Click Start")
        self.canvas.create_image(198, 250, image=self.img1)

    def Info(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(198, 50, text="Gra napisana na potrzebę nauki podstaw modułu tkinter")

    def HowtoPlay(self):
        self.canvas.delete(ALL)
        self.canvas.create_text(198, 50, text="How to play?")
        self.canvas.create_text(198, 80, text="""That is easy program, i believe in you!""", justify=CENTER)

# --------------------------- Wywołanie programu ---------------------------
root = Tk()
root.title("Placius Lotto")
Lotto(root)
root.mainloop()
