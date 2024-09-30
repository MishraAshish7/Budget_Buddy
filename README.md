# Budget Buddy

## Overview

**Budget Buddy** is a web application designed to help users efficiently manage their personal finances by tracking expenses and providing an overview of their budgeting. The application features user authentication, expense logging, and a dashboard for easy access to financial summaries.

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [File Structure](#file-structure)
4. [Installation Guide](#installation-guide)
5. [Usage](#usage)
6. [User Interface](#user-interface)
7. [Code Details](#code-details)
8. [Credits](#credits)
9. [Future Enhancements](#future-enhancements)

---

## Features

- **User Authentication**: Users can register and log in to their accounts securely.
- **Expense Tracking**: Users can add, edit, and delete expenses easily.
- **Dashboard Overview**: A centralized page displaying a summary of the user's financial activities.
- **User-Friendly Interface**: Simple and intuitive HTML pages for seamless navigation.

---

## Technologies Used

- **HTML/CSS**: For creating responsive and interactive web pages.
- **Flask**: A Python web framework for building the back-end.
- **CSV Files**: Used as a lightweight database to store user data and expenses.
- **JavaScript**: For client-side interactivity (if applicable).
- **GitHub Pages**: For hosting the static files of the application.

---

## File Structure

```
BudgetBuddy/
│
├── home.html             # Landing page of the application
├── dashboard.html        # User dashboard displaying financial summary
├── add_expense.html      # Form to add new expenses
├── view_expense.html      # Page to view logged expenses
├── login.html            # Login page for users
├── register.html         # Registration page for new users
├── BB_expense_data.csv          # CSV file to store user expenses
├── BB_user_credentials_data.csv             # CSV file to store user data
└── Budget_Buddy_final.py  # Main Flask application file
```

### File Descriptions

- **home.html**: Introduces users to Budget Buddy and its features.
- **dashboard.html**: Provides an overview of user finances, including total expenses and budget tracking.
- **add_expense.html**: Contains a form where users can input new expenses.
- **view_expense.html**: Lists all logged expenses for the user, allowing for review and management.
- **login.html**: Interface for existing users to log in.
- **register.html**: Allows new users to create an account.
- **BB_expense_data.csv**: Stores all user expenses in a structured format.
- **BB_user_credentials_data.csv**: Stores user credentials and information.
- **Budget_Buddy_final.py**: The back-end logic using Flask, including routes for user authentication and expense management.

---

## Installation Guide

### Prerequisites

- Python 3.x installed on your machine.
- Basic understanding of command line usage.

### Step-by-Step Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**:
   ```bash
   pip install Flask
   ```

4. **Run the Flask Application**:
   ```bash
   python Budget_Buddy_final.py
   ```

5. **Access the Application**: Open a web browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

1. **Register**: Navigate to `register.html` to create a new user account.
2. **Login**: Use the `login.html` page to access your account.
3. **Manage Expenses**: After logging in, you can add expenses through the `add_expense.html` page, view your logged expenses on `view_expense.html`, and see your financial summary on the dashboard.

---

## User Interface

### Home Page
- Introduction to Budget Buddy with links to register and log in.

### Dashboard
- Overview of financial data with options to add new expenses and view existing ones.

### Add Expense Page
- A form allowing users to enter details of their expenses, including category, amount, and date.

### View Expense Page
- Displays a list of all expenses, with options to edit or delete entries.

---

## Code Details

### Flask Application

The core of the application is contained in `Budget_Buddy_final.py`, where the Flask server is set up to handle routes for user registration, login, and expense management. Below is a brief explanation of some key functions:

```python
from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Other routes (login, register, add_expense) follow...

# Example of reading from CSV for expenses
def read_expenses():
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)
```

### HTML Templates

Each HTML file is crafted to provide a seamless user experience. The templates are enhanced with CSS for styling and JavaScript for any dynamic behavior.

```html
<!-- Example snippet from login.html -->
<form action="/login" method="POST">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
    <button type="submit">Login</button>
</form>
```

---

## Credits

- **AI Tools Used**:
  - **ChatGPT**: Assisted in generating HTML templates and backend code.
  - **Blackbox AI**: Helped refine code and provide coding suggestions.

- **Contributors**: The core logic and file structures were developed by the project owner.

---

## Future Enhancements

- **Data Visualization**: Incorporate libraries like Chart.js to display expenses graphically.
- **Mobile Responsiveness**: Improve the design to ensure usability on mobile devices.
- **Notifications**: Implement features to alert users when they are close to exceeding their budget.
- **Export Options**: Allow users to export their expense data as CSV or PDF.

