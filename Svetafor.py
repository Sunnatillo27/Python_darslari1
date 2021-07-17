from tkinter import *
import time


class Frame(Tk):

    def __init__(self):
        self.state = 0
        super().__init__()
        self.title('Svetafor')
        self.canvas = c = Canvas(self, width=170, height=360, bg="blue")
        self.r = c.create_oval(35, 10, 145, 120, fill="#ff0000")
        self.y = c.create_oval(35, 135, 145, 240, fill="#808000")
        self.g = c.create_oval(35, 250, 145, 350, fill="#008000")
        c.pack()
        self.update()
        self.after(3000, self.upd)

    def upd(self):
        if self.state == 0:
            self.state = 1
            self.canvas.itemconfigure(self.r, fill='#800000')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.after(1000, self.upd)
        elif self.state == 1:
            self.state = 2
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.canvas.itemconfigure(self.g, fill='#00ff00')
            self.after(6000, self.upd)
        elif self.state == 2:
            self.state = 3
            self.canvas.itemconfigure(self.g, fill='#008000')
            self.canvas.itemconfigure(self.y, fill='#ffff00')
            self.after(1000, self.upd)
        else:
            self.state = 0
            self.canvas.itemconfigure(self.r, fill='#ff0000')
            self.canvas.itemconfigure(self.y, fill='#808000')
            self.after(6000, self.upd)


root = Frame()
root.mainloop()