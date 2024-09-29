# ### Project Overview: Expense Tracker
# **Goal**: To create an application that helps users track their expenses, categorize them, and generate reports or summaries.
#
# ### Key Features:
# 1. **Add Expenses**: Users can enter details of their expenses including amount, category, date, and description.
# 2. **View Expenses**: Users can view a list of their expenses with the ability to filter by category or date range.
# 3. **Generate Reports**: Users can generate summaries or reports of their expenses over a specific period.
# 4. **Data Persistence**: Expenses are stored persistently in a file or database.
#
# ### Main Components:
#
# 1. **User Interface (UI)**
#    - A form to input expense details.
#    - Buttons or links for viewing expenses and generating reports.
#    - A display area for showing lists and summaries.
#
# 2. **Backend Logic**
#    - Functions to handle adding expenses.
#    - Functions to retrieve and filter expenses.
#    - Functions to generate summaries and reports.
#
# 3. **Data Storage**
#    - Saving and loading expense data to/from a file or database.
#
# ### Tree Diagram of User Actions and Responses
#
# #### 1. **Start Application**
#
#    - **Action**: User starts the application.
#    - **Response**: Display main menu with options to add expenses, view expenses, or generate reports.
#
# ```
# Start Application
# │
# ├── Display Main Menu
# │   ├── Option: Add Expense
# │   ├── Option: View Expenses
# │   └── Option: Generate Report
# ```
#
# #### 2. **Add Expense**
#
#    - **Action**: User selects "Add Expense" option.
#    - **Response**: Display form to input expense details.
#
# ```
# Add Expense
# │
# ├── Display Input Form
# │   ├── Field: Amount
# │   ├── Field: Category
# │   ├── Field: Date
# │   └── Field: Description
# │
# ├── User Submits Form
# │   ├── Validate Input (Check for completeness and correctness)
# │   ├── Save Expense to Data Storage
# │   └── Display Confirmation Message
# ```
#
# #### 3. **View Expenses**
#
#    - **Action**: User selects "View Expenses" option.
#    - **Response**: Display options to filter and view expenses.
#
# ```
# View Expenses
# │
# ├── Display Filter Options
# │   ├── Filter by Category
# │   ├── Filter by Date Range
# │   └── View All Expenses
# │
# ├── User Applies Filter
# │   ├── Retrieve Expenses from Data Storage
# │   ├── Display Filtered Expenses
# │   └── Allow Export (e.g., CSV) or Further Actions
# ```
#
# #### 4. **Generate Report**
#
#    - **Action**: User selects "Generate Report" option.
#    - **Response**: Display options to specify report parameters.
#
# ```
# Generate Report
# │
# ├── Display Report Parameters
# │   ├── Specify Date Range
# │   └── Choose Report Type (e.g., Summary, Detailed)
# │
# ├── User Submits Parameters
# │   ├── Retrieve Data Based on Parameters
# │   ├── Generate Report
# │   └── Display Report or Provide Download Option
# ```
#
# #### 5. **Exit Application**
#
#    - **Action**: User chooses to exit the application.
#    - **Response**: Confirm exit and close the application.
#
# ```
# Exit Application
# │
# └── Confirm Exit
#     └── Close Application
# ```
#
# ### Detailed Flow
#
# 1. **Start Application**:
#    - On starting, the application shows a main menu with options: "Add Expense", "View Expenses", and "Generate Report".
#
# 2. **Add Expense**:
#    - When the user chooses to add an expense, they are presented with a form to enter details.
#    - After submission, the application validates the input, saves the data, and confirms the action.
#
# 3. **View Expenses**:
#    - Selecting "View Expenses" shows filtering options (by category or date range) and a list of expenses.
#    - Users can apply filters to view specific entries or choose to see all expenses.
#
# 4. **Generate Report**:
#    - Users choose to generate a report, specifying parameters like date range and report type.
#    - The application processes these parameters, generates the report, and presents it or provides a download option.
#
# 5. **Exit Application**:
#    - Users can choose to exit, which triggers a confirmation and then closes the application.

