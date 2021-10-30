# Created By Team SumShakti

# importing libraries
import math
import os
import tkinter as tk

from PIL import ImageTk, Image


# Class App
class App(tk.Tk):

    # __init__ function for class App
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Title and Layout size of App
        self.title('Latency Estimator')
        self.geometry('700x500')

        # Creating a container
        container = tk.Frame(self, bg="white")
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        page_layout = (register_user_screen, register, log_in, startPage, Bullet, Video_Latency, UGV_Vehicle_Control,
                       obstacleDetectionModule)
        for F in page_layout:
            frame = F(container, self)

            # initializing frame of that object from startPage, Bullet respectively with for loop
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(register_user_screen)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class register_user_screen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Welcome To Latency Estimator Application ", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).grid(row=0)
        load = Image.open("img/cvrde-drdo-logo.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, pady=70)
        tk.Button(self, text="Login", height="2", width="30", bg="#093d81", fg="white",
                  command=lambda: controller.show_frame(log_in)).grid(
            row=10, sticky=tk.S)
        tk.Button(self, text="Register", height="2", width="30", bg="#093d81", fg="white",
                  command=lambda: controller.show_frame(register)).grid(
            row=13, sticky=tk.S, pady=5)


class register(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self, text="Please enter details below", bg="#093d81", fg="white", font=("Calibri", 13), width=80,
                 height=2).pack()
        tk.Label(self, text="").pack()
        self.username_lable = tk.Label(self, text="Username * ", font=("Calibri", 13))
        self.username_lable.pack()
        self.username_entry = tk.Entry(self, font=("Calibri", 10), textvariable=self.username)
        self.username_entry.pack()
        self.password_lable = tk.Label(self, text="Password * ", font=("Calibri", 13))
        self.password_lable.pack()
        self.password_entry = tk.Entry(self, textvariable=self.password, show='*', font=("Calibri", 10))
        self.password_entry.pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Register", width=20, height=2, bg="#093d81", fg="white",
                  command=lambda: self.register_user()).pack()
        tk.Button(self, text="Back", width=20, height=2,
                  command=lambda: controller.show_frame(register_user_screen)).pack(pady=8)

    def register_user(self):
        self.username_info = self.username.get()
        self.password_info = self.password.get()
        file = open(self.username_info, "w")
        file.write(self.username_info + "\n")
        file.write(self.password_info)
        file.close()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        tk.Label(self, text="Registration Success", fg="green", font=("calibri", 11)).pack()


