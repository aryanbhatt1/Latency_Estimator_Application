""" Created By Team SumShakti on 18th October

Topic : End To End Latency Estimator

Team SumShakti
1. Aryan Bhatt
2. Himanshu R Singh
3. Jayesh Baibhav
4. Jyothisman Ghatak
5. Vivek Krishna
"""

# importing libraries
import math
import tkinter as tk
from tkinter import ttk
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
        page_layout = (register_user_screen, startPage, Bullet, CommunicationModule, DBW_module, DBW_module_info,
                       obstacleDetectionModule, perception_module, NetworkLatencyCommunicationModule,
                       perception_module_info, Total_latency)
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


# User Screen Class
class register_user_screen(tk.Frame):

    # __init__ function for class register_user_screen
    def __init__(self, parent, controller):
        # __init__ function for class Tk
        tk.Frame.__init__(self, parent)

        # Header Label For class register_user_screen with properties
        tk.Label(self, text="Welcome To Latency Estimator Application ", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).grid(row=0)

        # Loading CVRDE logo in the tkinter frame
        load = Image.open("img/cvrde-drdo-logo.png")

        # Rendering loaded image in the frame
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, pady=70)

        # button for "Main Screen" Frame
        tk.Button(self, text="Get In", height="2", width="30", bg="#093d81", fg="white",
                  command=lambda: controller.show_frame(startPage)).grid(
            row=10, sticky=tk.S)

        # button for "About" Frame
        tk.Button(self, text="About", height="2", width="30", bg="#093d81", fg="white").grid(
            row=13, sticky=tk.S, pady=5)


