import tkinter as tk
from tkinter import ttk
import sqlite3

class Application(tk.Tk):
    def __init__(self, *args):
        super().__init__(*args)
        self.title('Main Page')
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

        # Variable to store selected answer
        self.selected_answer = None

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

    def page_one(self):
        self.clear_screen()
        selected_category = self.category_var.get()
        lbl1 = ttk.Label(self, text=f'{selected_category} quiz')
        lbl1.pack()

        # Get the table name based on the selected category
        table_name = self.category_table_mapping.get(selected_category)

        if table_name:
            # Query the database to fetch questions for the selected category
            questions = self.fetch_questions(table_name)
            for question_data in questions:
                # Display the question to the user
                question_label = ttk.Label(self, text=question_data[1])  # Display question
                question_label.pack()

                # Create a Combobox for the user to select their answer
                self.answer_var = tk.StringVar()  # Define as self.answer_var
                answer_combo = ttk.Combobox(self, textvariable=self.answer_var, values=question_data[2:6], width=50)  # Adjust width as needed
                answer_combo.pack()

                # Button to submit answer
                submit_button = tk.Button(self, text="Submit", command=lambda q=question_data: self.check_answer(q[6]))
                submit_button.pack()
        else:
            ttk.Label(self, text="Invalid category").pack()

    def fetch_questions(self, table_name):
        # Execute a query to fetch questions from the specified table
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        questions = self.cursor.fetchall()
        return questions

    def check_answer(self, correct_answer):
        # Ensure that correct_answer and selected_answer are both strings
        correct_answer = str(correct_answer)

        # Retrieve the selected answer from self.answer_var
        selected_answer = self.answer_var.get()

        print("Correct answer:", correct_answer.strip().lower())  # Debugging message
        print("Selected answer:", selected_answer.strip().lower())  # Debugging message

        if correct_answer.strip().lower() == selected_answer.strip().lower():  # Case-insensitive comparison
            # Display 'Correct!' in green
            feedback_label = tk.Label(self, text="Correct!", fg="green")
            feedback_label.pack()
            self.score += 1  # Increment score
        else:
            # Display 'Incorrect!' in red
            feedback_label = tk.Label(self, text="Incorrect!", fg="red")
            feedback_label.pack()


    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def __del__(self):
        # Close the database connection when the application is destroyed
        self.connection.close()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