import string as st
import random
import csv
from datetime import date, datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Salts
def salts():
    salt = ["*@($12$", "423h4", "ewj7", "jlsow3", "3h2", "ash", "ish", "1%@", "HSs", "a2a", "ksam&", "%@lc", "mko",
            "s03",
            "*@%S", "vAI", "q9#", "lauA", "Y!617", ",wso.2(", "ka8", ")-1m", "ka^2", "ba%2", "ksi(@", "bdu4", "au3",
            "ja",
            "neu3", "nj23r", "iuo", "nkj409", "ayu", "sh", "BJ@", "&*(", "kj*", "@#(", "mk", "pos", "wqd9", "a7ha",
            "js",
            "o*@*", "*@HS", "ka9", "ns8", "(@Js", "nsU*#", "lsis", "nxus", "pwie", "os*", "@j", "ks9[", "!`",
            "jsus", "hs",
            "SUBX", "ius", "*()", "jis", "i91", "nx7", "ow8", "o9", "2js", "jwq", "iue", "9i3", "32k", "dwj", "ijd",
            "q89",
            "rc3", "UKxB", "84Cp", "RB+", "N5c", "NZw", "$I1", "iyM", "SCi", "XsC", "7cH", "D1B", "/2g", "twb",
            "hE2",
            "3q5", "NVa", "eXp", "6t0I", "w+x4", "jxE", "bMh", "UnX", "BrT", "8eB", "OEy", "KBS", "g$U", "OvS",
            "Uql",
            "Ptc", "QX/", "U2I", "mvv", "vWG", "TXC", "W1Z", "T2N", "8/E", "qSX", "SI4", "RpM", "Ifc", "82r", "ENH",
            "2JD",
            "oKC", "TYs", "38A", "$ZI", "4b/", "YcV", "DfQ", "3uG", "l38", "6id", "B+t", "GT3", "L1C", "Ddw", "RlV",
            "PzR", "bQX", "BQ",
            "sxY", "vt6", "1Vj", "DQm", "ajy", "uUX", "Qe5", "uzu", "12g", "CiB", "55L", "OMm", "dSP", "j9Q", "sE9",
            "xKF", "OFI", "e6",
            "9dz", "THZ", "d5F", "Kwp", "zii", "MTH", "LB.", "ua8", "Iar", "wvu", "JNk", "PN1", "3Ii", "5J/", "lk.",
            "2wZ", "/pi", "nq", "vXt", "Dm9", "1.A", "qBg", "N18", "4fw", "qn4", ".j.", "N0D", "A0B", "8oe", "0Xk",
            "bqg", "tXj",
            "1GC", "LeT", "rVB", "ae", "/Bl", "Jg.", "8mM", "2kZ", "Mer", "mdW", "qU.", "F0T", "ckL", "DXW", "7hB",
            "LwY", "xOO", "2qB",
            "gfj", "rpY", "4mde", "FFV", "G3W", "EtC", "LKg", "kwO", "3BI", "Ghb", "eTd", "JNu", "1go", "Z9c",
            "ykq", "HeG", "nzK", "MQC",
            "m0L", "GtD", "K", "uVz", "TQw", "wa/", "qO3", "QVu", "C7V", "AuW", "eBr", "c01", "Fsw", "YNf", "UK8",
            "Ung", "F3z", ".RI",
            "rCS", "h7t", "1G"]
    random.shuffle(salt)
    return salt

# Characters
def characters():
    return list(" " + st.digits + st.ascii_letters + st.punctuation)

# Keys
def chars_keys():
    return ['(', 'T', '`', '{', 'v', '!', '$', 'z', '_', '^', 'p', 'e', 'V', '0', '6', 'o', '&', '-', '"', 'w', 'R',
            "'", 'O', '<', '.', 'L',
            'b', 'm', 'U', '>', 'i', 'G', 'k', 'd', ' ', 'h', 'c', ',', 'q', '3', 'X', 'M', '[', '|', 'g', 'Q', '2',
            'C', 's', 'N', 'H', 'S',
            'P', '7', 'D', '@', '9', 'j', '?', 'K', 't', 'F', '8', '%', 'A', '~', '5', '/', 'y', '1', 'J', 'W', '=',
            'B', ')', 'f', 'E',
            'u', 'Y', '*', '+', 'x', ']', ';', 'a', '4', '#', 'I', '}', 'l', ':', 'n', 'r', 'Z']



