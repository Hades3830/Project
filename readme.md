# Introduction
I am familiar with coding and have a basic understanding before CM3 by adding custom formulas and actions in notion. Before the begining the assignment I consulted my mother who works as a technical writer and asked how I can make the project faster, and lower the number of mistakes that I will make during the assignment. She recommended using CSV to store expenses since our team's project was creating a simple expense tracker.
Managing personal finances is an essential skill for everyone, enabling them to track their spending habits, save money, and work within a budget. The Expense Manager is a simple command-line application developed in Python that allows users to record and analyze their daily expenses easily. It is meant to be simple, lightweight, and very efficient: the right tool for people who want no frills in personal budget management.
This project builds upon the basic concepts of Python, such as file handling, functions, and loops. The application stores expenses in a CSV file, allowing data representation after closing the application. Also, the program is structured to provide easy navigation for users through simple menu prompts. 
By making use of Python's inbuilt libraries, this project tries to keep things simple, barring complicated dependencies, which helps beginners grasp the fundamental exercise in programming. This Expense Manager, thus, aims to provide a practical tool in tracking expenses whilst reinforcing core coding skills for any newcomer to Python.

## The Expense Manager provides the following core functionalities:
1. **Add an Expense:** Users can enter the amount spent, the category (such as food, transportation, entertainment), and the date of the expense. The data is then stored in a CSV file.
2. **View All Expenses:** Users can display all recorded expenses in a structured table format.
3. **Calculate Total Expenses:** The program calculates and displays the total amount spent.
4. **Data Persistence:** Expenses are saved in a CSV file, ensuring they are not lost when the program is closed.
5. **Testing with Pytest:** The project includes test cases for the core functions to ensure they work as expected.
6. **Simple User Interface:** The command-line menu is designed to be intuitive, making it easy to navigate through different options.

 ## Essential files constituting the project are as follows: 

1. **project.py**
    - It is the main application file that contains the core functioning of the Expense Manager.
    - Provides functions of adding expenses, viewing expenses, and calculating expenses.
    - A simple menu for user interaction has been programmed.
2. **test_project.py**
    - This file contains test cases written with `pytest`.
    - It tests main function add_expense(), view_expenses(), and total_expenses().
    - Ensures that the program is reliable and works as intended.
3. **expenses.csv**
    - A data repository file where expenses are recorded.
    - Each new expense is added automatically with this file.
4. **requirements.txt**
    - Lists needed dependencies to run the project.
    - The main dependency is `pytest` for testing.
5. **README.md**
    - This file documents the project in detail so that one understands how it works, each file how it works, and with what each setting is set up and runs.

## The following are the key design considerations with which this project was conceived:

1. **Simplicity over Complexity**
    - The intention was to provide an application that is thoroughly **beginner-friendly** and very simple.
    - Instead of a classic way of storing data in a database, it chose the easy alternative: A CSV file.
2. **CLI as opposed to GUI**
    - While laying emphasis on the fundamentals of Python, the option was rather to keep it simple and develop a command-line interface.
    - Future iterations may consider a GUI using Tkinter or a web-based alternative in Flask.
3. **File-Based Data Storage**
    - For the sake of persistence, the CSV file format was preferred for data storage rather than an SQLite database.
    - This will allow users to work through their program without installing any extra dependencies or setting up a database.
4. **Minimal Dependencies**
    - The only dependencies for the project were Python’s built-in `csv` library and `pytest`, making it very lightweight and easy to install.
    - Hence, these options help minimize complexity and allow the greatest number of people to work with the project.
## How to Install and Run

### **Prerequisites**

- Install Python (if not already installed).
- Install dependencies by running:
    pip install -r requirements.txt
### **Running the Expense Manager**

1. Open a terminal and navigate to the project folder.
2. Run the program using:
    python project.py
3. Follow the on-screen menu to add, view, or calculate expenses.

### **Running Tests**

1. Ensure `pytest` is installed:
    pip install pytest
2. Run the tests using:
    pytest test_project.py

this project fulfills the basic criteria of an expense-tracking application, it leaves room for numerous enhancements in the future:

- **Graphical Interface Implementation:** Tkinter will be used to build a simple GUI to enhance user engagement.
- **Database Support Implementation:** Moving from CSV to SQLite or PostgreSQL in order to provide multi-user access for expenses.
- **Expense Reports and Analytics:** Visualization of spending trends through the application of graphs using Matplotlib. 
- **User Authentication:** Facilitates multiple users to keep track of their expenses independently.
- **Cloud Integration:** Storing data inside a cloud database will allow access from different devices.
- **Mobile App Version:** Expanding the project features on a mobile app, using Kivy or Flutter, will give better user experience.
- **Automated Categorization:** Categorization of expenses with the use of machine learning from the past behavior of spending.
- **Supports Other Currency:** Enabling users to log-in different currencies while automatically doing conversion. 
### Conclusion
The Expense Manager is a lucid project for a beginner to learn Python programming, file handling, and simple testing using Pytest concepts. It provides elementary financial tracking functionality while preserving a simple and easy-to-work-with interface.

Keeping ***simplicity*** in mind, this project is a ***wonderful learning tool*** for beginners in Python subjects and for people who would actually use it. With CSV file storage and a command-line interface, it is very easy to maintain and expand down the line. 

This is a good beginner project that could generate interest in programming and finance among many people. The project is scalable to allow incorporating more enhancements, like **data visualization, database integration, or AI-powered financial insights**.