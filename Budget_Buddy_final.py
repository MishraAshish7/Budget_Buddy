from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
import csv
from datetime import date, datetime
import os
import random
import string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO



app = Flask(__name__)
app.secret_key = 'hshusy73gs'  # Replace with your secret key


# Helper functions
def salts():
    salt = ["*@($12$", "423h4", "ewj7", "jlsow3", "3h2", "ash", "ish", "1%@", "HSs", "a2a", "ksam&", "%@lc", "mko",
            "s03", "*@%S", "vAI", "q9#", "lauA", "Y!617", ",wso.2(", "ka8", ")-1m", "ka^2", "ba%2", "ksi(@", "bdu4",
            "au3",
            "ja", "neu3", "nj23r", "iuo", "nkj409", "ayu", "sh", "BJ@", "&*(", "kj*", "@#(", "mk", "pos", "wqd9",
            "a7ha", "js",
            "o*@*", "*@HS", "ka9", "ns8", "(@Js", "nsU*#", "lsis", "nxus", "pwie", "os*", "@j", "ks9[", "!`", "jsus",
            "hs",
            "SUBX", "ius", "*()", "jis", "i91", "nx7", "ow8", "o9", "2js", "jwq", "iue", "9i3", "32k", "dwj", "ijd",
            "q89",
            "rc3", "UKxB", "84Cp", "RB+", "N5c", "NZw", "$I1", "iyM", "SCi", "XsC", "7cH", "D1B", "/2g", "twb", "hE2",
            "3q5", "NVa", "eXp", "6t0I", "w+x4", "jxE", "bMh", "UnX", "BrT", "8eB", "OEy", "KBS", "g$U", "OvS", "Uql",
            "Ptc", "QX/", "U2I", "mvv", "vWG", "TXC", "W1Z", "T2N", "8/E", "qSX", "SI4", "RpM", "Ifc", "82r", "ENH",
            "2JD",
            "oKC", "TYs", "38A", "$ZI", "4b/", "YcV", "DfQ", "3uG", "l38", "6id", "B+t", "GT3", "L1C", "Ddw", "RlV",
            "PzR",
            "bQX", "BQ", "sxY", "vt6", "1Vj", "DQm", "ajy", "uUX", "Qe5", "uzu", "12g", "CiB", "55L", "OMm", "dSP",
            "j9Q",
            "sE9", "xKF", "OFI", "e6", "9dz", "THZ", "d5F", "Kwp", "zii", "MTH", "LB.", "ua8", "Iar", "wvu", "JNk",
            "PN1",
            "3Ii", "5J/", "lk.", "2wZ", "/pi", "nq", "vXt", "Dm9", "1.A", "qBg", "N18", "4fw", "qn4", ".j.", "N0D",
            "A0B",
            "8oe", "0Xk", "bqg", "tXj", "1GC", "LeT", "rVB", "ae", "/Bl", "Jg.", "8mM", "2kZ", "Mer", "mdW", "qU.",
            "F0T",
            "ckL", "DXW", "7hB", "LwY", "xOO", "2qB", "gfj", "rpY", "4mde", "FFV", "G3W", "EtC", "LKg", "kwO", "3BI",
            "Ghb", "eTd", "JNu", "1go", "Z9c", "ykq", "HeG", "nzK", "MQC", "m0L", "GtD", "K", "uVz", "TQw", "wa/",
            "qO3",
            "QVu", "C7V", "AuW", "eBr", "c01", "Fsw", "YNf", "UK8", "Ung", "F3z", ".RI", "rCS", "h7t", "1G"]
    random.shuffle(salt)
    return salt


def characters():
    return list(" " + string.digits + string.ascii_letters + string.punctuation)


def chars_keys():
    return ['(', 'T', '`', '{', 'v', '!', '$', 'z', '_', '^', 'p', 'e', 'V', '0', '6', 'o', '&', '-', '"', 'w', 'R',
            "'", 'O', '<', '.', 'L', 'b', 'm', 'U', '>', 'i', 'G', 'k', 'd', ' ', 'h', 'c', ',', 'q', '3', 'X', 'M',
            '[', '|', 'g', 'Q', '2', 'C', 's', 'N', 'H', 'S', 'P', '7', 'D', '@', '9', 'j', '?', 'K', 't', 'F', '8',
            '%',
            'A', '~', '5', '/', 'y', '1', 'J', 'W', '=', 'B', ')', 'f', 'E', 'u', 'Y', '*', '+', 'x', ']', ';', 'a',
            '4', '#', 'I', '}', 'l', ':', 'n', 'r', 'Z']


def encrypter(password):
    salt = salts()
    char_to_list = characters()
    keys = chars_keys()

    encrypted_value = ""
    for i in password:
        if i in char_to_list:
            index = char_to_list.index(i)
            encrypted_value += keys[index]
        else:
            raise ValueError(f"Character {i} not found in character list")

    after_salt = ""
    for i in range(0, len(encrypted_value), 2):
        after_salt += salt[i % len(salt)]
    after_salt += (salt[6] + encrypted_value[:3] + salt[4] + salt[7] + salt[1] + encrypted_value[3:6] +
                   salt[2] + salt[8] + encrypted_value[6:] + salt[3] + salt[11] + salt[13] + salt[12])

    return after_salt


