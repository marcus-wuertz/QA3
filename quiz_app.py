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

    def page_one(self):
        self.clear_screen()
        selected_category = self.category_var.get()
        lbl1 = ttk.Label(self, text=f'{selected_category} quiz')
        lbl1.pack()

        # Store selected category for later use
        self.selected_category = selected_category

        # Get the table name based on the selected category
        table_name = self.category_table_mapping.get(selected_category)

        if table_name:
            # Query the database to fetch questions for the selected category
            questions = self.fetch_questions(table_name)
            self.answer_vars = []  # List to store answer variables
            
            # Create a label for feedback
            self.feedback_label = tk.Label(self)
            self.feedback_label.pack()
            
            for question_data in questions:
                # Display the question to the user
                question_label = ttk.Label(self, text=question_data[1])  # Display question
                question_label.pack()

                # Create a Combobox for the user to select their answer
                answer_var = tk.StringVar()  # Define as local variable
                answer_combo = ttk.Combobox(self, textvariable=answer_var, values=question_data[2:6], width=50)  # Adjust width as needed
                answer_combo.pack()

                # Append answer_var to the list
                self.answer_vars.append(answer_var)

                # Button to submit answer
                submit_button = tk.Button(self, text="Submit", command=lambda qa=question_data, av=answer_var: self.check_answer(qa[6], av))
                submit_button.pack()

            # Button to see score
            score_button = tk.Button(self, text="See Score", command=self.page_two)
            score_button.pack()

        else:
            ttk.Label(self, text="Invalid category").pack()

    def fetch_questions(self, table_name):
        # Execute a query to fetch questions from the specified table
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        questions = self.cursor.fetchall()
        return questions
    
    def check_answer(self, correct_answer, answer_var):
        # Retrieve the selected answer from the corresponding answer_var
        selected_answer = answer_var.get()
 
        # Ensure that correct_answer and selected_answer are both strings
        correct_answer = str(correct_answer)

        print("Correct answer:", correct_answer.strip().lower())  # Debugging message
        print("Selected answer:", selected_answer.strip().lower())  # Debugging message

        if correct_answer.strip().lower() == selected_answer.strip().lower():  # Case-insensitive comparison
            # Display 'Correct!' in green
            self.feedback_label.config(text="Correct!", fg="green")
            self.score += 1  # Increment score
        else:
            # Display 'Incorrect!' in red
            self.feedback_label.config(text="Incorrect!", fg="red")

    def page_two(self):
        self.clear_screen()
        if self.selected_category:
            score_label = ttk.Label(self, text=f"Your score on the {self.selected_category} quiz:")
            score_label.pack()

            score_value_label = ttk.Label(self, text=f"{self.score}/{len(self.answer_vars)}")
            score_value_label.pack()

            farewell_lbl=ttk.Label(self, text="Thanks, for playing! I'f you'd like another category, press Home")
            farewell_lbl.pack()

            # Button to go back to the home page
            home_button = tk.Button(self, text="Home", command=self.main_page)
            home_button.pack()
        else:
            ttk.Label(self, text="No quiz has been taken yet.").pack()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def __del__(self):
        # Close the database connection when the application is destroyed
        self.connection.close()

if __name__ == "__main__":
    app = Application()
    app.mainloop()