# first window frame startPage
class startPage(tk.Frame):

    # __init__ function for startPage class
    def __init__(self, parent, controller):
        # __init__ function for Tk class
        tk.Frame.__init__(self, parent)

        # Header Label for class startPage i.e. Main Screen
        tk.Label(self, text="Choose An Option", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).pack()

        # Button for Bullet Frame or class Bullet
        button1 = tk.Button(self, text="Bullet", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(Bullet))
        button1.pack()
        button1.place(x=30, y=75)

        # Button for Class perception_module
        button2 = tk.Button(self, text="Perception Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(perception_module))
        button2.pack()
        button2.place(x=260, y=75)

        # Button for DBW_module class
        button3 = tk.Button(self, text="DBW Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(DBW_module))
        button3.pack()
        button3.place(x=485, y=75)

        # Button for obstacleDetectionModule class
        button4 = tk.Button(self, text="Obstacle Detection Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(obstacleDetectionModule))
        button4.pack()
        button4.place(x=30, y=150)

        # Button for Network Latency Module or communication Module Class
        button5 = tk.Button(self, text="Communication Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(CommunicationModule))
        button5.pack()
        button5.place(x=260, y=150)

        # Button for Over all Latency class
        button6 = tk.Button(self, text="Total Latency", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(Total_latency))
        button6.pack()
        button6.place(x=485, y=150)

        # Button for Go Back button
        button10 = tk.Button(self, text="Go Back!!", width=25, height=2, bg="red", fg="white",
                             command=lambda: controller.show_frame(register_user_screen))
        button10.pack()
        button10.place(x=485, y=300)


# Bullet latency Calculation Frame Page
class Bullet(tk.Frame):

    # __init__ function for Bullet Latency
    def __init__(self, parent, controller):

        # __init__ function for Tk Class
        tk.Frame.__init__(self, parent)

        # String for storing Final Latency
        self.myText = tk.StringVar()

        # Header Label For class Bullet
        tk.Label(self, text="Time Taken by Bullet to hit the target....", fg="#093d81", font=("Calibri", 13),
                 height=2).grid(row=0)
        # Height Label
        tk.Label(self, text="Height (m)").grid(row=1, sticky=tk.W)
        # Velocity Label
        tk.Label(self, text="Velocity (m/s)").grid(row=2, sticky=tk.W)
        # Angle of Elevation Label
        tk.Label(self, text="Angle of elevation (degree)").grid(row=3, sticky=tk.W)
        # Distance Label
        tk.Label(self, text="Distance (m)").grid(row=4, sticky=tk.W)
        # Latency result Label
        tk.Label(self, text="Result : ").grid(row=5, sticky=tk.W)
        # Label for displaying string myText
        tk.Label(self, text="", textvariable=self.myText).grid(row=5, column=1, sticky=tk.W)

        # Entry for storing value for Label Height
        self.e1 = tk.Entry(self)
        self.e1.grid(row=1, column=1)
        # Entry for storing value for Label Velocity
        self.e2 = tk.Entry(self)
        self.e2.grid(row=2, column=1)
        # Entry for storing value for Label Angle of Elevation
        self.e3 = tk.Entry(self)
        self.e3.grid(row=3, column=1)
        # Entry for storing value for Label Distance
        self.e4 = tk.Entry(self)
        self.e4.grid(row=4, column=1)

        # Default Value for Height
        self.e1.insert(0, "2")
        # Default Value for Velocity
        self.e2.insert(0, "100")
        # Default Value for Angle of Elevation
        self.e3.insert(0, "30")
        # Default Value for Distance
        self.e4.insert(0, "50")

        # Button for calculating Latency for bullet to hit the target
        b = tk.Button(self, text="Calculate", bg="#093d81", fg="white", width=20, height=2,
                      command=lambda: self.calculate())
        b.grid(row=6, column=1, sticky=tk.W + tk.E + tk.N + tk.S)

        # Home Button for navigating to Main Screen or Start Page
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=7, column=2, sticky=tk.E, padx=60, pady=180)

    # Function to calculate Time taken by bullet to hit the Target
    def calculate(self):

        # variable to store calculated time1
        time = int(self.e4.get()) / int(self.e2.get()) * math.cos(int(self.e3.get()))
        # value of g (gravity)
        g = 9.8

        # variable to store calculated time2
        time2 = (math.sqrt(
            2 * g * int(self.e1.get()) + math.pow((int(self.e2.get()) * math.sin(int(self.e3.get()))), 2))) / g

        if time2 >= time:
            self.myText.set(str(round(time, 4)) + " sec")
        else:
            self.myText.set("Not Possible")


# Class DBW Module
class DBW_module(tk.Frame):

    # __init__ function for DBW_module class
    def __init__(self, parent, controller):
        # __init__ function for Tk Class
        tk.Frame.__init__(self, parent)

        # Header Label For DBW module
        tk.Label(self, text="DBW Module", fg="#093d81", font=("Calibri", 13), padx=10,
                 height=2).grid(row=0, sticky=tk.W)

        # Base Station to UGV Latency
        tk.Label(self, text="Base Station to UGV Latency", fg="#093d81", font=("Calibri", 13), padx=10, pady=5,
                 height=2).grid(row=1, sticky=tk.W)

        # String for storing Base Station to UGV Latency
        self.myText = tk.StringVar()

        # Label Command to UGV Latency
        tk.Label(self, text="Command to UGV Latency").grid(row=2, padx=10, pady=5, sticky=tk.W)
        # Label ES Latency
        tk.Label(self, text="ES Latency").grid(row=3, padx=10, pady=5, sticky=tk.W)
        # Label Radio Latency
        tk.Label(self, text="Radio Latency").grid(row=4, padx=10, pady=5, sticky=tk.W)
        # Label Result
        tk.Label(self, text="Result:").grid(row=5, padx=10, pady=5, sticky=tk.W)
        # Label To store Result string
        tk.Label(self, text="", textvariable=self.myText).grid(row=5, pady=5, column=1, sticky=tk.W)

        # Entry for storing value for Label Command to UGV Latency
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=1)
        # Entry for storing value for Label ES Latency
        self.e2 = tk.Entry(self)
        self.e2.grid(row=3, column=1)
        # Entry for storing value for Label Radio Latency
        self.e3 = tk.Entry(self)
        self.e3.grid(row=4, column=1)

        # Default value for Entry Command to UGV Latency
        self.e1.insert(0, "35")
        # Default value for Entry ES Latency
        self.e2.insert(0, "10")
        # Default value for Entry Radio Latency
        self.e3.insert(0, "2")

        # Calculate button to call function base_station_to_ugv_latency()
        b = tk.Button(self, text="Calculate", height=2, bg="#093d81", fg="white",
                      command=lambda: self.base_station_to_ugv_latency())
        b.grid(row=9, column=1, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)

        # Button to open frame startPage
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=12, column=3, pady=30, sticky=tk.W)

        # Button to open frame DBW_module_info
        More_Info = tk.Button(self, text="More Info", bg="#1e81b0", fg="white", width=20, height=2,
                              command=lambda: controller.show_frame(DBW_module_info))
        More_Info.grid(row=12, column=4, pady=30, padx=5, sticky=tk.W)

    # Function base_station_to_UGV_Latency
    def base_station_to_ugv_latency(self):
        total_latency = float(self.e1.get()) + float(self.e2.get()) + float(self.e3.get())
        self.myText.set(str(total_latency) + " ms")
        global DBW_module_latency
        DBW_module_latency = total_latency


# DBW Module frame Page
class DBW_module_info(tk.Frame):

    # __init__ function for DBW_module class
    def __init__(self, parent, controller):
        # __init__ function for Tk class
        tk.Frame.__init__(self, parent)

        # Header Label For class DBW module with properties
        tk.Label(self, text="DBW Module", bg="#093d81", fg="white", font=("Calibri", 13),
                 width=80, height=2).grid(row=0)

        # Loading DBW module in the tkinter frame
        load = Image.open("img/DBW_Module.png")

        # Rendering loaded image in the frame
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, sticky=tk.N)

        # Button for "Main Screen" Frame
        DBW_module_back_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                           command=lambda: controller.show_frame(startPage))
        DBW_module_back_button.grid(row=3, sticky=tk.E, padx=50)


