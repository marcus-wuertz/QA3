import sqlite3

# Connect to the database
conn = sqlite3.connect('quiz_bowlGUI.db')
cursor = conn.cursor()

# create a list of dictionaries with the questions and answers for Business Strategy
questions = [
    {
        "id": 1,
        "question": "Porter's Five Forces framework assesses _____?",
        "option1": "Industry",
        "option2": "Organization",
        "option3": "Market",
        "option4": "Country",
        "correct_answer": "Industry"
    },
    {
        "id": 2,
        "question": "What does SWOT analysis stand for?",
        "option1": "Strengths, Weaknesses, Opportunities, Threats",
        "option2": "Strengths, Weaknesses, Opportunities, Trends",
        "option3": "Strategies, Weaknesses, Opportunities, Threats",
        "option4": "Strengths, Warnings, Opportunities, Threats",
        "correct_answer": "Strengths, Weaknesses, Opportunities, Threats"
    },
    {
        "id": 3,
        "question": "Successful business strategy characteristics include being _____?",
        "option1": "Clear, Focused",
        "option2": "Detailed, Long",
        "option3": "Ambiguous, General",
        "option4": "Uncertain, Vague",
        "correct_answer": "Clear, Focused"
    },
    {
        "id": 4,
        "question": "Differentiation strategy focuses on offering _____ products or services.",
        "option1": "Unique",
        "option2": "High-cost",
        "option3": "Similar",
        "option4": "Expensive",
        "correct_answer": "Unique"
    },
    {
        "id": 5,
        "question": "Competitive advantage contributes to business _____?",
        "option1": "Success",
        "option2": "Failure",
        "option3": "Mediocrity",
        "option4": "Stagnation",
        "correct_answer": "Success"
    },
    {
        "id": 6,
        "question": "The role of strategic planning involves _____?",
        "option1": "Goal setting",
        "option2": "Analysis, Planning",
        "option3": "Execution",
        "option4": "All the above",
        "correct_answer": "All the above"
    },
    {
        "id": 7,
        "question": "Main components of a strategic management process include _____?",
        "option1": "Environmental scanning, Formulation, Implementation",
        "option2": "Strategy, Tactics, Operations",
        "option3": "HR, Finance, Marketing",
        "option4": "None of the above",
        "correct_answer": "Environmental scanning, Formulation, Implementation"
    },
    {
        "id": 8,
        "question": "Blue ocean strategy aims for uncontested _____?",
        "option1": "Market",
        "option2": "Competitive edge",
        "option3": "Innovation",
        "option4": "Industry",
        "correct_answer": "Market"
    },
    {
        "id": 9,
        "question": "Environmental scanning helps identify _____ and threats?",
        "option1": "Opportunities",
        "option2": "Competitors",
        "option3": "Risks",
        "option4": "None of the above",
        "correct_answer": "Opportunities"
    },
    {
        "id": 10,
        "question": "Challenges of implementing a new business strategy include _____?",
        "option1": "Resistance to change",
        "option2": "Resource constraints",
        "option3": "Organizational inertia",
        "option4": "All the above",
        "correct_answer": "All the above"
    }
]
# Insert questions into the BusinessStrategy table
# for question in questions:
#    pass
#    cursor.execute('''INSERT INTO BusinessStrategy (id, question, option1, option2, option3, option4, correct_answer)
#                      VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                         question['option2'], question['option3'], question['option4'],
#                                                         question['correct_answer']))
#    conn.commit()


