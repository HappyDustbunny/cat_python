# import pyautogui
# import sys
from tkinter import Tk, Canvas, Frame  # , BOTH
# from tkinter.ttk import Frame


class Frame1(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.canv = Canv()


class Canv(Canvas):

    def __init__(self):
        super().__init__()
        self.initCanv()
        self.pack()

    def initCanv(self):
        # self.root = Tk()
        # self.root.wait_visibility(self.root)
        # self.root.wm_attributes('-alpha', 0.3)
        # self.root.wm_attributes('-fullscreen', 1)

        self.draw_buffer = []

        self.master.title("Cat")
        self.bind_all("<Key>", self.key_pressed)

        self.width = self.master.winfo_screenwidth()
        self.height = self.master.winfo_screenheight()
        print("Screen dimensions", self.width, self.height)
        self.mouse_xy = [self.width/2, self.height/2]

        self.canvas = Canvas(width=self.width - 10, height=self.height - 10,
                             bg='light blue')
        # Mouse placement stop working if the canvas is fullscreen. Go figure.

        self.canvas.pack(fill='both', expand=True)
        # self.root.mainloop()

        self.after(100, self.get_offset)

    def get_offset(self):
        """
        Get offset neede to place mouse pointer.

        Canvas has to initialised, so this can't be in initCanv.
        """

        self.off_set_x = self.winfo_x()
        self.off_set_y = self.winfo_y()
        self.top_right = [self.width, 0]
        self.top_left = [0, 0]
        self.bottom_left = [0, self.height]
        self.bottom_right = [self.width, self.height]
        self.diagonal_up = subtract(self.bottom_left, self.top_right)
        self.diagonal_down = subtract(self.top_left, self.bottom_right)
        self.upstart = 1
        self.reset()
        print("Canvas offset ", self.off_set_x, self.off_set_y)
        self.after(100, self.timer_event)

    def draw(self):
        """ Draw rhombe from corners and middle of sides """

        self.draw_buffer = [self.top_pt, self.right_pt, self.bottom_pt,
                            self.left_pt, self.top_pt, self.mid_top_right_pt,
                            self.mid_bottom_left_pt, self.bottom_pt,
                            self.mid_bottom_right_pt, self.mid_top_left_pt]

        for i, end in enumerate(self.draw_buffer):
            if i == 0:
                start = end
                continue
            self.canvas.create_line(start[0], start[1], end[0], end[1],
                                    width=2, fill="red", dash=(8, 8))

            self.canvas.pack(side='top', fill='both', expand=True)
            start = end

    def timer_event(self):

        self.draw()

        self.after(100, self.timer_event)
        # The first number is time between updates in milliseconds.

    def key_pressed(self, e):

        key = e.keysym

        if key == "Left" or key == "a":
            if self.left_pt[0] >= 0 or self.zoom < 1:  # Stay on screen...
                self.contract_to(self.left_pt)
                print("Left")
        if key == "Right" or key == "d":
            if self.right_pt[0] <= self.width or self.zoom < 1:  # Excpt 1 time
                self.contract_to(self.center_pt)
                print("Right")
        if key == "Up" or key == "w":
            if self.top_pt[1] >= 0 or self.zoom < 1:
                self.contract_to(self.mid_top_left_pt)
                print("Up")
        if key == "Down" or key == "s":
            if self.bottom_pt[1] <= self.height or self.zoom < 1:
                self.contract_to(self.mid_bottom_left_pt)
                print("Down")
        if key == "e" or key == "q":
            self.mouse_xy = self.center_pt
            print(self.mouse_xy)
            self.event_generate('<Motion>', warp=True,  # Place mouse pointer
                                x=self.mouse_xy[0] - self.off_set_x,
                                y=self.mouse_xy[1] - self.off_set_y)
            self.end()

            # sys.exit()
            # self.reset()
        if key == '<space>':
            print("Yay")

    def end(self):
        root.quit()

    def reset(self):
        """ Clear canvas. Set corners and midpoint for screenfilling rhombe"""
        self.canvas.delete("all")

        self.top_pt = add(self.top_left, times_scalar(-0.5, self.diagonal_up))
        self.right_pt = subtract(self.top_pt, self.diagonal_down)
        self.bottom_pt = add(self.right_pt, self.diagonal_up)
        self.left_pt = add(self.bottom_pt, self.diagonal_down)
        self.mid_top_right_pt = self.top_right
        self.mid_top_left_pt = self.top_left
        self.mid_bottom_right_pt = self.bottom_right
        self.mid_bottom_left_pt = self.bottom_left
        self.center_pt = add(self.bottom_left,
                             times_scalar(-0.5, self.diagonal_up))
        self.zoom = 0

        self.event_generate('<Motion>', warp=True,  # Place mouse pointer
                            x=self.mouse_xy[0] - self.off_set_x,
                            y=self.mouse_xy[1] - self.off_set_y)

    def contract_to(self, left_point):
        """ Contract rhombe to the quarter rhombe definde by the left point """

        self.canvas.delete("all")

        self.new_top = add(left_point,
                           times_scalar(0.5, subtract(self.top_pt,
                                                      self.left_pt)))
        self.new_bottom = add(left_point,
                              times_scalar(0.5, subtract(self.bottom_pt,
                                                         self.left_pt)))
        self.new_right = add(left_point,
                             times_scalar(0.5, subtract(self.right_pt,
                                                        self.left_pt)))
        self.top_pt = self.new_top
        self.bottom_pt = self.new_bottom
        self.right_pt = self.new_right
        self.left_pt = left_point
        self.mid_top_right_pt = add(self.new_right,
                                    times_scalar(0.5,
                                                 subtract(self.new_top,
                                                          self.new_right)))
        self.mid_top_left_pt = add(left_point,
                                   times_scalar(0.5,
                                                subtract(self.new_top,
                                                         left_point)))
        self.mid_bottom_right_pt = add(self.new_right,
                                       times_scalar(0.5,
                                                    subtract(self.new_bottom,
                                                             self.new_right)))
        self.mid_bottom_left_pt = add(left_point,
                                      times_scalar(0.5,
                                                   subtract(self.new_bottom,
                                                            left_point)))
        self.center_pt = add(left_point,
                             times_scalar(0.5,
                                          subtract(self.new_right,
                                                   left_point)))
        self.mouse_xy = self.center_pt

        self.zoom += 1  # Place pointer if the rhombe is only a few pixels
        if self.zoom > 8:
            self.reset()


def add(a, b):
    """ Add vectors a and b """

    return [a[0] + b[0], a[1] + b[1]]


def subtract(a, b):
    """ Subtract vectors a and b.   (a - b) """

    return [a[0] - b[0], a[1] - b[1]]


def times_scalar(t, a):
    """ Multiply vector a with scalar t """

    return [t * a[0], t * a[1]]


def main():

    root = Tk()
    root.wait_visibility(root)
    root.wm_attributes('-alpha', 0.3)
    root.wm_attributes('-fullscreen', 1)

    # root.bind("r", root.iconify())
    # pyautogui.moveTo(100, 200)
    # pyautogui.click()

    # app = Canv(root)
    app = Frame1(root)
    # app.config(scrollregion=app.bbox('all'))  # No effect. Shuts up PEP8
    root.mainloop()
    # root.destroy()


if __name__ == '__main__':
    main()
