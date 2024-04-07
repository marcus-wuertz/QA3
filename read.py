import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowlGUI.db')
cursor = conn.cursor()

# Fetch and display column names and data from each table
tables = ['BusinessStrategy', 'BusinessApplications', 'ProgrammingLogic', 'AnalyticsCapstone', 'BusinessLaw']
for table in tables:
    col_names=['id', 'question','option1','option2','option3','option4','correct_answer']
    print('column names:')
    print(col_names)
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    print(f"Contents of {table} table:")
    for row in rows:
        print(row)
    print()