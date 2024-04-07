import tkinter as tk
from tkinter import ttk
import sqlite3

class Application(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.title('Quiz Bowl')
        self.main_page()

        # Connect to the database
        self.connection = sqlite3.connect('quiz_bowlGUI.db')
        self.cursor = self.connection.cursor()

        # Mapping between category names and table names
        self.category_table_mapping = {
            "Business Strategy": "BusinessStrategy",
            "Business Applications": "BusinessApplications",
            "Programming Logic": "ProgrammingLogic",
            "Analytics Capstone": "AnalyticsCapstone",
            "Business Law": "BusinessLaw"
        }

        # Variable to track user's score
        self.score = 0
        self.selected_category = None

    def main_page(self):
        self.clear_screen() 
        
        self.l1 = tk.Label(self, text="Welcome to the Quiz Bowl! Please select a category")
        self.l1.pack()

        # Create a list of categories
        categories = ["Business Strategy", "Business Applications", "Programming Logic","Analytics Capstone","Business Law"]

        # Create a Combobox to select the category
        self.category_var = tk.StringVar()
        self.category_combo = ttk.Combobox(self, textvariable=self.category_var, values=categories)
        self.category_combo.pack()

        # Button to proceed to the quiz based on selected category
        self.b1 = tk.Button(self, text="Start Quiz", command=self.page_one)
        self.b1.pack()