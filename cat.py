from tkinter import Tk, Canvas, BOTH
from tkinter.ttk import Frame

# http://zetcode.com/tkinter/snake/

class Cat(Frame):

    def __init__(self):
        super().__init__()
        self.initCat()
        self.pack()

    def initCat(self):
        self.draw_buffer = []
        self.inGame = True
        self.master.title("Cat")
        self.bind_all("<Key>", self.key_pressed)
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry(f"{width}x{height}+{0}+{0}")
        self.after(100, self.timer_event())

    def draw(self):

        canvas = Canvas(self)

        for line in self.draw_buffer:
            x1, y1, x2, y2 = line
            canvas.create_line(x1, y1, x2, y2)
            print(line)

        canvas.pack()

        self.draw_buffer = []

    def key_pressed(self, e):

        key = e.keysym

        if key == "Left":
            self.draw_buffer.append((10, 10, 20, 20))
            print("Left", self.draw_buffer)
        if key == "Right":
            self.draw_buffer.append((10, 10, 10, 50))
            print("Right")
        if key == "Up":
            self.draw_buffer.append((60, 60, 50, 50))
            print("Up")
        if key == "Down":
            self.draw_buffer.append((50, 50, 50, 60))
            print("Down")

    def timer_event(self):
        self.draw()
        if self.inGame:
            self.after(100, self.timer_event()) # The first number is time between updates in milliseconds.

def main():

    root = Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 0.3)
    # root.geometry("500x500+300+800")
    # app = Example()
    app = Cat()

    root.mainloop()


if __name__ == '__main__':
    main()