def decrypter(hashed_password):
    salt = salts()
    char_to_list = characters()
    keys = chars_keys()

    def remove_salt(encrypted_value):
        for s in salt:
            encrypted_value = encrypted_value.replace(s, "")
        return encrypted_value

    pass_2_decrypt = remove_salt(hashed_password)
    decrypted = ""

    for i in pass_2_decrypt:
        if i in keys:
            index = keys.index(i)
            decrypted += char_to_list[index]
        else:
            raise ValueError(f"Character {i} not found in key list")

    return decrypted


def email_exists(email):
    try:
        with open('../BudgetBuddy/data/BB_user_credentials_data.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[2] == email:  # Check if email already exists
                    return True
    except FileNotFoundError:
        return False
    return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']

        if email_exists(email):
            flash('Email is already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))

        hashed_password = encrypter(password)

        try:
            with open('../BudgetBuddy/data/BB_user_credentials_data.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([first_name, last_name, email, email.split('@')[0], hashed_password])
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            with open('../BudgetBuddy/data/BB_user_credentials_data.csv', mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[2] == email:
                        if decrypter(row[4]) == password:
                            session['email'] = email
                            session['username'] = row[3]  # Assuming row[0] is the username
                            flash('Login successful!', 'success')
                            return redirect(url_for('dashboard'))
                        else:
                            flash('Invalid password. Please try again.', 'error')
                            return redirect(url_for('login'))
            flash('Email not found. Please register.', 'error')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'email' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('email', None)  # Remove email from session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


# Function to handle adding expense
@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    if 'email' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

    username = session.get('username')
    if not username:
        flash('User session not found. Please log in again.', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Extract expense data from the form
        user_name = session.get('username')  # Assuming 'username' is stored in session
        date = request.form['date']
        amount = request.form['amount']
        amt_type = request.form['amount_type']
        category_code = request.form['category']
        description = request.form['description']

        # Category list
        Category_list = {
            "A": "Food & Dining",
            "B": "Transportation",
            "C": "Housing",
            "D": "Healthcare",
            "E": "Entertainment",
            "F": "Education",
            "G": "Personal Care",
            "H": "Clothing and Accessories",
            "I": "Travel",
            "J": "Miscellaneous",
            "K": "Salary",
            "L": "Earned Incomes",
            "M": "Investment Income",
            "N": "Royalties",
            "O": "Passive Income",
            "P": "Residual Income",
            "Q": "Portfolio Income"
        }

        category_name = Category_list.get(category_code, "Unknown")

        # File path
        file_name = "../BudgetBuddy/data/BB_expense_data.csv"

        # Preparing data as list
        data = [user_name, date, amount, amt_type, category_name, description]

        # Write data to CSV file
        try:
            with open(file_name, mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(data)
            flash('Transaction added successfully!', 'success')
        except Exception as e:
            flash(f'An error occurred: {e}', 'error')

        return redirect(url_for('dashboard'))

    return render_template('add_expense.html')


@app.route('/view_expense', methods=['GET', 'POST'])
def view_expense():
    if 'email' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

    try:
        data = pd.read_csv("../BudgetBuddy/data/BB_expense_data.csv")
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Username', 'Date', 'Amount', 'Type', 'Category', 'Description'])

    username = session.get('username')
    if not username:
        flash('User session not found. Please log in again.', 'warning')
        return redirect(url_for('login'))

    # Filter data for the logged-in user
    df = data[data["Username"] == username]

    if request.method == 'POST':
        category = request.form.get('category')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        # Debug: Print all form data
        print("Form Data:", request.form)

        # Apply category filter if specified
        if category:
            df = df[df['Category'] == category]
            print("Data after category filter:", df)

        # Apply date range filter if both start and end dates are specified
        if start_date and end_date:
            try:
                # Convert 'Date' column to datetime format
                df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d", errors='coerce')
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

                # Debug: Print parsed dates
                print("Parsed Start Date:", start_date)
                print("Parsed End Date:", end_date)

                # Apply date filter
                df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
                print("Data after date filter:", df)
            except ValueError:
                flash('Invalid date format. Please use yyyy-mm-dd.', 'error')

    # Group by category for display
    by_cat = df.groupby("Category")["Amount"].sum().reset_index()

    # Calculate total income, total expense, and net savings
    income_df = df[df["Type"] == "Income"]
    total_income = income_df["Amount"].sum()

    expense_df = df[df["Type"] == "Expense"]
    total_expense = expense_df["Amount"].sum()

    net_savings = total_income - total_expense

    # Debug: Print final filtered data
    print("Final Filtered Data:", df)

    return render_template('view_expense.html', expenses=df.to_dict(orient='records'),
                           categories=by_cat.to_dict(orient='records'),
                           total_income=total_income, total_expense=total_expense, net_savings=net_savings)



@app.route('/generate_report', methods=['GET', 'POST'])
def generate_report():
    if 'email' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

    report_message = ""
    report_image_url = None

    if request.method == 'POST':
        u_name = session['username']
        data = pd.read_csv("../BudgetBuddy/data/BB_expense_data.csv")
        df = pd.DataFrame(data)
        df = df[df["Username"] == u_name]

        if df.empty:
            report_message = "No data available to generate the report."
        else:
            report_type = request.form.get('report_type')
            report_image_url = generate_report_image(df, report_type)
            if not report_image_url:
                report_message = "An error occurred while generating the report."

    return render_template('generate_report.html', message=report_message, report_image_url=report_image_url)


def generate_report_image(df, report_type):
    try:
        if not os.path.exists('static/reports'):
            os.makedirs('static/reports')

        if report_type == "summary":
            # Generate summary statistics report
            return create_summary_stats_image(df)
        elif report_type == "category":
            # Generate category breakdown report
            return create_category_breakdown_image(df)
        else:
            return None
    except Exception as e:
        print(f"Error generating report image: {e}")
        return None


def create_summary_stats_image(df):
    income_df = df[df["Type"] == "Income"]
    expense_df = df[df["Type"] == "Expense"]

    total_income = income_df["Amount"].sum()
    total_expense = expense_df["Amount"].sum()
    net_savings = total_income - total_expense

    fig, (fig1, fig2) = plt.subplots(1, 2, figsize=(18, 8))

    # Pie chart for income and expense distribution
    charts = df.groupby("Type")["Amount"].sum()
    fig1.pie(charts, autopct="%1.1f%%", labels=charts.index, startangle=140, pctdistance=0.85,
             wedgeprops=dict(width=0.3, edgecolor='w'))
    fig1.set_title("Distribution of Income and Expense", fontsize=16, fontweight="bold", color="black")
    fig1.axis("equal")

    # Bar plot for income and expense by type
    sns.barplot(x=charts.index, y=charts.values, palette="viridis", hue=charts.index, ax=fig2)
    fig2.set_title("Income and Expense by Type", fontsize=16, fontweight="bold", color="black")
    fig2.set_xlabel("Type", fontsize=14, fontweight="bold")
    fig2.set_ylabel("Amount", fontsize=14, fontweight="bold")

    for ax in (fig1, fig2):
        for spine in ax.spines.values():
            spine.set_edgecolor("black")
            spine.set_linestyle("--")
            spine.set_linewidth(1.5)

    plt.tight_layout()
    file_path = 'static/reports/summary_report.png'
    plt.savefig(file_path)
    plt.close()

    return url_for('static', filename='reports/summary_report.png')


def create_category_breakdown_image(df):
    income_df = df[df["Type"] == "Income"]
    expense_df = df[df["Type"] == "Expense"]

    bycategory_expense = expense_df.groupby("Category")["Amount"].sum()
    bycategory_income = income_df.groupby("Category")["Amount"].sum()

    fig, ((fig1, fig2), (fig3, fig4)) = plt.subplots(2, 2, figsize=(18, 8))

    fig1.pie(bycategory_expense, autopct="%1.1f%%", labels=bycategory_expense.index, startangle=140, pctdistance=0.85,
             wedgeprops=dict(width=0.3, edgecolor='w'))
    fig1.set_title("Expenses by Category", fontsize=16, fontweight="bold", color="black")
    fig1.axis("equal")

    sns.barplot(x=bycategory_expense.index, y=bycategory_expense.values, palette="viridis", ax=fig2)
    fig2.set_title("Expenses by Category", fontsize=16, fontweight="bold", color="black")
    fig2.set_xlabel("Category", fontsize=14, fontweight="bold")
    fig2.set_ylabel("Amount", fontsize=14, fontweight="bold")

    fig3.pie(bycategory_income, autopct="%1.1f%%", labels=bycategory_income.index, startangle=140, pctdistance=0.85,
             wedgeprops=dict(width=0.3, edgecolor='w'))
    fig3.set_title("Income by Category", fontsize=16, fontweight="bold", color="black")
    fig3.axis("equal")

    sns.barplot(x=bycategory_income.index, y=bycategory_income.values, palette="viridis", ax=fig4)
    fig4.set_title("Income by Category", fontsize=16, fontweight="bold", color="black")
    fig4.set_xlabel("Category", fontsize=14, fontweight="bold")
    fig4.set_ylabel("Amount", fontsize=14, fontweight="bold")

    for ax in (fig1, fig2, fig3, fig4):
        for spine in ax.spines.values():
            spine.set_edgecolor("black")
            spine.set_linestyle("--")
            spine.set_linewidth(1.5)

    plt.tight_layout()
    file_path = 'static/reports/category_report.png'
    plt.savefig(file_path)
    plt.close()

    return url_for('static', filename='reports/category_report.png')

if __name__ == '__main__':
    app.run(debug=True)
