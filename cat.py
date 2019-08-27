from tkinter import Tk, Canvas, BOTH
from tkinter.ttk import Frame

# http://zetcode.com/tkinter/snake/

class Cat(Frame):

    def __init__(self):
        super().__init__()
        self.initCat()
        self.pack()

    def initCat(self):
        self.master.title("Cat")
        self.bind_all("<Key>", self.key_pressed)
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry(f"{width}x{height}+{0}+{0}")
        self.draw(100, 100, 888, 400)

    def draw(self, x1, y1, x2, y2):
        canvas = Canvas(self)
        canvas.create_line(x1, y1, x2, y2)
        canvas.pack()

    def key_pressed(self, e):

        key = e.keysym

        if key == "Left":
            self.draw(100, 100, 200, 200)
            print("Left")
        if key == "Right":
            self.draw(200, 100, 200, 100)
            print("Right")
        if key == "Up":
            self.draw(500, 600, 500, 600)
            print("Up")
        if key == "Down":
            self.draw(600, 500, 600, 500)
            print("Down")

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
