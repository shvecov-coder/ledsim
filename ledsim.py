import tkinter as tk
from PIL import ImageTk, Image


class LEDSim:

    def __init__(self):
        self.w = '450'
        self.h = '600'
        self.root = tk.Tk()
        self.window_name = 'LEDSim'
        self.Canvas = tk.Canvas(self.root)
        self.img = Image.open('./led.png')
        new_size = (self.img.width // 4, self.img.height // 4)
        new_size_img = self.img.resize(size=new_size)
        self.img = ImageTk.PhotoImage(new_size_img)

    def configuration(self):
        '''Configuration window'''
        self.root.title(self.window_name)
        self.root.resizable(False, False)
        self.root.geometry(self.w + 'x' + self.h)

        '''Configuration canvas'''
        self.Canvas.configure(width=self.w, height=self.h)
        self.Canvas.create_image(0, 0, anchor='nw', image=self.img)
        self.Canvas.pack()

    def start_ledsim(self):
        self.configuration()
        tk.mainloop()