# List of questions for Business Applications Development course
business_app_questions = [
    {
        "id": 1,
        "question": "What is the purpose of using generative AI in software development?",
        "option1": "To automate testing processes",
        "option2": "To generate code automatically",
        "option3": "To design user interfaces",
        "option4": "To analyze user behavior",
        "correct_answer": "To generate code automatically"
    },
    {
        "id": 2,
        "question": "Which Python control structure is typically used to iterate over a sequence of elements?",
        "option1": "if-else statement",
        "option2": "for loop",
        "option3": "while loop",
        "option4": "try-except block",
        "correct_answer": "for loop"
    },
    {
        "id": 3,
        "question": "What is the purpose of using dictionaries in Python?",
        "option1": "To store ordered data",
        "option2": "To store data in key-value pairs",
        "option3": "To store only numeric data",
        "option4": "To perform mathematical operations",
        "correct_answer": "To store data in key-value pairs"
    },
    {
        "id": 4,
        "question": "What is the primary purpose of using functions in programming?",
        "option1": "To repeat a block of code",
        "option2": "To organize code into reusable units",
        "option3": "To display output on the screen",
        "option4": "To handle errors and exceptions",
        "correct_answer": "To organize code into reusable units"
    },
    {
        "id": 5,
        "question": "What is the purpose of using databases in software development?",
        "option1": "To improve user interface design",
        "option2": "To perform mathematical calculations",
        "option3": "To store and manage data persistently",
        "option4": "To generate random numbers",
        "correct_answer": "To store and manage data persistently"
    },
    {
        "id": 6,
        "question": "Which Python statement is used to catch and handle exceptions?",
        "option1": "try-except",
        "option2": "if-else",
        "option3": "for",
        "option4": "while",
        "correct_answer": "try-except"
    },
    {
        "id": 7,
        "question": "What does the term 'IDE' stand for in software development?",
        "option1": "Integrated Development Environment",
        "option2": "Interpreted Development Environment",
        "option3": "Interactive Design Environment",
        "option4": "Innovative Development Engine",
        "correct_answer": "Integrated Development Environment"
    },
    {
        "id": 8,
        "question": "What is the purpose of a while loop in Python?",
        "option1": "To execute a block of code a fixed number of times",
        "option2": "To iterate over a sequence of elements",
        "option3": "To execute a block of code indefinitely until a condition is met",
        "option4": "To handle errors and exceptions",
        "correct_answer": "To execute a block of code indefinitely until a condition is met"
    },
    {
        "id": 9,
        "question": "Which data structure in Python is used to represent a collection of elements with unique keys?",
        "option1": "List",
        "option2": "Tuple",
        "option3": "Set",
        "option4": "Dictionary",
        "correct_answer": "Dictionary"
    },
    {
        "id": 10,
        "question": "What is the purpose of using modules in Python?",
        "option1": "To store and manage data",
        "option2": "To perform mathematical operations",
        "option3": "To organize code into separate files for reusability",
        "option4": "To handle errors and exceptions",
        "correct_answer": "To organize code into separate files for reusability"
    }
]
# for loop to insert questions into the BusinessApplications table
# for question in business_app_questions:
#     cursor.execute('''INSERT INTO BusinessApplications (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

# List of questions for Programming Logic course
programming_logic_questions = [
    {
        "id": 1,
        "question": "What is the primary purpose of using version control systems like GitHub?",
        "option1": "To manage database transactions",
        "option2": "To track changes in code and collaborate with others",
        "option3": "To analyze user behavior on websites",
        "option4": "To design user interfaces for web applications",
        "correct_answer": "To track changes in code and collaborate with others"
    },
    {
        "id": 2,
        "question": "Which programming language is widely used for web development and data analysis?",
        "option1": "Java",
        "option2": "C++",
        "option3": "Python",
        "option4": "Ruby",
        "correct_answer": "Python"
    },
    {
        "id": 3,
        "question": "What is the purpose of using Wix in web development?",
        "option1": "To write server-side code",
        "option2": "To create and design websites without coding",
        "option3": "To manage databases",
        "option4": "To perform data analysis",
        "correct_answer": "To create and design websites without coding"
    },
    {
        "id": 4,
        "question": "Which of the following is an important skill for professionalism in the workplace?",
        "option1": "Adaptability",
        "option2": "Ignoring feedback",
        "option3": "Avoiding teamwork",
        "option4": "Isolation",
        "correct_answer": "Adaptability"
    },
    {
        "id": 5,
        "question": "What is the primary goal of critical thinking in problem-solving?",
        "option1": "To follow predefined rules",
        "option2": "To analyze situations and make informed decisions",
        "option3": "To avoid challenges",
        "option4": "To repeat previous mistakes",
        "correct_answer": "To analyze situations and make informed decisions"
    },
    {
        "id": 6,
        "question": "What does a personal SWOT analysis aim to identify?",
        "option1": "Strengths, weaknesses, opportunities, and threats",
        "option2": "Software development techniques",
        "option3": "Systematic web operations training",
        "option4": "Server-side web optimization tactics",
        "correct_answer": "Strengths, weaknesses, opportunities, and threats"
    },
    {
        "id": 7,
        "question": "Which of the following is NOT a benefit of effective communication in the workplace?",
        "option1": "Improved teamwork",
        "option2": "Increased productivity",
        "option3": "Confusion and misunderstandings",
        "option4": "Enhanced collaboration",
        "correct_answer": "Confusion and misunderstandings"
    },
    {
        "id": 8,
        "question": "What is the significance of algorithmic thinking in programming?",
        "option1": "To write code quickly without planning",
        "option2": "To solve problems efficiently and logically",
        "option3": "To rely solely on trial and error",
        "option4": "To ignore best practices",
        "correct_answer": "To solve problems efficiently and logically"
    },
    {
        "id": 9,
        "question": "What role does creativity play in software development?",
        "option1": "It is not relevant",
        "option2": "It is only important for graphic design",
        "option3": "It fuels innovation and problem-solving",
        "option4": "It is only important for marketing",
        "correct_answer": "It fuels innovation and problem-solving"
    },
    {
        "id": 10,
        "question": "What does the 'DRY' principle in programming stand for?",
        "option1": "Don't Repeat Yourself",
        "option2": "Do Repeat Yourself",
        "option3": "Don't Run Yourself",
        "option4": "Do Run Yourself",
        "correct_answer": "Don't Repeat Yourself"
    }
]
# Insert questions into the ProgrammingLogic table
# for question in programming_logic_questions:
#     cursor.execute('''INSERT INTO ProgrammingLogic (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

