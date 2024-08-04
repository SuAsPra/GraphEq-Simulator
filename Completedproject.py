import tkinter as tk
from tkinter import messagebox
import pickle
import time
import sys
import numpy as np
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt
import math
from sympy import *
from sympy.plotting import plot, plot_implicit, plot_parametric

#after completion put condition that password should be more than eight charecters

f=open("Accounts3.dat", 'wb')
f.close()
check=[]

class App:
    def __init__(self, root):
        global check
        self.root = root
        self.root.title("Login and Signup")
        self.root.geometry("500x500")

        # Variables to store user data
        self.users = {"suri": "p"}
        # Sample user data
        f=open("Accounts3.dat",'rb')
        try:
            while True:
                d=pickle.load(f)
                self.users.update(d)
        except EOFError:
            f.close()

        # Create login page
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(pady=20)

        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, padx=10, pady=10)

        self.login_username_entry = tk.Entry(self.login_frame)
        self.login_username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        self.login_password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

        # Create signup page
        self.signup_frame = tk.Frame(self.root)
        self.signup_frame.pack(pady=20)

        tk.Label(self.signup_frame, text="New Username:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.signup_frame, text="New Password:").grid(row=1, column=0, padx=10, pady=10)

        self.signup_username_entry = tk.Entry(self.signup_frame)
        self.signup_username_entry.grid(row=0, column=1, padx=10, pady=10)
        self.signup_password_entry = tk.Entry(self.signup_frame, show="*")
        self.signup_password_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Button(self.signup_frame, text="Signup", command=self.signup).grid(row=2, column=0, columnspan=2, pady=10)
        Notemessage= " Set a strong password. It must be of minimum eight charecters "
        
        #Creating text
        text_frame = tk.Frame(self.root)
        text_frame.pack(pady=20)
        
        tk.Label(text_frame, text="GRAPH EQUATION SIMULATOR", background="orange", font="100").grid(row=10, column=10, padx=20, pady=20)
        textmessage="'Welcome to graph equation simulator. \n This program allows user to \n input any 2 variable equation and then give output as its graph. \n You have to use decimal instead of fraction."
        tk.Label(text_frame, text= textmessage, background="blue", font="10").grid(row=12, column=10, padx=20, pady=20)
        tk.Label(text_frame, text=Notemessage).grid(row=13, column=10, padx=10, pady=10)
    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login Successful", "Welcome, {}".format(username))
            check=["complete"]
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    def signup(self):
        new_username = self.signup_username_entry.get()
        new_password = self.signup_password_entry.get()

        #in binary file
        if new_username and new_password:
            if new_username not in self.users:
                self.users[new_username] = new_password
                messagebox.showinfo("Signup Successful", "Account created for" + str(new_username))
                self.users.update({new_username:new_password})
                f=open("Accounts3.dat",'ab')
                pickle.dump({new_username:new_password},f)
                f.close()
            else:
                messagebox.showerror("Signup Failed", "Username already exists")
        else:
            messagebox.showerror("Signup Failed", "Please enter both username and password")

def makeline():
    def putline():
        slope=int(slope_entry.get())
        intercept=int(intercept_entry.get())
        print(slope)
        print(intercept)
    #to add graph
        if slope!=0:
            fig, ax = plt.subplots()
            plt.plot([0, (100-intercept)/slope], [intercept, 100], marker='o', color='black',linestyle='-', linewidth=1)
            ax.set_aspect('equal', adjustable='box')
            ax.set_xlim(0, 100)
            ax.set_ylim(0, 100)
            plt.title("Line Plot")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid(True)
            plt.show()
    rootline=tk.Tk()
    rootline.title("Straight Line Equation")
    rootline.geometry("600x300")
    line_frame = tk.Frame(rootline)
    line_frame.pack(pady=20)
    tk.Label(line_frame, text="Lines are in the form y=mx+c. Enter your slope value and y intercept value in the dialog box").grid(row=0, column=0, padx=10, pady=10)  
    line2_frame = tk.Frame(rootline)
    line2_frame.pack(pady=20)
    tk.Label(line2_frame, text=" Y  = ").grid(row=1, column=0, padx=10, pady=10)
    slope_entry = tk.Entry(line2_frame)
    slope_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(line2_frame, text=" X  +").grid(row=1, column=2, padx=10, pady=10)
    intercept_entry = tk.Entry(line2_frame)
    intercept_entry.grid(row=1, column=3, padx=10, pady=10)
    tk.Button(line2_frame, text="Go", command=putline).grid(row=2, column=4, columnspan=2, pady=10)
    rootline.mainloop()
    
    
def makecircle():
    def putcircle():
        h=int(h_entry.get())
        k=int(k_entry.get())
        r=int(r_entry.get())
        if r!=0:
            plt.scatter(h, k, s=r*3200, facecolors='none', edgecolors='black')
            plt.xlim(h-5, k+5)
            plt.ylim(h-5, k+5)
            plt.show()
    rootcircle=tk.Tk()
    rootcircle.title("Circle Equation")
    rootcircle.geometry("800x300")
    circle_frame = tk.Frame(rootcircle)
    circle_frame.pack(pady=20)
    tk.Label(circle_frame, text="Circles are in the form (x-h)^2 + (y-k)^2 = r^2. Enter the respective values in the dialog box").grid(row=0, column=0, padx=10, pady=10)
    circle2_frame = tk.Frame(rootcircle)
    circle2_frame.pack(pady=20)
    tk.Label(circle2_frame, text=" (X-").grid(row=1, column=0, padx=10, pady=10)
    h_entry = tk.Entry(circle2_frame)
    h_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(circle2_frame, text=" )^2 + (Y-").grid(row=1, column=2, padx=10, pady=10)
    k_entry = tk.Entry(circle2_frame)
    k_entry.grid(row=1, column=3, padx=10, pady=10)
    tk.Label(circle2_frame, text=" )^2 = ").grid(row=1, column=4, padx=10, pady=10)
    r_entry = tk.Entry(circle2_frame)
    r_entry.grid(row=1, column=5, padx=10, pady=10)
    tk.Button(circle2_frame, text="Go", command=putcircle).grid(row=2, column=4, columnspan=2, pady=10)
    tk.Label(circle2_frame, text=")^2 ").grid(row=1, column=6, padx=10, pady=10)
    rootcircle.mainloop()
    h=h_entry.get()
    k=k_entry.get()
    r=r_entry.get()
    #graphing
    plt.scatter(h, k, s=r*3200, facecolors='none', edgecolors='black')
    plt.xlim(h-5, k+5)
    plt.ylim(h-5, k+5)
    plt.show()
    
def makeparabola():
    def putparabola():
        a=0
        b=0
        a=int(a_entry.get())
        b=int(b_entry.get())
        #work only if the other unused space is filled zero
    #graphing
        if a != 0 or b!=0:
            if a !=0:
                y = np.linspace(-10, 10, 400)
                x = (y**2)/(4*a)
                plt.plot(x, y)
                plt.title("Graph of Horizontal parabola")
            if b !=0:
                x = np.linspace(-10, 10, 400)
                #dont use this gives zero error
                y = (x**2)/(4*b)
                plt.plot(x, y)
                plt.title("Graph of Vertical Parabola")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.show()
    rootparabola=tk.Tk()
    rootparabola.title("Parabola Equation")
    rootparabola.geometry("800x300")
    parabola_frame = tk.Frame(rootparabola)
    parabola_frame.pack(pady=20)
    tk.Label(parabola_frame, text="Standard Parabolas are in the form Y^2 = 4AX (Horizontal) and X^2 = 4AY. Enter the respective values in the dialog box.").grid(row=0, column=0, padx=10, pady=10)
    parabola2_frame = tk.Frame(rootparabola)
    parabola2_frame.pack(pady=20)
    tk.Label(parabola2_frame, text="horizontal parabola-Enter focus").grid(row=1, column=0, padx=10, pady=10)
    a_entry = tk.Entry(parabola2_frame)
    a_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(parabola2_frame, text="vertical parabola-Enter focus").grid(row=1, column=2, padx=10, pady=10)
    b_entry = tk.Entry(parabola2_frame)
    b_entry.grid(row=1, column=3, padx=10, pady=10)
    tk.Button(parabola2_frame, text="Go", command=putparabola).grid(row=2, column=4, columnspan=2, pady=10)
    
    
def makeellipse():
    from matplotlib.patches import Ellipse
    def putellipse():
        a=int(a_entry.get())
        b=int(b_entry.get())
        #graphing
        fig,ax = plt.subplots()
        ellipse = Ellipse((0,0), a, b, angle=0, fill=False, color='black')
        ax.add_patch(ellipse)
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        plt.title("Ellipse")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.show()
    rootellipse=tk.Tk()
    rootellipse.title("Ellipse Equation")
    rootellipse.geometry("800x300")
    ellipse_frame = tk.Frame(rootellipse)
    ellipse_frame.pack(pady=20)
    tk.Label(ellipse_frame, text="Standard Ellipse are in the form (X/A)^2 + (Y/B)^2 = 1. Enter the respective values in the dialog box").grid(row=0, column=0, padx=10, pady=10)
    ellipse2_frame = tk.Frame(rootellipse)
    ellipse2_frame.pack(pady=20)
    tk.Label(ellipse2_frame, text="Enter width or A value").grid(row=1, column=0, padx=10, pady=10)
    a_entry = tk.Entry(ellipse2_frame)
    a_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(ellipse2_frame, text="Enter ehight or B value").grid(row=1, column=2, padx=10, pady=10)
    b_entry = tk.Entry(ellipse2_frame)
    b_entry.grid(row=1, column=3, padx=10, pady=10)
    tk.Button(ellipse2_frame, text="Go", command=putellipse).grid(row=2, column=4, columnspan=2, pady=10)
    
    
def makehyperbola():
    def puthyperbola():
        a=int(a_entry.get())
        b=int(b_entry.get())
        #graphing
        x, y = symbols('x y')
        plot_implicit(Eq(x**2/a - y**2/b, 1),(x,-10,10))
        
    roothyperbola=tk.Tk()
    roothyperbola.title("Hyperbola Equation")
    roothyperbola.geometry("800x300")
    hyperbola_frame = tk.Frame(roothyperbola)
    hyperbola_frame.pack(pady=20)
    tk.Label(hyperbola_frame, text="Standard hyperbolas are in the form (X/A)^2 - (Y/B)^2 = 1. Enter the respective values in the dialog box").grid(row=0, column=0, padx=10, pady=10)
    hyperbola2_frame = tk.Frame(roothyperbola)
    hyperbola2_frame.pack(pady=20)
    tk.Label(hyperbola2_frame, text="Enter A value").grid(row=1, column=0, padx=10, pady=10)
    a_entry = tk.Entry(hyperbola2_frame)
    a_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(hyperbola2_frame, text="Enter B value").grid(row=1, column=2, padx=10, pady=10)
    b_entry = tk.Entry(hyperbola2_frame)
    b_entry.grid(row=1, column=3, padx=10, pady=10)
    tk.Button(hyperbola2_frame, text="Go", command=puthyperbola).grid(row=2, column=4, columnspan=2, pady=10)
    
    
def makegeneral():
    def putgeneral():
        a=int(a_entry.get())
        b=int(b_entry.get())
        c=int(c_entry.get())
        #
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c
        plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
        
        # Add labels and title
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Quadratic Equation Graph')
        
        # Add a legend
        plt.legend()
        
        # Show the plot
        plt.grid(True)
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.show()
        
    rootgeneral=tk.Tk()
    rootgeneral.title("General Quadratic Equation")
    rootgeneral.geometry("800x300")
    general_frame = tk.Frame(rootgeneral)
    general_frame.pack(pady=20)
    tk.Label(general_frame, text="Quadratic equations are in the form AX^2 + BX + C. Enter the respective values in the dialog box").grid(row=0, column=0, padx=10, pady=10)
    general2_frame = tk.Frame(rootgeneral)
    general2_frame.pack(pady=20)
    tk.Label(general2_frame, text="Enter A value").grid(row=1, column=0, padx=10, pady=10)
    a_entry = tk.Entry(general2_frame)
    a_entry.grid(row=1, column=1, padx=10, pady=10)
    tk.Label(general2_frame, text="Enter B value").grid(row=1, column=2, padx=10, pady=10)
    b_entry = tk.Entry(general2_frame)
    b_entry.grid(row=1, column=3, padx=10, pady=10)
    tk.Label(general2_frame, text="Enter C value").grid(row=1, column=4, padx=10, pady=10)
    c_entry = tk.Entry(general2_frame)
    c_entry.grid(row=1, column=5, padx=10, pady=10)
    tk.Button(general2_frame, text="Go", command=putgeneral).grid(row=2, column=4, columnspan=2, pady=10)
    
    

def exitapp():
    print("EXITING")
    messagebox.showinfo("You will be exited in 3 seconds","You will be exited in 3 seconds")
    print("You will be exited in 3 seconds")
    time.sleep(3)
    root2.destroy()
    sys.exit()





#body

name="main"

if name == "main":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

#start of interface
##
check = ["complete"]
if check == ["complete"]:
    root2 = tk.Tk()
    root2.title("GRAPH EQUATION SIMULATOR")
    root2.geometry("1200x300")
    main_frame = tk.Frame(root2)
    main_frame.pack(pady=20)
    tk.Label(main_frame, text="GRAPH EQUATION SIMULATOR", bg="orange", font='20').grid(row=0, column=0, padx=10, pady=10)
    tk.Label(main_frame, text="Choose any of the following buttons to proceed and give your equation").grid(row=1, column=0, padx=10, pady=10)
    tk.Button(main_frame, text="Straight Line", command=makeline).grid(row=3, column=1, padx=10, pady=10)
    tk.Button(main_frame, text="Circle", command=makecircle).grid(row=3, column=2, padx=10, pady=10)
    tk.Button(main_frame, text="Parabola", command=makeparabola).grid(row=3, column=3, padx=10, pady=10)
    tk.Button(main_frame, text="Ellipse", command=makeellipse).grid(row=3, column=4, padx=10, pady=10)
    tk.Button(main_frame, text="Hyperbola", command=makehyperbola).grid(row=3, column=5, padx=10, pady=10)
    tk.Button(main_frame, text="General Quadratic", command=makegeneral).grid(row=3, column=6, padx=10, pady=10)
    tk.Button(main_frame, text="Exit Application", command=exitapp).grid(row=3, column=7, padx=10, pady=10)
    root2.mainloop()
    
    