# Perception Module Frame Page
class perception_module(tk.Frame):

    # __init__ function for perception_module Class
    def __init__(self, parent, controller):
        # __init__ function for class TK
        tk.Frame.__init__(self, parent)

        # Header Label For Perception Module
        tk.Label(self, text="Perception Module", fg="#093d81", font=("Calibri", 13), padx=10,
                 height=2).grid(row=0, sticky=tk.W)

        # Header Label For Digital Camera
        tk.Label(self, text="Digital Camera", fg="#093d81", font=("Calibri", 13), padx=10, pady=5,
                 height=2).grid(row=1, sticky=tk.W)

        # String to Store Calculated value for Digital Camera Latency
        self.myText = tk.StringVar()
        # Label For Frame Width
        tk.Label(self, text="Frame Width").grid(row=2, padx=10, pady=5, sticky=tk.W)
        # Label For Frame Height
        tk.Label(self, text="Frame Height").grid(row=3, padx=10, pady=5, sticky=tk.W)
        # Label For Bits/pixel
        tk.Label(self, text="Bits/Pixel").grid(row=4, padx=10, pady=5, sticky=tk.W)
        # Label For compression Ratio
        tk.Label(self, text="compression %").grid(row=5, padx=10, pady=5, sticky=tk.W)
        # Label For FPS
        tk.Label(self, text="FPS").grid(row=6, padx=10, pady=5, sticky=tk.W)
        # Label For Result
        tk.Label(self, text="Result:").grid(row=7, padx=10, pady=5, sticky=tk.W)
        # Label to Store Calculated Value
        tk.Label(self, text="", textvariable=self.myText).grid(row=7, pady=5, column=1, sticky=tk.W)

        # Entry for storing value for Label Frame Width
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=1)
        # Entry for storing value for Label Frame Height
        self.e2 = tk.Entry(self)
        self.e2.grid(row=3, column=1)
        # Entry for storing value for Label Bits/Pixel
        self.e3 = tk.Entry(self)
        self.e3.grid(row=4, column=1)
        # Entry for storing value for Label Compression %
        self.e4 = tk.Entry(self)
        self.e4.grid(row=5, column=1)
        # Entry for storing value for Label FPS
        self.e5 = tk.Entry(self)
        self.e5.grid(row=6, column=1)

        # Default Value For Entry self.e1 and Label Frame Width
        self.e1.insert(0, "1280")
        # Default Value For Entry self.e2 and Label Frame Height
        self.e2.insert(0, "960")
        # Default Value For Entry self.e3 and Label Bits/Pixel
        self.e3.insert(0, "12")
        # Default Value For Entry self.e4 and Label Compression %
        self.e4.insert(0, "0.6")
        # Default Value For Entry self.e5 and Label FPS
        self.e5.insert(0, "20")

        # Button to call function digital_latency()
        b = tk.Button(self, text="Calculate", height=2, bg="#093d81", fg="white",
                      command=lambda: self.digital_latency())
        b.grid(row=9, column=1, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)

        # Button to show Frame startPage
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=12, column=3, pady=30, sticky=tk.W)

        # Button to show Frame perception_module_info
        More_Info = tk.Button(self, text="More Info", bg="#1e81b0", fg="white", width=20, height=2,
                              command=lambda: controller.show_frame(perception_module_info))
        More_Info.grid(row=12, column=4, pady=30, padx=5, sticky=tk.W)

        # Header Label For Analogue Camera
        tk.Label(self, text="Analogue Camera", fg="#093d81", font=("Calibri", 13), padx=10, pady=5,
                 height=2).grid(row=1, column=3, sticky=tk.W)

        # String to store calculated value of Analogue Camera Latency
        self.myText2 = tk.StringVar()
        tk.Label(self, text="Select Camera Type").grid(row=2, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Frame Width").grid(row=3, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Frame Height").grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="FPS").grid(row=5, column=3, padx=10, pady=5, sticky=tk.W)
        tk.Label(self, text="Select Y:Cr:Cb").grid(row=6, padx=10, column=3, pady=5, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=7, padx=10, column=3, pady=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText2).grid(row=7, column=4, pady=5, sticky=tk.W)

        n = tk.StringVar()
        n2 = tk.StringVar()
        optionSelect = ttk.Combobox(self, width=17, textvariable=n)
        optionSelect['values'] = ('PAL', 'NTSC')
        self.e7 = tk.Entry(self)
        self.e8 = tk.Entry(self)
        self.e9 = tk.Entry(self)
        self.e10 = tk.Entry(self)
        optionSelect2 = ttk.Combobox(self, width=17, textvariable=n2)
        optionSelect2['values'] = ('4:4:4', '4:4:2', '4:2:2')

        optionSelect.grid(column=4, row=2)
        optionSelect.current(0)
        self.e7.grid(row=3, column=4)
        self.e8.grid(row=4, column=4)
        self.e9.grid(row=5, column=4)
        optionSelect2.grid(column=4, row=6)
        self.m1 = 0.0
        self.m2 = 0.0
        self.m3 = 0.0
        button_options = tk.Button(self, text="Select", bg="#093d81", fg="white",
                                   command=lambda: self.insert_value(optionSelect))
        button_options.grid(row=2, column=5)
        button_options2 = tk.Button(self, text="Select", bg="#093d81", fg="white",
                                    command=lambda: self.insert_value2(optionSelect2))
        button_options2.grid(row=6, column=5)
        b1 = tk.Button(self, text="Calculate", width=17, height=2, bg="#093d81", fg="white",
                       command=lambda: self.analogue_latency(parent, controller))
        b1.grid(row=9, column=4, sticky=tk.W + tk.E + tk.N + tk.S)

    def calculate_x(self):
        x = (float(self.e2.get()) * float(self.e1.get()) * float(self.e3.get()) * float(self.e4.get()) * float(
            self.e5.get())) / 1000000
        return x

    def insert_value(self, optionSelect):
        if optionSelect.get() == "PAL":
            self.e7.insert(0, "720")
            self.e8.insert(0, "576")
            self.e9.insert(0, "25")
        else:
            self.e7.insert(0, "720")
            self.e8.insert(0, "480")
            self.e9.insert(0, "30")

    def insert_value2(self, optionSelect2):
        if optionSelect2.get() == '4:4:4':
            self.m1 = 4
            self.m2 = 4
            self.m3 = 4
        elif optionSelect2.get() == '4:4:2':
            self.m1 = 4
            self.m2 = 4
            self.m3 = 2
        elif optionSelect2.get() == '4:2:2':
            self.m1 = 4
            self.m2 = 2
            self.m3 = 2

    def digital_latency(self):
        communication_latency = 10
        Radio_latency = 10
        display = 50
        d_latency = ((self.calculate_x() / 100) * 0.001) + communication_latency + Radio_latency + display
        global digital_Latency
        digital_Latency = d_latency
        self.myText.set(str(d_latency) + " ms")

    def calculate_y(self):
        latency_y = ((float(self.e8.get()) * float(self.e7.get()) * 8) / (4 / self.m1)) + (
                (float(self.e8.get()) * float(self.e7.get()) * 8) / (4 / self.m2)) + (
                            (float(self.e8.get()) * float(self.e7.get()) * 8) / (4 / self.m3))
        final_y = (latency_y / 1000000) * (1 / 100) * 1000
        return final_y

    def analogue_latency(self, parent, controller):
        video_acq = 50
        video_compression = 55
        Radio_latency = 7
        display_latency = 50
        analogue_l = video_acq + video_compression + Radio_latency + display_latency + 2 * (self.calculate_y())
        self.myText2.set(str(analogue_l) + " ms")
        global analogue_Latency
        analogue_Latency = analogue_l

