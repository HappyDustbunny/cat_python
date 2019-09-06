
    # root.wait_visibility(root)
    # root.wm_attributes('-alpha', 0.3)
    # root.wm_attributes('-fullscreen', 1)
    #
    # app = Canv(root)

    root.mainloop()

    # pyautogui.click()
    #
    # # Move the mousepointer to the upper rigth corner
    # pyautogui.moveTo(pyautogui.size()[0] - 50, 50)


if __name__ == '__main__':
    main()


# from tkinter import Tk, Frame, Canvas, Label, Button
#
#
# class CloseAfterFinishFrame(Frame):  # Diz que herda os parametros de Frame
#     def __init__(self, master):
#         self.master = master
#         Frame.__init__(self, master)  # Inicializa com os parametros acima!!
#         Label(self, text="Hey", font=("Arial", 16)).pack()
#         button = Button(self, text="the End",
#                         command=self.CloseWindow(master), font=("Arial", 12))
#         button.pack()
#         self.canv = Canv()
#         # self.bind_all("<Key>", self.key_pressed)
#         # Canv(self.master)
#         # NewFrame(self.master)
#         self.pack()
#
#     def CloseWindow(self, master):
#         # root.quit()
#         # self.button.config(state=DISABLED)
#         self.master.destroy()
#         # self.forget()
#         # NewFrame(self.master)
#
#
# class NewFrame(Frame):
#     def __init__(self, master):
#         Frame.__init__(self, master)
#         button = Button(self, text="Gyf", command=self.CloseWindow)
#         button.pack()
#         self.pack()
#
#     def CloseWindow(self):
#         root.quit()
#
#
# class Canv(Canvas):
#
#     def __init__(self):
#         super().__init__()
    #     self.initCanv(master)
        # self.pack()
    #
    # def initCanv(self):
        # self.master.title("Cat")
        # self.bind_all("<Key>", self.key_pressed)
        #
        # self.width = 500  # self.master.winfo_screenwidth()
        # self.height = 500  # self.master.winfo_screenheight()
        # print("Screen dimensions", self.width, self.height)
        # self.mouse_xy = [self.width/2, self.height/2]
#         #
#         self.canvas = Canvas(width=400, height=400)
#         # Mouse placement stop working if the canvas is fullscreen. Go figure.
#         self.canvas.create_line(0, 0, 350, 350,
#                                 width=2, fill="red", dash=(8, 8))
#
#         self.canvas.pack(fill='both', expand=True)
#
#
# root = Tk()
# CloseAfterFinishFrame(root)
# root.mainloop()

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
