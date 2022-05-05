from tkinter import *


class FindMySoul:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1024x768')

        self.player_image = PhotoImage(file="img/Little_Mac.png")
        self.label = Label(self.root, image=self.player_image)
        self.label.place(x=50, y=100)

        self.opponent_image = PhotoImage(file="img/King_Hippo_Transparent.png")
        self.label_o = Label(self.root, image=self.opponent_image)
        self.label_o.place(x=500, y=100)

        self.root.mainloop()


app = FindMySoul()