def encrypter(password):

    # Importing helper functions
    salt = salts()
    char_to_list = characters()
    keys = chars_keys()

    # Encryption logic
    encrypted_value = ""
    for i in password:
        if i in char_to_list:
            index = char_to_list.index(i)
            encrypted_value += keys[index]
        else:
            raise ValueError(f"Character {i} not found in character list")

    # Adding salt
    after_salt = ""
    for i in range(0, len(encrypted_value), 2):
        after_salt += salt[i % len(salt)]  # Ensure salt index is within range
    after_salt += (salt[6] + encrypted_value[:3] + salt[4] + salt[7] + salt[1] + encrypted_value[3:6] +
                   salt[2] + salt[8] + encrypted_value[6:] + salt[3] + salt[11] + salt[13] + salt[12])

    return after_salt


# Decrypter
def decrypter(hashed_password):
    # Importing helper functions
    salt = salts()
    char_to_list = characters()
    keys = chars_keys()

    def remove_salt(encrypted_value):
        # Remove all occurrences of each salt value
        for s in salt:
            encrypted_value = encrypted_value.replace(s, "")
        return encrypted_value

    # Remove salt from the hashed password
    pass_2_decrypt = remove_salt(hashed_password)
    decrypted = ""

    # Decrypting password
    for i in pass_2_decrypt:
        if i in keys:
            index = keys.index(i)
            decrypted += char_to_list[index]
        else:
            raise ValueError(f"Character {i} not found in key list")

    return decrypted


def decrypt_password_from_row(file_name, row_index):
    try:
        with open(file_name, mode="r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)  # Read all rows into a list

            if 0 <= row_index < len(rows):
                row = rows[row_index]
                hashed_password = row[4]  # Assuming hashed password is in the 5th column (index 4)
                decrypted_password = decrypter(hashed_password)
                return decrypted_password
            else:
                print("Row index out of range.")
                return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# User registration form
def user_registration_form():

    print("----------Hello my dear friend! Welcome to the User Registration Panel----------")
    print("----------Please enter the credentials below----------")

    # CSV File where we are going to append user credentials
    file_name = "data/BB_user_credentials_data.csv"

    # User Inputs
    # Getting first name of user
    while True:
        try:
            f_name = input("Enter your first name: ")
            if all(char in st.ascii_letters for char in f_name):
                break
            else:
                print("First Name cannot contain a number or special characters")
        except Exception as e:
            print("Ooops! An error occurred")

    # Getting last name of the user
    while True:
        try:
            l_name = input("Enter your last name: ")
            if all(char in st.ascii_letters for char in l_name):
                break
            else:
                print("Last Name cannot contain a number or special characters")
        except Exception as e:
            print("Ooops! An error occurred")

    # Getting user Gmail
    while True:
        try:
            # User Gmail
            Gmail = input("Enter your G-mail: ")
            if Gmail.endswith("@gmail.com"):  # Checking if gmail ends with @gmail.com

                # Removing @gmail part to validation
                u_name = Gmail[:-10]

                # Checking if Gmail does not start with a full stop
                if u_name.startswith("."):
                    print("Ooops! Gmail cannot start with fullstop (.)")

                # Checking if Gmail does not ends with a full stop
                elif u_name.endswith("."):
                    print("Ooops! Gmail cannot ends with fullstop (.)")

                # Checking if Gmail is not empty
                elif u_name == "":
                    print("Ooops! Gmail can't be empty")

                # Checking if length of Gmail username is greater than 30 characters
                elif len(u_name) > 30:
                    print("The length of gmail username is too long, please make it shorter")

                # Checking if Gmail does not contain anything rather than small letters(a-z) or numbers(0-9)
                elif all(char in st.ascii_lowercase + st.digits for char in u_name):
                    with open(file_name, mode="r", newline="") as file:
                        reader = csv.reader(file)
                        existing_email = [row[2] for row in reader]
                    if Gmail in existing_email:
                        print("Ooops! This Gmail is already registered! Please choose an different Gmail")
                    else:
                        break
                else:
                    print("Please enter an valid email(e.g. abc12@gmail.com)")

        except Exception as e:
            print("Ooops! An error occurred")

    # Getting user's username
    u_name = Gmail[:-10]

    # Getting user's password
    while True:
        try:
            password = input("Enter your password: ")
            if len(password) >= 6 and len(password) <= 9:
                break
            else:
                print("The length of password must greater than 6 digits and smaller than 9 digits")
        except Exception as e:
            print("Ooops! An error occurred")

    #Hashed password
    h_pass = encrypter(password)

    # Preparing data as a list
    data = [f_name, l_name, Gmail, u_name, h_pass]

    # Opening the file in append mode
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)

    # Writing data to csv file
        writer.writerow(data)
    print("Registration successful! Your details have been saved.")
    print("Please always remember your Username and Password for future login:")
    print(f"Your username is: {u_name}")
    print(f"Your password is: {password}")