class log_in(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Please enter details below to login", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).pack()
        tk.Label(self, text="").pack()
        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()
        tk.Label(self, text="Username * ", font=("Calibri", 13)).pack()
        self.username_login_entry = tk.Entry(self, textvariable=self.username_verify, width=20)
        self.username_login_entry.pack()
        tk.Label(self, text="").pack()
        tk.Label(self, text="Password * ", font=("Calibri", 13)).pack()
        self.password_login_entry = tk.Entry(self, textvariable=self.password_verify, show='*', width=20)
        self.password_login_entry.pack()
        tk.Label(self, text="").pack()
        tk.Button(self, text="Login", width=20, height=2, bg="#093d81", fg="white",
                  command=lambda: (self.login_verify(parent, controller))).pack()
        tk.Button(self, text="Back", width=20, height=2,
                  command=lambda: controller.show_frame(register_user_screen)).pack(pady=8)

    def login_verify(self, parent, controller):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_login_entry.delete(0, tk.END)
        self.password_login_entry.delete(0, tk.END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                controller.show_frame(startPage)


# first window frame startPage
class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Choose An Option", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).pack()
        button1 = tk.Button(self, text="Bullet", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(Bullet))
        button1.pack()
        button1.place(x=30, y=75)

        button2 = tk.Button(self, text="Perception Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(Video_Latency))
        button2.pack()
        button2.place(x=260, y=75)

        button3 = tk.Button(self, text="DBW Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(UGV_Vehicle_Control))
        button3.pack()
        button3.place(x=485, y=75)

        button4 = tk.Button(self, text="Obstacle Detection Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(obstacleDetectionModule))
        button4.pack()
        button4.place(x=30, y=150)
        button5 = tk.Button(self, text="button4", width=25, height=2, bg="#093d81", fg="white")
        button5.pack()
        button5.place(x=260, y=150)
        button6 = tk.Button(self, text="button4", width=25, height=2, bg="#093d81", fg="white")
        button6.pack()
        button6.place(x=485, y=150)
        button7 = tk.Button(self, text="button4", width=25, height=2, bg="#093d81", fg="white")
        button7.pack()
        button7.place(x=30, y=225)
        button8 = tk.Button(self, text="button4", width=25, height=2, bg="#093d81", fg="white")
        button8.pack()
        button8.place(x=260, y=225)
        button9 = tk.Button(self, text="button4", width=25, height=2, bg="#093d81", fg="white")
        button9.pack()
        button9.place(x=485, y=225)
        button10 = tk.Button(self, text="Log Out!!", width=25, height=2, bg="red", fg="white",
                            command=lambda: controller.show_frame(register_user_screen))
        button10.pack()
        button10.place(x=485, y=300)


class UGV_Vehicle_Control(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="DBW Module", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).grid(row=0)
        load = Image.open("img/DBW_Module.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, sticky=tk.N)
        UGV_Vehicle_Control_back_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                                    command=lambda: controller.show_frame(startPage))
        UGV_Vehicle_Control_back_button.grid(row=3, sticky=tk.E, padx=50)

class perception_module(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Perception Module", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).grid(row=0)

class obstacleDetectionModule(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Obstacle Detection Module", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).grid(row=0)
        load = Image.open("img/obstacle_detection_module.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, sticky=tk.N)
        UGV_Vehicle_Control_back_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                                    command=lambda: controller.show_frame(startPage))
        UGV_Vehicle_Control_back_button.grid(row=3, sticky=tk.E, padx=40)

class Bullet(tk.Frame):
    def calculate(self):
        time = int(self.e4.get()) / int(self.e2.get()) * math.cos(int(self.e3.get()))
        g = 9.8
        time2 = (math.sqrt(
            2 * g * int(self.e1.get()) + math.pow((int(self.e2.get()) * math.sin(int(self.e3.get()))), 2))) / g
        if time2 >= time:
            self.myText.set(str(round(time, 4)) + " sec")
        else:
            self.myText.set("Not Possible")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.myText = tk.StringVar()
        tk.Label(self, text="Choose An Option", fg="#093d81", font=("Calibri", 13), height=2).grid(row=0)
        tk.Label(self, text="Height (m)").grid(row=1, sticky=tk.W)
        tk.Label(self, text="Velocity (m/s)").grid(row=2, sticky=tk.W)
        tk.Label(self, text="Angle of elevation (degree)").grid(row=3, sticky=tk.W)
        tk.Label(self, text="Distance (m)").grid(row=4, sticky=tk.W)
        tk.Label(self, text="Result : ").grid(row=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=5, column=1, sticky=tk.W)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        self.e3.grid(row=3, column=1)
        self.e4.grid(row=4, column=1)

        self.e1.insert(0, "0")
        self.e2.insert(0, "0")
        self.e3.insert(0, "0")
        self.e4.insert(0, "0")

        b = tk.Button(self, text="Calculate", command=lambda: self.calculate())
        b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)


class Video_Latency(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.myText = tk.StringVar()
        tk.Label(self, text="Stages").grid(row=0, sticky=tk.W)
        tk.Label(self, text="MB per line").grid(row=1, sticky=tk.W)
        tk.Label(self, text="System Clock").grid(row=2, sticky=tk.W)
        tk.Label(self, text="Distance").grid(row=3, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=4, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=4, column=1, sticky=tk.W)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        b = tk.Button(self, text="Calculate", command=lambda: self.calculate_latency())
        b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)

    def calculate_latency(self):
        tencode = ((int(self.e2.get()) + int(self.e1.get())) * 613) / int(self.e3.get()) / 1000
        toutputbuff = (int(self.e4.get()) * int(self.e2.get())) / 8160
        tinputbuff = toutputbuff
        tdecoder = ((3 * 640) / int(self.e3.get())) / 1000
        t_all = (tencode + toutputbuff + tinputbuff + tdecoder)
        self.myText.set(str(t_all) + " ms")


# Main Program;
if "__main__" == __name__:
    app = App()
    app.mainloop()
