from tkinter import Tk, Canvas, BOTH, Button
from tkinter.ttk import Frame

# http://zetcode.com/tkinter/snake/
# https://docs.python.org/3/library/tkinter.html
# https://effbot.org/tkinterbook/canvas.htm

class Canv(Canvas):

    def __init__(self):
        super().__init__()
        self.initCanv()
        self.pack()

    def initCanv(self):
        self.draw_buffer = []
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
        self.top_right = [self.winfo_x(), 0]
        self.top_left =  [0, 0]
        self.bottom_right = [0, self.winfo_y()]
        self.bottom_left = [self.winfo_x(), self.winfo_y()]
        self.diagonal_up = subtract(self.top_right, self.bottom_left)
        self.diagonal_down = subtract(self.top_left, self.bottom_right)
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
        if key == "d":
            Rhombe.reset()

class Rhombe(Canv):

    def __init__(self, arg):
        self.reset()

    def reset():
        self.top_pt = Canv.top_left + times_scalar(0.5, Canv.diagonal_up)
        self.bottom_pt = subtract(self.right_pt, Canv.diagonal_up)
        self.right_pt = subtract(self.top_pt, Canv.diagonal_down)
        self.left_pt = add(self.bottom_pt, Canv.diagonal_down)
        self.mid_top_right_pt = Canv.top_right
        self.mid_top_left_pt = Canv.top_left
        self.mid_bottom_right_pt = Canv.bottom_right
        self.mid_bottom_left_pt = Canv.bottom_left
        self.center_pt = add(Canv.bottom_left, times_scalar(0.5, Canv.diagonal_up))
        self.zoom = 0

        Canv.draw_buffer = [self.top_pt, self.right_pt, self.bottom_pt, self.left_pt, \
                            self.top_pt, self.mid_top_right_pt, \
                            self.mid_bottom_left_pt, self.bottom_pt, \
                            self.mid_bottom_right_pt, self.mid_top_left_pt]

    def contract_to(left_point):
        self.new_top = self.left_point + times_scalar(0.5, subtract(self.top_pt, self.left_pt))
        self.new_bottom = self.left_point + times_scalar(0.5, subtract(self.bottom_pt, self.left_pt))
        self.new_right = self.left_point + times_scalar(0.5, subtract(self.right_pt, self.left_pt))

        self.top_pt = self.new_top
        self.bottom_pt = self.new_bottom
        self.right_pt = self.new_right
        self.left_pt = left_point
        self.mid_top_right_pt = add(self.new_right, times_scalar(0.5, subtract(self.new_top, self.new_right)))
        self.mid_top_left_pt = add(left_point, times_scalar(0.5, subtract(self.new_top, left_point)))
        self.mid_bottom_right_pt = add(self.new_right, times_scalar(0.5, subtract(self.new_bottom, self.new_right)))
        self.mid_bottom_left_pt =  add(left_point, times_scalar(0.5, subtract(self.new_bottom, left_point)))
        self.center_pt = add(left_point, times_scalar(0.5, subtract(self.new_right, left_point)))
        self.zoom += 1

        Canv.draw_buffer = [self.top_pt, self.right_pt, self.bottom_pt, self.left_pt, \
                            self.top_pt, self.mid_top_right_pt, \
                            self.mid_bottom_left_pt, self.bottom_pt, \
                            self.mid_bottom_right_pt, self.mid_top_left_pt]

        if self.zoom > 10:
            reset()

def add(a, b):
    # Vector addition
    return [a[0] + b[0], a[1] + b[1]]

def subtract(a, b):
    # Vector subtraction
    return [a[0] - b[0], a[1] - b[1]]

def times_scalar(t, a):
    # Scalar times Vector
    return [t * a[0], t * a[1]]

def main():

    root = Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 0.93)
    root.wm_attributes('-fullscreen', 1)
    # root.geometry("500x500+300+800")
    # app = Example()
    app = Canv()

    root.mainloop()


if __name__ == '__main__':
    main()