#golbal variable to store the username
global_username = None

def login_form():

    global global_username

    # File name
    file_name = "data/BB_user_credentials_data.csv"

    # Validating Credentials Username
    while True:
        try:
            user_name = input("Enter Username: ")
            with open(file_name, mode="r", newline="") as file:
                reader = csv.reader(file)
                uname_match = [row[3] for row in reader]
                if user_name in uname_match:
                    index_value = uname_match.index(user_name)
                    global_username = user_name
                    break
                else:
                    print("User does not exist! Please enter an Valid User name")
        except Exception as e:
            print("Ooops! An error occurred")

    # Validating Credentials Passwords
    while True:
        try:
            password = input("Enter Password: ")
            pass_in_db = decrypt_password_from_row(file_name, index_value)
            if password == pass_in_db:
                print("Access Authorized")
                user_name = user_name
                break
            else:
                print("Access Denied! Please enter an valid password")
        except Exception as e:
            print("Ooops! An error occurred")



# Function: Add Expense
def add_expense():

    while True:
        # Category and their codes
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
            "K": "Salary"
        }

        # Getting expense entries
        u_name = global_username

        # Date
        while True:
            edate = input("Enter Date (dd-mm-yyyy) or press enter for today:")
            if edate == "":
                edate = date.today().strftime("%d-%m-%Y")
                break
            else:
                try:
                    datetime.strptime(edate, "%d-%m-%Y")
                    edate == edate
                    break
                except ValueError:
                    print("Invalid Format! Please enter date in correct format (dd-mm-yyyy)")

        # Amount
        while True:
            try:
                amt = float(input("Enter expense amount ($): "))
                if amt <= 0:
                    print("Expense amount must be greater than zero")
                else:
                    break
            except ValueError as e:
                print("Amount can't be a non number")
            except Exception as e:
                print("Ooops! An error occurred")

        # Type e.g. Income, Expense
        while True:
            amt_type = input("Enter type of Amount (I- Income, E- Expense): ").upper()
            if amt_type == "I":
                amt_type = "Income"
                break
            elif amt_type == "E":
                amt_type = "Expense"
                break
            else:
                print("Please enter an valid type (I- Income, E- Expense)")

        # Category
        while True:
            try:
                category_code = input("Enter category code of expense (press * for category code): ").upper()
                if category_code in Category_list.keys():
                    category_code = Category_list.get(category_code)
                    break
                elif category_code == "*":
                    for key, value in Category_list.items():
                        print(f"{key} : {value}")
                else:
                    print("Please enter an valid Category code")
            except Exception as e:
                print("Ooops! An error occurred")

        # Description
        desc = input("Enter detailed description: ")

        # File name
        file_name = "data/BB_expense_data.csv"

        # Preparing data as list
        data = [u_name, edate, amt, amt_type, category_code, desc]

        # Opening csv file to append data
        with open(file_name, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(data)

        print("Entry added successfully!!!")
        if input("Wanna add one more entry (y/n)?") != "y":
            print("Thanks man! Visit again")
            break


# Function : View Expenses
def view_expense():

    data = pd.read_csv("data/BB_expense_data.csv")
    df = pd.DataFrame(data)

    # For specific user
    u_name = global_username
    df = df[df["Username"] == u_name]

    df["Date"] = pd.to_datetime(df["Date"], format= "mixed")

    # Filtering data by Category
    by_cat = df.groupby("Category")["Amount"].sum()

    # Filtering data by date range
    def by_dateRange():
        while True:
            try:
                start_date = input("Enter start date (dd-mm-yyyy): ")
                end_date = input("Enter end date (dd-mm-yyyy): ")

                # Validating date formats
                datetime.strptime(start_date, "%d-%m-%Y")
                datetime.strptime(end_date, "%d-%m-%Y")
                break
            except ValueError:
                print("Invalid Format! Enter dates in dd-mm-yyyy")
            except Exception as e:
                print("Ooops! An error occurred")

    print("Filters:\n1) Filter by Category\n2) Filter by Date Range\n3) View all expenses")
    user_choice = input("Enter your choice (1-3): ")

    if user_choice == "1":
        print(by_cat)
    elif user_choice == "2":
        by_dateRange()
    elif user_choice == "3":
        print(df)
    else:
        print("Please enter an valid choice (1-3)")


def generate_report():

    u_name = global_username
    data = pd.read_csv("data/BB_expense_data.csv")
    df = pd.DataFrame(data)
    df = df[df["Username"] == u_name]

    # Summary Statistics
    def summary_stats():

        # Non-visually
        # total income
        income_df = df[df["Type"] == "Income"]
        total_income = sum(income_df["Amount"])

        # total expense
        expense_df = df[df["Type"] == "Expense"]
        total_expense = sum(expense_df["Amount"])

        # Savings
        net_savings = total_income - total_expense

        # Visually
        def visualize():

            # Preparing data for charts based on type
            charts = df.groupby("Type")["Amount"].sum()

            # Visualizing
            fig, (fig1, fig2) = plt.subplots(1, 2, figsize= (18,8))

            # Pie chart
            fig1.pie(charts, autopct="%1.1f%%", labels= charts.index, startangle= 140, pctdistance= 0.85,
                    wedgeprops=dict(width=0.3, edgecolor='w')
                    )
            fig1.set_title("Distribution of Income and Expense", fontsize= 16, fontweight= "bold", color= "black")
            fig1.axis("equal")

            # Bar plot
            sns.barplot(x= charts.index, y= charts.values, palette= "viridis", hue= charts.index, ax= fig2)
            fig2.set_title("Income and Expense by Type", fontsize=16, fontweight="bold", color="black")
            fig2.set_xlabel("Type", fontsize=14, fontweight="bold")
            fig2.set_ylabel("Amount", fontsize=14, fontweight="bold")

            # Adding borders
            for ax in (fig1, fig2):
                for spine in ax.spines.values():
                    spine.set_edgecolor("black")
                    spine.set_linestyle("--")
                    spine.set_linewidth(1.5)

            plt.tight_layout()
            plt.show()


        # Printing summary stats
        # Non visualize
        print("|--------------------------------------|")
        print("| Summary Statistics:                  |")
        print("----------------------------------------")
        print(f"| Total Income: ${total_income}               |")
        print(f"| Total Expense: ${total_expense}                |")
        print(f"| Net Savings: ${net_savings}                |")
        print("|--------------------------------------|")


        # Asking user if he wants visualization
        if input("You wanna see the charts (y/n)? ").lower() == "y":
            visualize()


    # Category wise spending and income
    def category_Breakdown_Report():

        income_df = df[df["Type"] == "Income"]

        expense_df = df[df["Type"] == "Expense"]

        # Category wise spending
        bycategory_expense = expense_df.groupby("Category")["Amount"].sum()

        # Category wise income
        bycategory_income = income_df.groupby("Category")["Amount"].sum()


        # Visualization
        # Visualizing
        def visualize():
            fig, ((fig1, fig2), (fig3, fig4)) = plt.subplots(2, 2, figsize=(18, 8))

            # Pie chart represents spending by category
            fig1.pie(bycategory_expense, autopct="%1.1f%%", labels=bycategory_expense.index, startangle=140, pctdistance=0.85,
                     wedgeprops=dict(width=0.3, edgecolor='w')
                     )
            fig1.set_title("Distribution of Income and Expense", fontsize=16, fontweight="bold", color="black")
            fig1.axis("equal")

            # Bar plot represents spending by category
            sns.barplot(x=bycategory_expense.index, y=bycategory_expense.values, palette="viridis", hue=bycategory_expense.index, ax=fig2)
            fig2.set_title("Income and Expense by Type", fontsize=16, fontweight="bold", color="black")
            fig2.set_xlabel("Type", fontsize=14, fontweight="bold")
            fig2.set_ylabel("Amount", fontsize=14, fontweight="bold")

            # Pie chart represents income by category
            fig3.pie(bycategory_income, autopct="%1.1f%%", labels=bycategory_income.index, startangle=140,
                     pctdistance=0.85,
                     wedgeprops=dict(width=0.3, edgecolor='w')
                     )
            fig3.set_title("Distribution of Income and Expense", fontsize=16, fontweight="bold", color="black")
            fig3.axis("equal")

            # Bar plot represents spending by category
            sns.barplot(x=bycategory_income.index, y=bycategory_income.values, palette="viridis",
                        hue=bycategory_income.index, ax=fig4)
            fig4.set_title("Income and Expense by Type", fontsize=16, fontweight="bold", color="black")
            fig4.set_xlabel("Type", fontsize=14, fontweight="bold")
            fig4.set_ylabel("Amount", fontsize=14, fontweight="bold")

            # Adding borders
            for ax in (fig1, fig2, fig3, fig4):
                for spine in ax.spines.values():
                    spine.set_edgecolor("black")
                    spine.set_linestyle("--")
                    spine.set_linewidth(1.5)

            plt.tight_layout()
            plt.show()

        # Printing distribution of income based on category
        print("|-----------------------------------------|")
        print("|Distribution of income based on category |")
        print("|-----------------------------------------|")
        for category, amount in bycategory_income.items():
            print(f"|{category} : ${amount}")
        print("|-----------------------------------------|")

        # Printing distribution of expense based on category
        print("\n")
        print("|-----------------------------------------|")
        print("|Distribution of expense based on category|")
        print("|-----------------------------------------|")
        for category, amount in bycategory_expense.items():
            print(f"|{category} : ${amount}")
        print("|-----------------------------------------|")

        # Asking user if he wants visualization
        if input("You wanna see the charts (y/n)? ").lower() == "y":
            visualize()


    def main():
        while True:
            print("1) Summary Statistics report\n2) Category wise breakdown report\n3) Exit")
            user_choice = input("Enter your choice (1-3): ")

            if user_choice == "1":
                summary_stats()
            elif user_choice == "2":
                category_Breakdown_Report()
            elif user_choice == "3":
                break
            else:
                print("Please enter an valid choice (1-3)")
    main()


def options():
    while True:
        print("1) Add Transactions\n2) View Transactions\n3) View Reports\n4) Exit")
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == "1":
            add_expense()
        elif user_choice == "2":
            view_expense()
        elif user_choice == "3":
            generate_report()
        elif user_choice == "4":
            break
        else:
            print("Please enter an valid choice(1-4)")

# Main application
def main_app():
    while True:
        print("------------------Hey buddy! Welcome to BudgetBuddy------------------")
        print("1) Login\n2) Register\n3) Exit")
        user_choice = input("Please enter your choice (1-3): ")

        if user_choice == "1":
            login_form()
            options()
        elif user_choice == "2":
            user_registration_form()
        elif user_choice == "3":
            break
main_app()








