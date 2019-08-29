from vectors import Point, Vector

from tkinter import Tk, Canvas, BOTH, Button
from tkinter.ttk import Frame

# http://zetcode.com/tkinter/snake/
# https://docs.python.org/3/library/tkinter.html
# https://effbot.org/tkinterbook/canvas.htm

class Cat(Canvas):

    def __init__(self):
        super().__init__()
        self.initCat()
        self.pack()

    def initCat(self):
        self.draw_buffer = [(0,0,100,100), (100,100,100,200),(100,200,300,400)]
        #self.draw_buffer = []
        self.master.title("Cat")
        self.bind_all("<Key>", self.key_pressed)

        self.canvas = Canvas()
        self.canvas.pack(fill='both', expand=True)

        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        print("Screen dimensions", self.width, self.height)

        self.after(100, self.get_offset)

    def get_offset(self):
        # Nessecary to move to own function in order to get canvas initialised
        self.off_set_x = self.winfo_x()
        self.off_set_y = self.winfo_y()
        print("Canvas offset ", self.off_set_x, self.off_set_y)
        self.after(100, self.timer_event)

    def draw(self):

        for line in self.draw_buffer:
            x1, y1, x2, y2 = line
            self.canvas.create_line(x1, y1, x2, y2)
            self.canvas.pack()

    def timer_event(self):

        self.canvas.delete("all") # Clear all drawings
        self.draw()
        self.draw_buffer = []
        self.after(100, self.timer_event) # The first number is time between updates in milliseconds.

    def key_pressed(self, e):

        key = e.keysym

        if key == "Left":
            self.draw_buffer.append((10, 10, 20, 40))
            print("Left", self.draw_buffer)
        if key == "Right":
            self.draw_buffer.append((10, 10, 10, 50))
            print("Right")
        if key == "Up":
            self.draw_buffer.append((60, 60, 80, 90))
            print("Up")
        if key == "Down":
            self.draw_buffer.append((50, 50, 50, 60))
            print("Down")
        if key == "a":
            xx = 1000
            yy = 500
            self.event_generate('<Motion>', warp=True, x=xx - self.off_set_x, y=yy - self.off_set_y)
            print("a", self.winfo_pointerx(), self.winfo_pointery())
        if key == "b":
            self.event_generate('<Motion>', warp=True, x=-450, y=-757)
            print("b", self.winfo_pointerx(), self.winfo_pointery())
        if key == "c":
            self.event_generate('<Motion>', warp=True, x=831, y=268)
            print("c", self.winfo_pointerx(), self.winfo_pointery())

class Rhombe(object):

    def __init__(self, arg):

        self.arg = arg



def main():

    root = Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 0.93)
    root.wm_attributes('-fullscreen', 1)
    # root.geometry("500x500+300+800")
    # app = Example()
    app = Cat()

    root.mainloop()


if __name__ == '__main__':
    main()
