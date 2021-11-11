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
        self.geometry('700x600')
        self.resizable(0, 0)

        # Creating a container
        container = tk.Frame(self, bg="white")
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        page_layout = (register_user_screen, startPage, Bullet, DBW_module, DBW_module_info,
                       perception_module, perception_module_info, Total_latency, About)
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
        img.grid(row=2, pady=90)

        # button for "Main Screen" Frame
        tk.Button(self, text="Get In", height="2", width="30", bg="#093d81", fg="white",
                  command=lambda: controller.show_frame(startPage)).grid( row=10, sticky=tk.S)

        # button for "About" Frame
        tk.Button(self, text="About", height="2", width="30", bg="#093d81", fg="white",
                  command=lambda: controller.show_frame(About)).grid(
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
        button1.place(x=30, y=100)

        # Button for Class perception_module
        button2 = tk.Button(self, text="Perception Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(perception_module))
        button2.pack()
        button2.place(x=260, y=100)

        # Button for DBW_module class
        button3 = tk.Button(self, text="DBW Module", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(DBW_module))
        button3.pack()
        button3.place(x=485, y=100)

        # Button for Over all Latency class
        button5 = tk.Button(self, text="Total Latency", width=25, height=2, bg="#093d81", fg="white",
                            command=lambda: controller.show_frame(Total_latency))
        button5.pack()
        button5.place(x=30, y=200)

        # Button for Go Back button
        button6 = tk.Button(self, text="Go Back!!", width=25, height=2, bg="red", fg="white",
                            command=lambda: controller.show_frame(register_user_screen))
        button6.pack()
        button6.place(x=485, y=200)

class About(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Loading Perception Module in the tkinter frame
        self.config(bg="#F8F4F4")
        tk.Label(self, text="ABOUT", bg="#093d81", fg="white", font=("Calibri", 13),
                 padx=330, height=2).grid(row=0, sticky=tk.E)
        load = Image.open("img/sathyabama.png")

        # Rendering loaded image in the frame
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render,bg="#F8F4F4")
        img.image = render
        img.grid(row=2,padx=145, sticky=tk.W)

        load = Image.open("img/team.png")

        # Rendering loaded image in the frame
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self, image=render,bg="#F8F4F4")
        img.image = render
        img.grid(row=3, sticky=tk.E)

        # Button to open frame startPage
        Home_button = tk.Button(self, text="Go Back", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(register_user_screen))
        Home_button.grid(row=4, column=0, pady=30, padx=50, sticky=tk.E)

class Bullet(tk.Frame):

    # __init__ function for Bullet Latency
    def __init__(self, parent, controller):

        # __init__ function for Tk Class
        tk.Frame.__init__(self, parent)

        # String for storing Final Latency
        self.myText = tk.StringVar()

        # Label For Heading
        tk.Label(self, text="Time Taken By Bullet To Hit the Target", bg="#093d81", fg="white", font=("Calibri", 13),
                 padx=230, height=2).grid(row=0, sticky=tk.E)
        # Label Blank
        tk.Label(self, text=" ", bg="#093d81", fg="white", font=("Calibri", 13), height=2).grid(row=1, sticky=tk.E)
        # Label Height
        tk.Label(self, text="Height (m)").grid(row=2, pady=5, padx=20, sticky=tk.W)
        # Label Velocity of Bullet
        tk.Label(self, text="Velocity of Bullet (m/s)").grid(row=3, pady=5, padx=20, sticky=tk.W)
        # Label Angle of elevation
        tk.Label(self, text="Angle of elevation (degree)").grid(row=4, pady=5, padx=20, sticky=tk.W)
        # Label Distance
        tk.Label(self, text="Distance (m)").grid(row=5, pady=5, padx=20, sticky=tk.W)
        # Label Result
        tk.Label(self, text="Result:").grid(row=6, padx=20, pady=5, sticky=tk.W)
        # Label to print Value
        tk.Label(self, text="", textvariable=self.myText).grid(row=6, padx=300, column=0, pady=5, sticky=tk.W)

        # Entry for storing value for Label Height
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=0)

        # Entry for storing value for Label Velocity of Bullet
        self.e2 = tk.Entry(self)
        self.e2.grid(row=3, column=0)

        # Entry for storing value for Label Angle of Elevation
        self.e3 = tk.Entry(self)
        self.e3.grid(row=4, column=0)

        # Entry for storing value for Label Distance
        self.e4 = tk.Entry(self)
        self.e4.grid(row=5, column=0)

        # Default Value for Height
        self.e1.insert(0, "2")
        # Default Value for Velocity
        self.e2.insert(0, "400")
        # Default Value for Angle of Elevation
        self.e3.insert(0, "30")
        # Default Value for Distance
        self.e4.insert(0, "500")

        # Calculate button to call function self.calculate()
        b = tk.Button(self, text="Calculate", height=2, width=17, bg="#093d81", fg="white",
                      command=lambda: self.calculate())
        b.grid(row=8, column=0)

        # Button to open frame startPage
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=10, column=0, pady=30, padx=50, sticky=tk.E)

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
        tk.Label(self, text="Drive-by-wire Module (DBW)", bg="#093d81", fg="white", font=("Calibri", 13), padx=270,
                 height=2).grid(row=0, sticky=tk.E)

        # Base Station to UGV Latency
        tk.Label(self, text="Operator command from console to UGV", fg="#093d81", font=("Calibri", 13), pady=5,
                 height=2).grid(row=1, sticky=tk.W)

        # Initializing StringVar self.myText
        self.myText = tk.StringVar()

        # Label Generation of Operator Command
        tk.Label(self, text="Generation of Operator Command (ms)").grid(row=2, pady=5, sticky=tk.W)
        # Label Ethernet Switch Latency
        tk.Label(self, text="Ethernet Switch Latency (ms)").grid(row=3, pady=5, sticky=tk.W)
        # Label Radio (Tx to Rx)
        tk.Label(self, text="Radio (Tx to Rx) (ms)").grid(row=4, pady=5, sticky=tk.W)
        # Label Command Execution
        tk.Label(self, text="Command Execution (ms)").grid(row=5, pady=5, sticky=tk.W)
        # Label result
        tk.Label(self, text="Result:").grid(row=6, pady=5, sticky=tk.W)
        # Label To store Result string
        tk.Label(self, text="", textvariable=self.myText).grid(row=6, pady=5, padx=305, column=0, sticky=tk.W)

        # Entry for storing value for Label Generation of Operator Command
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=0, padx=100)

        # Entry for storing value for Label Ethernet Switch Latency
        self.e2 = tk.Entry(self)
        self.e2.grid(row=3, column=0, padx=100)

        # Entry for storing value for Label Radio (Tx to Rx)
        self.e3 = tk.Entry(self)
        self.e3.grid(row=4, column=0, padx=100)

        # Entry for storing value for Label Execution
        self.e4 = tk.Entry(self)
        self.e4.grid(row=5, column=0, padx=100)

        # Default value for all Entries
        self.e1.insert(0, "35")
        self.e2.insert(0, "0.0048")
        self.e3.insert(0, "20")
        self.e4.insert(0, "140")

        # Calculate button to call function self.base_station_to_ugv_latency()
        b = tk.Button(self, text="Calculate", height=2, width=17, bg="#093d81", fg="white",
                      command=lambda: self.base_station_to_ugv_latency())
        b.grid(row=8, column=0)

        # Button to open frame startPage
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=10, column=0, pady=80, padx=50, sticky=tk.E)

        # Button to open frame DBW_module_info
        More_Info = tk.Button(self, text="More Info", bg="#1e81b0", fg="white", width=20, height=2,
                              command=lambda: controller.show_frame(DBW_module_info))
        More_Info.grid(row=10, column=0, pady=80, padx=210, sticky=tk.E)

    def base_station_to_ugv_latency(self):
        total_latency = float(self.e1.get()) + float(self.e2.get()) + float(self.e3.get()) + float(self.e4.get())
        self.myText.set(str(round(total_latency, 6)) + " ms")
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
        DBW_module_back_button.grid(row=3, sticky=tk.E, padx=35)
        # Back button for "Perception Module" Frame
        Back_button = tk.Button(self, text="Back", bg="#154c79", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(DBW_module))
        Back_button.grid(row=3, sticky=tk.E, padx=200, pady=40)


