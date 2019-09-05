from tkinter import Tk, Frame, Canvas, Label, Button, DISABLED


class CloseAfterFinishFrame(Frame):  # Diz que herda os parametros de Frame
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)  # Inicializa com os parametros acima!!
        Label(self, text="Hey", font=("Arial", 16)).pack()
        button = Button(self, text="the End",
                        command=self.CloseWindow, font=("Arial", 12))
        button.pack()
        # Canv(self.master)
        NewFrame(self.master)
        self.pack()

    def CloseWindow(self):
        # root.quit()
        # self.button.config(state=DISABLED)
        self.forget()
        NewFrame(self.master)


class NewFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        button = Button(self, text="Gyf", command=self.CloseWindow)
        button.pack()
        self.pack()

    def CloseWindow(self):
        root.quit()


class Canv(Canvas):

    def __init__(self):
        super().__init__()
    #     self.initCanv(master)
    #     self.pack()
    #
    # def initCanv(self):
        self.master.title("Cat")
        self.bind_all("<Key>", self.key_pressed)

        self.width = 500  # self.master.winfo_screenwidth()
        self.height = 500  # self.master.winfo_screenheight()
        print("Screen dimensions", self.width, self.height)
        self.mouse_xy = [self.width/2, self.height/2]

        self.canvas = Canvas(width=self.width - 10, height=self.height - 10,
                             bg='light blue')
        # Mouse placement stop working if the canvas is fullscreen. Go figure.
        self.canvas.create_line(0, 0, 450, 450,
                                width=2, fill="red", dash=(8, 8))

        self.canvas.pack(fill='both', expand=True)


root = Tk()
CloseAfterFinishFrame(root)
root.mainloop()

# from tkinter import Tk, Canvas, Frame, BOTH
#
#
# class Example(Frame):
#
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         self.master.title("Lines")
#         self.pack(fill=BOTH, expand=1)
#
#         canvas = Canvas(self)
#         canvas.create_line(15, 25, 200, 25)
#         canvas.create_line(300, 35, 300, 200, dash=(4, 2))
#         canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
#
#         canvas.pack(fill=BOTH, expand=1)
#
#
# def main():
#
#     root = Tk()
#     ex = Example()
#     root.geometry("400x250+300+300")
#     print("Raf?")
#     root.mainloop()
#     print("Ruf?")
#
#
# if __name__ == '__main__':
#     main()