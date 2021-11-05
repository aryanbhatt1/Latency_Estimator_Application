# Created By Team SumShakti

# importing libraries
import math
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
        page_layout = (register_user_screen, startPage, Bullet, Video_Latency, UGV_Vehicle_Control,
                       obstacleDetectionModule, perception_module, NetworkLatencyCommunicationModule,
                       perception_module_info)
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
        tk.Button(self, text="Get In", height="2", width="30", bg="#093d81", fg="white",
                  command=lambda: controller.show_frame(startPage)).grid(
            row=10, sticky=tk.S)
        tk.Button(self, text="About", height="2", width="30", bg="#093d81", fg="white").grid(
            row=13, sticky=tk.S, pady=5)


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
                            command=lambda: controller.show_frame(perception_module))
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
        button5 = tk.Button(self, text="Network Latency Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(Video_Latency))
        button5.pack()
        button5.place(x=260, y=150)
        button6 = tk.Button(self, text="Over All Latency", width=25, height=2, bg="#093d81", fg="white")
        button6.pack()
        button6.place(x=485, y=150)
        button10 = tk.Button(self, text="Go Back!!", width=25, height=2, bg="red", fg="white",
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

    class DBW_module(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)


class perception_module_info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Perception Module (More Info)", bg="#093d81", fg="white",
                 font=("Calibri", 13), width=80, height=2).grid(row=0)
        load = Image.open("img/perception_module.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, sticky=tk.E)
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=3, sticky=tk.E, padx=60, pady=40)
        Back_button = tk.Button(self, text="Back", bg="#154c79", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(perception_module))
        Back_button.grid(row=3, sticky=tk.W, padx=260, pady=40)


def calculate_x_analogue():
    x = 1
    return x


class perception_module(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Perception Module", fg="#093d81", font=("Calibri", 13), padx=10,
                 height=2).grid(row=0, sticky=tk.W)
        tk.Label(self, text="Digital Camera", fg="#093d81", font=("Calibri", 13), padx=10, pady=5,
                 height=2).grid(row=1, sticky=tk.W)
        self.myText = tk.StringVar()
        tk.Label(self, text="Frame Width").grid(row=2, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Frame Height").grid(row=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Bits/Pixel").grid(row=4, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="compression %").grid(row=5, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="FPS").grid(row=6, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=7, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=7, pady=5, column=1, sticky=tk.W)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)
        self.e5 = tk.Entry(self)

        self.e1.grid(row=2, column=1)
        self.e2.grid(row=3, column=1)
        self.e3.grid(row=4, column=1)
        self.e4.grid(row=5, column=1)
        self.e5.grid(row=6, column=1)

        self.e1.insert(0, "1280")
        self.e2.insert(0, "960")
        self.e3.insert(0, "12")
        self.e4.insert(0, "0.6")
        self.e5.insert(0, "20")
        b = tk.Button(self, text="Calculate", height=2, bg="#093d81", fg="white",
                      command=lambda: self.digital_latency())
        b.grid(row=9, column=1, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=12, column=3, pady=30, sticky=tk.W)
        More_Info = tk.Button(self, text="More Info", bg="#1e81b0", fg="white", width=20, height=2,
                              command=lambda: controller.show_frame(perception_module_info))
        More_Info.grid(row=12, column=4, pady=30, padx=5, sticky=tk.W)

        tk.Label(self, text="Analogue Camera", fg="#093d81", font=("Calibri", 13), padx=10, pady=5,
                 height=2).grid(row=1, column=3, sticky=tk.W)
        self.myText2 = tk.StringVar()
        tk.Label(self, text="Frame Width").grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Frame Height").grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Bits/Pixel").grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="compression %").grid(row=5, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="FPS").grid(row=6, padx=10, column=3, pady=5, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=7, padx=10, column=3, pady=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText2).grid(row=7, column=4, pady=5, sticky=tk.W)

        self.e6 = tk.Entry(self)
        self.e7 = tk.Entry(self)
        self.e8 = tk.Entry(self)
        self.e9 = tk.Entry(self)
        self.e10 = tk.Entry(self)

        self.e6.grid(row=2, column=4)
        self.e7.grid(row=3, column=4)
        self.e8.grid(row=4, column=4)
        self.e9.grid(row=5, column=4)
        self.e10.grid(row=6, column=4)
        b1 = tk.Button(self, text="Calculate", height=2, bg="#093d81", fg="white",
                       command=lambda: self.analogue_latency())
        b1.grid(row=9, column=4, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)

    def calculate_x(self):
        x = (float(self.e2.get()) * float(self.e1.get()) * float(self.e3.get()) * float(self.e4.get()) * float(self.e5.get()))/1000000
        return x

    def digital_latency(self):
        communication_latency = 10
        Radio_latency = 10
        display = 50
        d_latency = ((self.calculate_x() / 100) * 0.001)+communication_latency+Radio_latency+display
        self.myText.set(str(d_latency) + " ms")

    def analogue_latency(self):
        communication_late = 10


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
        tk.Label(self, text="Time Taken by Bullet to hit the target....", fg="#093d81", font=("Calibri", 13),
                 height=2).grid(row=0)
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

        b = tk.Button(self, text="Calculate", bg="#093d81", fg="white", width=20, height=2,
                      command=lambda: self.calculate())
        b.grid(row=6, column=1, sticky=tk.W + tk.E + tk.N + tk.S)
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=7, column=2, sticky=tk.E, padx=60, pady=180)


class NetworkLatencyCommunicationModule(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Network Latency Communication Module (More Info)", bg="#093d81", fg="white",
                 font=("Calibri", 13),
                 width=80, height=2).grid(row=0)
        load = Image.open("img/network_latency_communication_module.png")
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, sticky=tk.E)
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=3, sticky=tk.E, padx=60, pady=180)
        Back_button = tk.Button(self, text="Back", bg="#154c79", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(Video_Latency))
        Back_button.grid(row=3, sticky=tk.W, padx=260, pady=180)


class Video_Latency(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Network Latency Communication Module", fg="#093d81", font=("Calibri", 13), padx=80,
                 height=2).grid(row=0)
        self.myText = tk.StringVar()
        tk.Label(self, text="Frame Width").grid(row=1, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="Frame Height").grid(row=2, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="FPS").grid(row=3, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="Distance").grid(row=4, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=5, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=5, pady=5, column=1, sticky=tk.W)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)

        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        self.e3.grid(row=3, column=1)
        self.e4.grid(row=4, column=1)

        self.e1.insert(0, "1280")
        self.e2.insert(0, "960")
        self.e3.insert(0, "60")

        b = tk.Button(self, text="Calculate", height=2, bg="#093d81", fg="white",
                      command=lambda: self.calculate_latency())
        b.grid(row=6, column=1, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=8, column=1, sticky=tk.SE, pady=160)
        More_Info = tk.Button(self, text="More Info", bg="#1e81b0", fg="white", width=20, height=2,
                              command=lambda: controller.show_frame(NetworkLatencyCommunicationModule))
        More_Info.grid(row=8, column=0, sticky=tk.E, pady=160, padx=40)

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