# Perception Module Page
class perception_module_info(tk.Frame):

    # __init__ function for perception_module_info class
    def __init__(self, parent, controller):
        # __init__ function for Tk class
        tk.Frame.__init__(self, parent)

        # Header Label For class Perception Module(info) with properties
        tk.Label(self, text="Perception Module (More Info)", bg="#093d81", fg="white",
                 font=("Calibri", 13), width=80, height=2).grid(row=0)

        # Loading Perception Module in the tkinter frame
        load = Image.open("img/perception_module.png")

        # Rendering loaded image in the frame
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render)
        img.image = render
        img.grid(row=2, sticky=tk.E)

        # Button for "Main Screen" Frame
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=3, sticky=tk.E, padx=60, pady=40)

        # Back button for "Perception Module" Frame
        Back_button = tk.Button(self, text="Back", bg="#154c79", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(perception_module))
        Back_button.grid(row=3, sticky=tk.W, padx=260, pady=40)


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
                                command=lambda: controller.show_frame(CommunicationModule))
        Back_button.grid(row=3, sticky=tk.W, padx=260, pady=180)


class CommunicationModule(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Communication Module", fg="#093d81", font=("Calibri", 13), padx=80,
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


class Total_latency(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text="Total Latency", fg="#093d81", font=("Calibri", 13), padx=80,
                 height=2).grid(row=0)
        self.myText = tk.StringVar()
        tk.Label(self, text="Perception Module Latency").grid(row=1, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="DBW Module Latency").grid(row=2, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=3, padx=80, pady=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=3, pady=5, column=1, sticky=tk.W)
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        b = tk.Button(self, text="Calculate", height=2, bg="#093d81", fg="white",
                      command=lambda: self.calculate_total_latency())
        b.grid(row=6, column=1, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S)
        b1 = tk.Button(self, text="Insert Values", width=17, height=2, bg="#093d81", fg="white",
                       command=lambda: self.insert_value())
        b1.grid(row=6, column=0,padx=80, columnspan=2, rowspan=2, sticky=tk.W)
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=8, column=0, sticky=tk.W,padx=80, pady=80)

    def insert_value(self):
        global analogue_Latency, digital_Latency, DBW_module_latency
        self.e1.insert(0, str(analogue_Latency+digital_Latency))
        self.e2.insert(0, str(DBW_module_latency))

    def calculate_total_latency(self):
        total_latency = float(self.e1.get())+float(self.e2.get())
        self.myText.set(str(total_latency) + " ms")

# Main Program;
if "__main__" == __name__:
    analogue_Latency = 0.0
    digital_Latency = 0.0
    DBW_module_latency = 0.0
    app = App()
    app.mainloop()
