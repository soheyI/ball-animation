# main.py
import tkinter as tk
from controller import Controller

def main():
    root = tk.Tk()
    root.title("Ball Animation")
    Controller(root) 
    root.geometry("540x740")


    # fixed size window
    root.resizable(False, False)  

    root.mainloop()


main()