# Perception Module Frame Page
class perception_module(tk.Frame):

    # __init__ function for perception_module Class
    def __init__(self, parent, controller):
        # __init__ function for class TK
        tk.Frame.__init__(self, parent)

        # Header Label For Perception Module
        tk.Label(self, text="Perception Module", bg="#093d81", fg="white", font=("Calibri", 13), padx=285,
                 height=2).grid(row=0, sticky=tk.W)

        # Header Label For Digital Camera
        tk.Label(self, text="Digital Camera", fg="#093d81", font=("Calibri", 13), pady=5,
                 height=2).grid(row=1, sticky=tk.W)

        # String to Store Calculated value for Digital Camera Latency
        self.myText = tk.StringVar()
        # Label Frame Width
        tk.Label(self, text="Frame Width (pixels)").grid(row=2, pady=5, sticky=tk.W)
        # Label Frame Height
        tk.Label(self, text="Frame Height (pixels)").grid(row=3, pady=5, sticky=tk.W)
        # Label Bits/Pixel
        tk.Label(self, text="Bits/Pixel").grid(row=4, pady=5, sticky=tk.W)
        # Label Compression %
        tk.Label(self, text="Compression %").grid(row=5, pady=5, sticky=tk.W)
        # Label FPS
        tk.Label(self, text="FPS").grid(row=6, pady=5, sticky=tk.W)
        # Label Communication Latency
        tk.Label(self, text="Communication Latency (ms)").grid(row=7, pady=5, sticky=tk.W)
        # Label For Radio Latency
        tk.Label(self, text="Radio Latency").grid(row=8, pady=5, sticky=tk.W)
        # Label Display
        tk.Label(self, text="Display").grid(row=9, pady=5, sticky=tk.W)
        # Label Result
        tk.Label(self, text="Result:").grid(row=10, pady=5, padx=2, sticky=tk.W)
        # Label to Store Calculated Value
        tk.Label(self, text="", textvariable=self.myText).grid(row=10, pady=5, column=0, padx=180, sticky=tk.W)

        # Entry for storing value for Label Frame Width
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label Frame Height
        self.e2 = tk.Entry(self)
        self.e2.grid(row=3, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label Bits/Pixel
        self.e3 = tk.Entry(self)
        self.e3.grid(row=4, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label Compression %
        self.e4 = tk.Entry(self)
        self.e4.grid(row=5, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label FPS
        self.e5 = tk.Entry(self)
        self.e5.grid(row=6, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label Communication Latency
        self.e6 = tk.Entry(self)
        self.e6.grid(row=7, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label Radio Latency
        self.e7 = tk.Entry(self)
        self.e7.grid(row=8, column=0, padx=180, sticky=tk.W)
        # Entry for storing value for Label Display
        self.e8 = tk.Entry(self)
        self.e8.grid(row=9, column=0, padx=180, sticky=tk.W)

        # Default Value for all Entries
        self.e1.insert(0, '1280')
        self.e2.insert(0, '960')
        self.e3.insert(0, '12')
        self.e4.insert(0, '0.6')
        self.e5.insert(0, '20')
        self.e6.insert(0, '10')
        self.e7.insert(0, '10')
        self.e8.insert(0, '50')

        # Button to call function digital_latency()
        b = tk.Button(self, text="Calculate", height=2, width=17, bg="#093d81", fg="white",
                      command=lambda: self.digital_latency())
        b.grid(row=12, column=0, padx=180, sticky=tk.W)

        # Initializing StringVar
        self.myText2 = tk.StringVar()
        n = tk.StringVar()
        n2 = tk.StringVar()

        # Header Label For Analogue Camera
        tk.Label(self, text="Analogue Camera", fg="#093d81", font=("Calibri", 13), pady=5,
                 height=2).grid(row=1, padx=360, sticky=tk.W)
        # Label Select Camera Type
        tk.Label(self, text="Select Camera Type").grid(row=2, padx=360, pady=5, sticky=tk.W)
        # Label Frame Width
        tk.Label(self, text="Frame Width").grid(row=3, padx=360, pady=5, sticky=tk.W)
        # Label Frame Height
        tk.Label(self, text="Frame Height").grid(row=4, padx=360, pady=5, sticky=tk.W)
        # Label FPS
        tk.Label(self, text="FPS").grid(row=5, padx=360, pady=5, sticky=tk.W)
        # Label Select Y:Cr:Cb
        tk.Label(self, text="Select Y:Cr:Cb").grid(row=6, padx=360, pady=5, sticky=tk.W)
        # Label Acquisition
        tk.Label(self, text="Video Acquisition").grid(row=7, padx=360, pady=5, sticky=tk.W)
        # Label Video Compression
        tk.Label(self, text="Video Compression").grid(row=8, padx=360, pady=5, sticky=tk.W)
        # Label Radio Latency
        tk.Label(self, text="Radio Latency").grid(row=9, padx=360, pady=5, sticky=tk.W)
        # Label Display Latency
        tk.Label(self, text="Display Latency").grid(row=10, padx=360, pady=5, sticky=tk.W)
        # Label Result
        tk.Label(self, text="Result:").grid(row=11, padx=360, pady=5, sticky=tk.W)
        # Label to store StringVar() self.myText2
        tk.Label(self, text="", textvariable=self.myText2).grid(row=11, padx=500, pady=5, sticky=tk.W)

        # Combobox options for Label Select Camera option
        optionSelect = ttk.Combobox(self, width=17, textvariable=n)
        optionSelect['values'] = ('PAL', 'NTSC')
        optionSelect.grid(row=2, column=0, padx=500, sticky=tk.W)
        optionSelect.current(0)

        # Entry for Label Frame Width
        self.e9 = tk.Entry(self)
        self.e9.grid(row=3, column=0, padx=500, sticky=tk.W)

        # Entry for Label Frame Height
        self.e10 = tk.Entry(self)
        self.e10.grid(row=4, column=0, padx=500, sticky=tk.W)

        # Entry for Label FPS
        self.e11 = tk.Entry(self)
        self.e11.grid(row=5, column=0, padx=500, sticky=tk.W)

        # Combobox options for Label Y:Cr:Cb
        optionSelect2 = ttk.Combobox(self, width=17, textvariable=n2)
        optionSelect2['values'] = ('4:4:4', '4:4:2', '4:2:2')
        optionSelect2.grid(row=6, column=0, padx=500, sticky=tk.W)
        optionSelect2.current(0)

        # Entry For Label Video Acquisition
        self.e12 = tk.Entry(self)
        self.e12.grid(row=7, column=0, padx=500, sticky=tk.W)

        # Entry For Label Video Compression
        self.e13 = tk.Entry(self)
        self.e13.grid(row=8, column=0, padx=500, sticky=tk.W)

        # Entry For Label Radio Latency
        self.e14 = tk.Entry(self)
        self.e14.grid(row=9, column=0, padx=500, sticky=tk.W)

        # Entry for Label Display Latency
        self.e15 = tk.Entry(self)
        self.e15.grid(row=10, column=0, padx=500, sticky=tk.W)

        # Inserting default values for all Entries
        self.e12.insert(0, '50')
        self.e13.insert(0, '55')
        self.e14.insert(0, '10')
        self.e15.insert(0, '50')

        # Initializing self.m1,self.m2,self.m3
        self.m1 = 0.0
        self.m2 = 0.0
        self.m3 = 0.0

        # Button to select Label Select Camera Type
        button_options = tk.Button(self, text="Select", bg="#093d81", fg="white",
                                   command=lambda: self.insert_value2(optionSelect))
        button_options.grid(row=2, column=0, padx=635, sticky=tk.W)

        # Button to select Label Select Y:Cr:Cb
        button_options2 = tk.Button(self, text="Select", bg="#093d81", fg="white",
                                    command=lambda: self.insert_value(optionSelect2))
        button_options2.grid(row=6, column=0, padx=635, sticky=tk.W)

        # Button to Call Function self.analogue_latency()
        b = tk.Button(self, text="Calculate", height=2, width=16, bg="#093d81", fg="white",
                      command=lambda: self.analogue_latency())
        b.grid(row=12, column=0, padx=500, sticky=tk.W)

        # Button to show Frame startPage
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=15, column=0, pady=30, padx=520, sticky=tk.W)

        # Button to show Frame perception_module_info
        More_Info = tk.Button(self, text="More Info", bg="#1e81b0", fg="white", width=20, height=2,
                              command=lambda: controller.show_frame(perception_module_info))
        More_Info.grid(row=15, column=0, pady=30, padx=360, sticky=tk.W)

    # Function insert_Value2
    def insert_value2(self, optionSelect):
        if optionSelect.get() == "PAL":
            self.e9.delete(0, 'end')
            self.e10.delete(0, 'end')
            self.e11.delete(0, 'end')
            self.e9.insert(0, "720")
            self.e10.insert(0, "576")
            self.e11.insert(0, "25")
        else:
            self.e9.delete(0, 'end')
            self.e10.delete(0, 'end')
            self.e11.delete(0, 'end')
            self.e9.insert(0, "720")
            self.e10.insert(0, "480")
            self.e11.insert(0, "30")

    # Function Insert_value
    def insert_value(self, optionSelect2):
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

    # Function digital_latency
    def digital_latency(self):
        digital_l = (self.calculate_data_rate_digital() * 1000 * 2) + float(self.e6.get()) + float(
            self.e7.get()) + float(self.e8.get())
        self.myText.set(str(round(digital_l, 4)) + ' ms')
        global digital_Latency
        digital_Latency = digital_l

    # Function calculate_data_rate_digital()
    def calculate_data_rate_digital(self):
        data_r = (float(self.e1.get()) * float(self.e2.get()) * float(self.e3.get()) * float(self.e4.get())) / 100000000
        return data_r

    # Function calculate_y()
    def calculate_y(self):
        latency_y = ((float(self.e9.get()) * float(self.e10.get()) * 8) / (4 / self.m1)) + (
                (float(self.e9.get()) * float(self.e10.get()) * 8) / (4 / self.m2)) + (
                            (float(self.e9.get()) * float(self.e10.get()) * 8) / (4 / self.m3))
        final_y = round(((latency_y / 1000000) * (1 / 100) * 1000), 4)
        return final_y

    # Function analogue_latency()
    def analogue_latency(self):
        analogue_l = (2 * (self.calculate_y() * 0.6)) + float(self.e12.get()) + float(self.e13.get()) + float(
            self.e14.get()) + float(self.e15.get())
        self.myText2.set(str(round(analogue_l, 4)) + " ms")
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
        Home_button.grid(row=3, sticky=tk.E, padx=40, pady=40)

        # Back button for "Perception Module" Frame
        Back_button = tk.Button(self, text="Back", bg="#154c79", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(perception_module))
        Back_button.grid(row=3, sticky=tk.E, padx=200, pady=40)


class Total_latency(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # String for storing Final Latency
        self.myText = tk.StringVar()

        # Label Total Latency
        tk.Label(self, text="Total Latency", bg="#093d81", fg="white", font=("Calibri", 13),
                 padx=320, height=2).grid(row=0, sticky=tk.E)
        tk.Label(self, text=" ", bg="#093d81", fg="white", font=("Calibri", 13), height=2).grid(row=1, sticky=tk.E)
        # Label Perception Module Latency
        tk.Label(self, text="Perception Module Latency (ms)").grid(row=2, pady=5, padx=20, sticky=tk.W)
        # Label DBW Module Latency
        tk.Label(self, text="DBW Module Latency (ms)").grid(row=3, pady=5, padx=20, sticky=tk.W)
        # Label Total latency
        tk.Label(self, text="Total Latency (ms)").grid(row=4, padx=20, pady=5, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=4, padx=305, column=0, pady=5, sticky=tk.W)

        # Entry for storing value for Label Perception Module Latency
        self.e1 = tk.Entry(self)
        self.e1.grid(row=2, column=0)

        # Entry for storing value for Label DBW Module Latency
        self.e2 = tk.Entry(self)
        self.e2.grid(row=3, column=0)

        # Button to call function self.insert_value()
        b1 = tk.Button(self, text="Insert Values", width=17, height=2, bg="#093d81", fg="white",
                       command=lambda: self.insert_value())
        b1.grid(row=6, padx=130, sticky=tk.W)

        # Button to call function self.calculate_total_latency()
        b2 = tk.Button(self, text="Calculate", width=17, height=2, bg="#093d81", fg="white",
                       command=lambda: self.calculate_total_latency())
        b2.grid(row=6, column=0, padx=300, sticky=tk.E)

        # Button to show Frame startPage
        Home_button = tk.Button(self, text="Home", bg="#093d81", fg="white", width=20, height=2,
                                command=lambda: controller.show_frame(startPage))
        Home_button.grid(row=15, column=0, pady=30, padx=50, sticky=tk.E)

    # Function insert_value()
    def insert_value(self):
        global analogue_Latency, digital_Latency, DBW_module_latency
        self.e1.insert(0, str(analogue_Latency + digital_Latency))
        self.e2.insert(0, str(DBW_module_latency))

    # Function calculate_total_latency
    def calculate_total_latency(self):
        total_latency = float(self.e1.get()) + float(self.e2.get())
        self.myText.set(str(total_latency) + " ms")

# Main Program;
if "__main__" == __name__:
    analogue_Latency = 0.0
    digital_Latency = 0.0
    DBW_module_latency = 0.0
    app = App()
    app.mainloop()