# List of questions for Business Intelligence and Analytics Capstone course
bi_analytics_questions = [
    {
        "id": 1,
        "question": "What is the primary purpose of using Python in Google Colab?",
        "option1": "To create business presentations",
        "option2": "To analyze data and create models",
        "option3": "To design user interfaces",
        "option4": "To generate random numbers",
        "correct_answer": "To analyze data and create models"
    },
    {
        "id": 2,
        "question": "Which regression technique is used to estimate the relationship between variables when the data has outliers?",
        "option1": "Quantile regression",
        "option2": "LASSO regression",
        "option3": "Linear regression",
        "option4": "Logistic regression",
        "correct_answer": "Quantile regression"
    },
    {
        "id": 3,
        "question": "What is the purpose of data cleaning in analytics?",
        "option1": "To make the data look better",
        "option2": "To remove outliers and errors from the data",
        "option3": "To add noise to the data",
        "option4": "To decrease data quality",
        "correct_answer": "To remove outliers and errors from the data"
    },
    {
        "id": 4,
        "question": "What does data standardization aim to achieve?",
        "option1": "To make the data less consistent",
        "option2": "To increase data variability",
        "option3": "To transform data into a standard format",
        "option4": "To add noise to the data",
        "correct_answer": "To transform data into a standard format"
    },
    {
        "id": 5,
        "question": "Which type of data visualization is commonly used to display correlations between variables?",
        "option1": "Heatmaps",
        "option2": "Barplots",
        "option3": "Pie charts",
        "option4": "Line graphs",
        "correct_answer": "Heatmaps"
    },
    {
        "id": 6,
        "question": "What statistical technique is used to analyze the relationship between two continuous variables?",
        "option1": "T-test",
        "option2": "ANOVA",
        "option3": "Linear regression",
        "option4": "Chi-square test",
        "correct_answer": "Linear regression"
    },
    {
        "id": 7,
        "question": "What is the purpose of a client presentation in the capstone project?",
        "option1": "To present data in a visually appealing way",
        "option2": "To answer a business-related question using data and analysis",
        "option3": "To demonstrate proficiency in Python programming",
        "option4": "To generate random data",
        "correct_answer": "To answer a business-related question using data and analysis"
    },
    {
        "id": 8,
        "question": "What is the main goal of linear regression analysis?",
        "option1": "To predict categorical outcomes",
        "option2": "To estimate the relationship between dependent and independent variables",
        "option3": "To analyze variance in a dataset",
        "option4": "To perform hypothesis testing",
        "correct_answer": "To estimate the relationship between dependent and independent variables"
    },
    {
        "id": 9,
        "question": "What type of data is suitable for logistic regression analysis?",
        "option1": "Continuous data",
        "option2": "Categorical data",
        "option3": "Ordinal data",
        "option4": "Nominal data",
        "correct_answer": "Categorical data"
    },
    {
        "id": 10,
        "question": "What is the primary objective of a statistical model?",
        "option1": "To make data analysis more complex",
        "option2": "To summarize and interpret data",
        "option3": "To generate random numbers",
        "option4": "To remove outliers from the data",
        "correct_answer": "To summarize and interpret data"
    }
]

#use a for loop to insert questions into the AnalyticsCapstone table
# for question in bi_analytics_questions:
#     cursor.execute('''INSERT INTO AnalyticsCapstone (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()

