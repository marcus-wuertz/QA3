from tkinter import *
import tkinter as tk
from tkinter import ttk
class Application(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.title('Main Page')
        self.main_page()
        
        
    def main_page(self):
        self.clear_screen() 
        
        self.l1 = tk.Label(self, text="Welcome to the Quiz Bowl!")
        self.l1.pack()

        # Create a list of categories
        categories = ["Business Strategy", "Business Applications", "Programming Logic","Analytics Capstone","Business Law"]

        # Create a Combobox to select the category
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(self, textvariable=self.category_var, values=categories)
        self.category_combo.pack()

        # Button to proceed to the quiz based on selected category
        self.b1 = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        self.b1.pack()

        