# List of questions for Business Law course
business_law_questions = [
    {
        "id": 1,
        "question": "What is the primary purpose of court jurisdiction?",
        "option1": "To decide which judge will preside over the case",
        "option2": "To determine the geographical area where a court has authority",
        "option3": "To establish the legal precedents for a case",
        "option4": "To issue arrest warrants",
        "correct_answer": "To determine the geographical area where a court has authority"
    },
    {
        "id": 2,
        "question": "What is a complaint in the legal context?",
        "option1": "A formal charge or allegation against a defendant",
        "option2": "A request for a jury trial",
        "option3": "A motion to dismiss a case",
        "option4": "A settlement agreement",
        "correct_answer": "A formal charge or allegation against a defendant"
    },
    {
        "id": 3,
        "question": "What is the process of litigation?",
        "option1": "The resolution of legal disputes through negotiation",
        "option2": "The formal process of taking legal action and resolving disputes in court",
        "option3": "The process of arbitration",
        "option4": "The process of mediation",
        "correct_answer": "The formal process of taking legal action and resolving disputes in court"
    },
    {
        "id": 4,
        "question": "What is arbitration?",
        "option1": "A form of alternative dispute resolution where a neutral third party makes a binding decision",
        "option2": "A court hearing for small claims cases",
        "option3": "A pretrial conference between attorneys and the judge",
        "option4": "A legal remedy for breach of contract",
        "correct_answer": "A form of alternative dispute resolution where a neutral third party makes a binding decision"
    },
    {
        "id": 5,
        "question": "What is employment law primarily concerned with?",
        "option1": "Protecting the rights of employers",
        "option2": "Regulating the hiring process",
        "option3": "Protecting the rights of employees",
        "option4": "Setting minimum wage rates",
        "correct_answer": "Protecting the rights of employees"
    },
    {
        "id": 6,
        "question": "What is the purpose of a non-compete agreement?",
        "option1": "To prevent employees from disclosing confidential information",
        "option2": "To restrict employees from working for a competitor after leaving the company",
        "option3": "To provide employees with job security",
        "option4": "To ensure equal pay for equal work",
        "correct_answer": "To restrict employees from working for a competitor after leaving the company"
    },
    {
        "id": 7,
        "question": "What does the term 'at-will employment' mean?",
        "option1": "Employment that is guaranteed for a fixed period of time",
        "option2": "Employment that can be terminated by either the employer or employee at any time, with or without cause",
        "option3": "Employment that requires approval from a labor union",
        "option4": "Employment that is based on a commission structure",
        "correct_answer": "Employment that can be terminated by either the employer or employee at any time, with or without cause"
    },
    {
        "id": 8,
        "question": "What is the purpose of the Fair Labor Standards Act (FLSA)?",
        "option1": "To regulate workplace safety standards",
        "option2": "To prohibit discrimination in employment",
        "option3": "To establish minimum wage, overtime pay, recordkeeping, and youth employment standards",
        "option4": "To provide employees with paid vacation time",
        "correct_answer": "To establish minimum wage, overtime pay, recordkeeping, and youth employment standards"
    },
    {
        "id": 9,
        "question": "What is the main goal of intellectual property law?",
        "option1": "To protect the rights of employees",
        "option2": "To regulate workplace safety standards",
        "option3": "To prevent the unauthorized use or exploitation of creative works and inventions",
        "option4": "To establish minimum wage rates",
        "correct_answer": "To prevent the unauthorized use or exploitation of creative works and inventions"
    },
    {
        "id": 10,
        "question": "What is the primary purpose of a contract?",
        "option1": "To create legal obligations between parties",
        "option2": "To establish workplace policies",
        "option3": "To provide employees with job security",
        "option4": "To regulate workplace safety standards",
        "correct_answer": "To create legal obligations between parties"
    }
]

# for loop to insert questions into the BusinessLaw table
# for question in business_law_questions:
#     cursor.execute('''INSERT INTO BusinessLaw (id, question, option1, option2, option3, option4, correct_answer)
#                       VALUES (?, ?, ?, ?, ?, ?, ?)''', (question['id'], question['question'], question['option1'],
#                                                          question['option2'], question['option3'], question['option4'],
#                                                          question['correct_answer']))
#     conn.commit()


def add_new_question(table, id, question, option1, option2, option3, option4, correct_answer):
    try:
        # Connect to the database
        conn = sqlite3.connect('quiz_bowlGUI.db')
        cursor = conn.cursor()

        # Insert the new question into the specified category table(add 1 to previous id )
        cursor.execute(f"INSERT INTO {table} (id, question, option1, option2, option3, option4, correct_answer) "
                       "VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (id, question, option1, option2, option3, option4, correct_answer))
        
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        print("New question added successfully!")

    except sqlite3.Error as error:
        print("Error adding new question:", error)
add_new_question('BusinessStrategy',11,'What general strategy targets a specific subset of a market and focuses on uniqueness?','Cost Leadership','Focused Cost Leadership','Differentiation','Focused Differentiation','Focused Differentiation')