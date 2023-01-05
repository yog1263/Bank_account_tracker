from tkinter import *
import sqlite3
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import MySQLdb
import sys
from fpdf import FPDF

root = Tk()
root.geometry("750x300")
root.config(bg="light blue")
root.title("Login Form")
#C = Canvas(root, bg="blue", height=300, width=400)
#filename = PhotoImage(file="C:\\Users\Hp\Desktop\images.png")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)


def Database():
    global conn, cursor
    #conn = MySQLdb.connect("localhost", "root", "", "Bank")
    conn = sqlite3.connect("Bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `Register` WHERE Username = '?' AND Password = '?' ")
    conn.commit()


def Login():
    Database()

    if Username.get() == "" or Password.get() == "":
        lbl_text.config(text="Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `Register` WHERE `Username` = ? AND `Password` = ?",
                       (Username.get(), Password.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            Username.set("")
            Password.set("")
            lbl_text.config(text="")
        else:
            res = messagebox.askretrycancel('Ask_RetryCancel', 'Invalid Username and Password')
            Username.set("")
            Password.set("")
    cursor.close()
    conn.close()


def HomeWindow():
    global REGISTER
    root.withdraw()
    REGISTER = Toplevel()
    REGISTER.config(bg="light blue")
    REGISTER.title(" Login Application")
    lbl_home = Label(REGISTER, text="Successfully Login!", font=('times new roman', 20))
    lbl_home.pack()

    def Welcome():
        global Welcome
        REGISTER.withdraw()
        Welcome = Toplevel()
        Welcome.geometry("400x350")
        Welcome.config(bg="light blue")
        Welcome.title("Welcome")
        lbl = Label(Welcome, text="************WELCOME************")
        lbl.grid(row=0)
        lbl.config(font=("bold", 20))
        Add_Account = Button(Welcome, text="ADD ACCOUNT", command=Add_account)
        Add_Account.grid(pady=25, row=3, columnspan=1)
        Add_Transaction = Button(Welcome, text="ADD NEW TRANSACTION", command=New_transaction)
        Add_Transaction.grid(pady=25, row=4, columnspan=3)
        Delete = Button(Welcome, text="DELETE", command=delete)
        Delete.grid(pady=25, row=5, columnspan=1)
        Show = Button(Welcome, text="Show", command=show)
        Show.grid(pady=25, row=6, columnspan=3)

    btn_Ok = Button(REGISTER, text='Ok', command=Welcome)
    btn_Ok.pack(pady=20, fill=X)

    def Add_account():

        window = Toplevel()
        window.geometry("450x370")
        window.configure(bg="light blue")
        window.title("ADD ACCOUNT")

        Holder_name = StringVar()
        Branch = StringVar()
        Account_no = StringVar()
        Costumer_id = StringVar()
        Ifsc = StringVar()
        Adhar_no = StringVar()
        DOB = StringVar()
        Phone_no = StringVar()
        Pan_no = StringVar()
        Email_id = StringVar()
        Address = StringVar()
        var = StringVar()
        c = StringVar()

        def database():
            name2 = Holder_name.get()
            branch = Branch.get()
            account_no = Account_no.get()
            costumer_id = Costumer_id.get()
            ifsc = Ifsc.get()
            adhar_no = Adhar_no.get()
            dob = DOB.get()
            phone_no = Phone_no.get()
            pan_no = Pan_no.get()
            email_id = Email_id.get()
            address = Address.get()
            Bank_name = c.get()
            account_type = var.get()
            if var == "Savings":
                'Savings'
            else:
                'Credit'

            if Holder_name.get() == "" or Branch.get() == "" or Account_no.get() == "" or Adhar_no.get() == "" or Costumer_id.get() == "":
                res = messagebox.askretrycancel('Ask_RetryCancel', 'Mandatory Data missing!!')
            else:
                conn = sqlite3.connect("Bank.db")
                with conn:
                    cursor = conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS ADD_ACCOUNT (Holder_name TEXT, Bank_name TEXT, Branch TEXT, '
                    'Account_no TEXT, '
                    'Account_type, Costumer_id TEXT, Ifsc TEXT, Adhar_no TEXT, DOB TEXT, Phone_no TEXT,Pan_no TEXT,'
                    'Email_id TEXT, '
                    'Address TEXT)')
                cursor.execute(
                    'INSERT INTO ADD_ACCOUNT (Holder_name, Bank_name, Branch, Account_no, Account_type, Costumer_id, '
                    'Ifsc, '
                    'Adhar_no, '
                    'DOB, Phone_no, Pan_no, Email_id, Address) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)',
                    (name2, Bank_name, branch, account_no, account_type, costumer_id, ifsc, adhar_no, dob, phone_no,
                     pan_no, email_id, address))
                res = messagebox.askokcancel('Ask_OKCancel', 'Account Added succesfully')
                window.withdraw()
                conn.commit()
                chk_state1 = forms.BooleanField(required=True)

        lbl = Label(window, text="Bank Holder's NAME", font=("bold", 12))
        lbl.grid(column=1, row=1)
        lbl.configure(background="light blue")

        txt = Entry(window, width=20, textvar=Holder_name)
        txt.grid(column=2, row=1)

        # Bank name

        lbl1 = Label(window, text="Bank Name", font=("bold", 12))
        lbl1.grid(column=1, row=2)
        lbl1.configure(background="light blue")

        list = ["--Bank name--", "ALLAHABAD BANK", "ANDRA BANK", "AXIS BANK", "BANK OF BARODA", "BANK OF INDIA",
                "BANK OF MAHARASTRA", "CANARA BANK", "CENTRAL BANK OF INDIA", "CORPORATION BANK", "DENA BANK",
                "IDBI BANK LTD.", "INDIAN BANK", "JAMMU & KASHMIR BANK LTD.", "KOTAK BANK", "PUNJAB NATIONAL BANK",
                "STATE BANK OF INDIA", "UNION BANK OF INDIA"]

        droplist = OptionMenu(window, c, *list)
        droplist.config(width=15)
        c.set('')
        droplist.grid(column=2, row=2)

        # BRANCH

        lbl2 = Label(window, text="BRANCH", font=("bold", 12))
        lbl2.grid(column=1, row=3)
        lbl2.configure(background="light blue")
        txt1 = Entry(window, width=20, textvar=Branch)
        txt1.grid(column=2, row=3)

        # ACCOUNT NO.

        lbl3 = Label(window, text="Account_no.", font=("bold", 12))
        lbl3.grid(column=1, row=4)
        lbl3.configure(background="light blue")

        def testVal(inStr, acttyp):
            if acttyp == '1':  # insert
                if not inStr.isdigit():
                    return False
            return True

        entry = Entry(window, width=20, textvar=Account_no, validate="key")
        entry['validatecommand'] = (entry.register(testVal), '%P', '%d')
        entry.grid(column=2, row=4)

        # Account type

        lbl4 = Label(window, text="Account type", font=("bold", 12))
        lbl4.grid(column=1, row=5)
        lbl4.configure(background="light blue")

        rad1 = Radiobutton(window, text="Savings", value="Savings", variable=var)

        rad2 = Radiobutton(window, text="Credit", value="Credit", variable=var)

        rad1.grid(column=2, row=5)
        rad2.grid(column=3, row=5)

        # CUSTOMER ID

        lbl5 = Label(window, text="CUSTOMER ID", font=("bold", 12))
        lbl5.grid(column=1, row=6)
        lbl5.configure(background="light blue")
        txt3 = Entry(window, width=20, textvar=Costumer_id)
        txt3.grid(column=2, row=6)

        # IFSC

        lbl6 = Label(window, text="IFSC", font=("bold", 12))
        lbl6.grid(column=1, row=7)
        lbl6.configure(background="light blue")
        txt4 = Entry(window, width=20, textvar=Ifsc)
        txt4.grid(column=2, row=7)

        # ADHAAR NO.

        lbl7 = Label(window, text="ADHAAR NO.", font=("bold", 12))
        lbl7.grid(column=1, row=8)
        lbl7.configure(background="light blue")

        def testVal(inStr, acttyp):
            if acttyp == '1':  # insert
                if not inStr.isdigit():
                    return False
            return True

        entry2 = Entry(window, width=20, textvar=Adhar_no, validate="key")
        entry2['validatecommand'] = (entry2.register(testVal), '%P', '%d')
        entry2.grid(column=2, row=8)

        # D.O.B

        lbl8 = Label(window, text="D.O.B", font=("bold", 12))
        lbl8.grid(column=1, row=9)
        lbl8.configure(background="light blue")

        txt5 = Entry(window, width=20, textvar=DOB)
        txt5.grid(column=2, row=9)

        lbl11 = Label(window, text="(DD/MM/YYYY)")
        lbl11.grid(column=3, row=9)
        lbl11.configure(background="light blue")

        # Phone no.

        lbl9 = Label(window, text="PHONE NO.", font=("bold", 12))
        lbl9.grid(column=1, row=10)
        lbl9.configure(background="light blue")

        def testVal(inStr, acttyp):
            if acttyp == '1':  # insert
                if not inStr.isdigit():
                    return False
            return True

        entry3 = Entry(window, width=20, textvar=Phone_no, validate="key")
        entry3['validatecommand'] = (entry3.register(testVal), '%P', '%d')
        entry3.grid(column=2, row=10)

        # PAN NO.

        lbl10 = Label(window, text="PAN NO.", font=("bold", 12))
        lbl10.grid(column=1, row=11)
        lbl10.configure(background="light blue")

        def testVal(inStr, acttyp):
            if acttyp == '1':  # insert
                if not inStr.isdigit():
                    return False
            return True

        entry4 = Entry(window, width=20, textvar=Pan_no, validate="key")
        entry4['validatecommand'] = (entry4.register(testVal), '%P', '%d')
        entry4.grid(column=2, row=11)

        # EMAIL ID

        lbl11 = Label(window, text="EMAIL ID", font=("bold", 12))
        lbl11.grid(column=1, row=12)
        lbl11.configure(background="light blue")
        txt6 = Entry(window, width=20, textvar=Email_id)
        txt6.grid(column=2, row=12)

        # ADDRESS

        lbl12 = Label(window, text="ADDRESS", font=("bold", 12))
        lbl12.grid(column=1, row=13)
        lbl12.configure(background="light blue")
        txt7 = Entry(window, width=20, textvar=Address)
        txt7.grid(column=2, row=13)

        # read form

        chk_state1 = BooleanVar()
        chk_state1.set(False)
        chk = Checkbutton(window, text='I agree to the Terms and Conditions', var=chk_state1)
        chk.grid(column=1, row=14)

        label = Label(window)
        label.grid(column=1, row=15)
        label.configure(background="light blue")

        lbl_text = Label(window)
        lbl_text.grid(column=1, row=15)

        # ADD ACCOUNT BUTTON

        addaccount = Button(window, text="ADD ACCOUNT", command=database)
        addaccount.grid(column=2, row=16)

    def New_transaction():
        window = Toplevel()

        window.title("ADD NEW TRANSACTION")
        window.configure(bg="light blue")
        window.geometry("430x250")

        Amount = StringVar()
        var = StringVar()
        c = StringVar()

        def database():
            amount = Amount.get()
            transaction_type = var.get()
            if var == "Deposite":
                'Deposite'
            else:
                'Withdraw'
            account_no = dropmenu.get()
            if Amount.get() == "":
                res = messagebox.askretrycancel('', 'Mandatory Data missing!!')
            else:

                conn = sqlite3.connect("Bank.db")
                with conn:
                    cursor = conn.cursor()
                cursor.execute(
                    'CREATE TABLE IF NOT EXISTS ADD_NEW_TRANSACTION (Account_no TEXT, Transaction_type TEXT, '
                    'Amount TEXT)')
                cursor.execute(
                    'INSERT INTO ADD_NEW_TRANSACTION (Account_no, Transaction_type, Amount) VALUES(?,?,?)',
                    (account_no, transaction_type, amount))
                conn.commit()

        def Verify():

            database()
            Database()
            if Name.get() == "" or Name1.get() == "":
                res = messagebox.askretrycancel('', 'Mandatory Data missing!!')
            else:
                cursor.execute("SELECT * FROM `Register` WHERE `Name` = ? AND `Name1` = ?",
                               (Name.get(), Name1.get()))

                if cursor.fetchone() is not None:
                    Name.set("")
                    Name1.set("")
                    Amount.set("")
                    var.set("")
                    c.set("")
                    lbl_text.config(text="")
                    res = messagebox.askokcancel('', 'Transaction succesfully')
                    window.withdraw()

                else:
                    lbl_text.config(text="Invalid father middle name or secret code")
                    Name.set("")
                    Name1.set("")

            cursor.close()
            conn.close()

        lbl = Label(window, text="Account_no.", font=("blue", 12))
        lbl.configure(background="light blue")
        lbl.grid(column=0, row=0)

        def combo_Account_no():
            conn = sqlite3.connect("Bank.db")
            cursor = conn.cursor()
            cursor.execute('SELECT Account_no FROM ADD_ACCOUNT')
            data = []
            for row in cursor.fetchall():
                data.append(row[0])
            return data

        rows = 0
        while rows < 50:
            window.rowconfigure(rows, weight=1)
            window.columnconfigure(rows, weight=1)
            rows += 1

        dropmenu = ttk.Combobox(window)
        dropmenu['values'] = combo_Account_no()
        dropmenu.bind('<<ComboboxSelected>>')
        dropmenu.set('')
        dropmenu.grid(row=0, column=1, sticky='NESW')

        # Account type

        Name = StringVar()
        lbl4 = Label(window, text="Transaction_type",font=("blue", 12))
        lbl4.grid(column=0, row=3)
        lbl4.configure(background="light blue")

        rad1 = Radiobutton(window, text="Deposite", value='Deposite', variable=var)

        rad2 = Radiobutton(window, text="Withdraw", value='Withdraw', variable=var)

        rad1.grid(column=1, row=3)
        rad2.grid(column=2, row=3)

        lb5 = Label(window, text="Amount", font=("blue", 12))
        lb5.grid(column=0, row=4)
        lb5.configure(background="light blue")

        def testVal(inStr, acttyp):
            if acttyp == '1':  # insert
                if not inStr.isdigit():
                    return False
            return True

        entry = Entry(window, width=20, textvar=Amount, validate="key")
        entry['validatecommand'] = (entry.register(testVal), '%P', '%d')
        entry.grid(column=1, row=4)

        # read form

        chk_state1 = BooleanVar()
        chk_state1.set(False)
        chk = Checkbutton(window, text='I agree to the Terms and Conditions', var=chk_state1)
        chk.grid(column=1, row=9)

        # ADD NEW TRANSACTION BUTTON

        addnewtransaction = Button(window, text="ADD TRANSACTION", command=Verify)
        addnewtransaction.grid(column=1, row=10)

        def Database():
            global conn, cursor
            conn = sqlite3.connect("Bank.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `Register` WHERE Name = '?' AND Name1 = '?' ")
            conn.commit()

        Name = StringVar()
        Name1 = StringVar()

        lbl5 = Label(window, text="Security Question*", font=("blue", 15))
        lbl5.grid(column=1, row=5)
        lbl5.configure(background="light blue")

        Name = StringVar()
        lbl2 = Label(window, text="father middle name", font=("blue", 12))
        lbl2.grid(column=0, row=6)
        lbl2.configure(background="light blue")
        entry1 = Entry(window, textvar=Name)
        entry1.grid(column=1, row=6)

        Name1 = StringVar()
        lbl3 = Label(window, text="Secret Code", font=("blue", 12))
        lbl3.grid(column=0, row=7)
        lbl3.configure(background="light blue")
        entry2 = Entry(window, textvar=Name1)
        entry2.grid(column=1, row=7)

        lbl_text = Label(window)
        lbl_text.grid(column=1, row=8)
        lbl_text.configure(background="light blue")

    def delete():
        root = Toplevel()
        root.configure(bg="light blue")
        root.title("Delete Account")
        Account_no = StringVar()
        Bank_name = StringVar()

        def database():
            global conn, cursor
            if Account_no.get() == "" or Bank_name.get() == "":
                messagebox.showinfo('Error')
            else:
                conn = sqlite3.connect("Bank.db")
                with conn:
                    cursor = conn.cursor()
                    sql = "DELETE FROM ADD_ACCOUNT WHERE Account_no= '%s'" \
                          % (Account_no.get())
                    cursor.execute(sql)
                    conn.commit()

                    messagebox.showinfo('Record Deleted')
                    root.withdraw()

        def search():
            try:
                e2.configure(state='disabled')
                conn = sqlite3.connect("Bank.db")
                with conn:
                    cursor = conn.cursor()
                    sql = "SELECT * FROM ADD_ACCOUNT WHERE Account_no= '%s'" % Account_no.get()
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    Bank_name.set((result[1]))
                    conn.commit()
            except:
                messagebox.showinfo('No Data')

        l1 = Label(root, text="Account_no", font=("blue", 12))
        l1.grid(row=0, column=1)
        l2 = Label(root, text="Bank_name", font=("blue", 12))
        l2.grid(row=0, column=2)
        e1 = Entry(root, textvar=Account_no)
        e1.grid(row=1, column=1)
        e2 = Entry(root, textvar=Bank_name)
        e2.grid(row=1, column=2)
        e2.configure(state='disabled')

        btn = Button(root, text="delete", command=database)
        btn.grid(row=2, column=1)
        btn = Button(root, text="search", command=search)
        btn.grid(row=2, column=2)

    def show():
        window = Toplevel()
        window.geometry("200x200")
        window.configure(bg="light blue")
        window.title("INFORMATION")

        def show1():
            global root1
            root1 = Toplevel()
            root1.geometry("200x200")
            root1.configure(bg="light blue")
            root1.title("Display Data")
            window.withdraw()

            def Show():
                con = sqlite3.connect("Bank.db")
                cur = con.cursor()
                cursor = cur.execute("SELECT * FROM ADD_ACCOUNT")
                sys.stdout = open("Accounts.txt", "w")
                for row in cursor:
                    print("-------------AVAILABLE ACCOUNTS--------------")
                    print("Holder_name= ", row[0])
                    print("Bank_name= ", row[1])
                    print("Branch= ", row[2])
                    print("Account_no= ", row[3])
                    print("Account_type= ", row[4])
                    print("Costumer_id= ", row[5])
                    print("Ifsc= ", row[6])
                    print("Adhar_no= ", row[7])
                    print("DOB= ", row[8])
                    print("Phone_no= ", row[9])
                    print("Pan_no= ", row[10])
                    print("Email= ", row[11])
                    print("Address= ", row[12], "\n")
                    sys.stdout.close()
                    root1.withdraw()
                con.close()

            btn = Button(root1, text="Show", command=Show)
            btn.grid(pady=25, row=2, columnspan=3)

        btn = Button(window, text="AVAILABLE ACCOUNT", command=show1)
        btn.grid(pady=25, row=2, columnspan=3)

        def show2():
            global root
            root = Toplevel()
            root.geometry("200x200")
            root.configure(bg="light blue")
            root.title("Display Data")
            window.withdraw()

            def Show():
                conn = sqlite3.connect("Bank.db")
                cur = con.cursor()
                cursor = cur.execute("SELECT * FROM ADD_NEW_TRANSACTION")
                for row in cursor:
                    print("-----------RECENT TRANSACTION--------------")
                    print("Account_no= ", row[0])
                    print("Transaction_type= ", row[1])
                    print("Amount= ", row[2], "\n")
                    root.withdraw()
                con.close()

            btn = Button(root, text="Show", command=Show)
            btn.grid(pady=25, row=2, columnspan=3)

        btn = Button(window, text="RECENT TRANSACTION", command=show2)
        btn.grid(pady=25, row=5, columnspan=3)


def Back():
    REGISTER.destroy()
    root.deiconify()


def Register():
    root = Toplevel()
    root.title("Registration Form")
    root.config(bg="light blue")

    Fullname = StringVar()
    Email = StringVar()
    Password = StringVar()
    Username = StringVar()
    Adhar_no = StringVar()
    var = StringVar()
    State = StringVar()
    City = StringVar()
    Name = StringVar()
    Name1 = StringVar()

    def database():
        name2 = Fullname.get()
        email = Email.get()
        password = Password.get()
        username = Username.get()
        adhar_no = Adhar_no.get()
        name = Name.get()
        name1 = Name1.get()

        gender = var.get()
        if var == "Male":
            'Male'
        else:
            'Female'
        state = State.get()
        city = City.get()

        if Fullname.get() == "" or Email.get() == "" or Username.get() == "" or Password.get() == "" or Name.get() == "" or Name1.get() == "" or Adhar_no.get() == "" or var.get() == "" or State.get() == "" or City.get() == "":
            res = messagebox.askretrycancel('Ask_RetryCancel', 'Mandatory Data missing!!')
        else:

            conn = sqlite3.connect("Bank.db")
            with conn:
                cursor = conn.cursor()
            cursor.execute(
                'CREATE TABLE IF NOT EXISTS Register (Fullname TEXT, Email TEXT, Username TEXT, Password varchar, '
                'Name TEXT, Name1 TEXT, Adhar_no TEXT, Gender TEXT, State TEXT, City TEXT)')
            cursor.execute(
                'INSERT INTO Register (Fullname, Email, Username, Password, Name , Name1, Adhar_no, Gender, State, '
                'City) VALUES( '
                '?,?,?,?,?,?,?,?,?,?)',
                (name2, email, username, password, name, name1, adhar_no, gender, state, city))
            res = messagebox.askokcancel('Ask_OKCancel', 'Register succesfully')

            conn.commit()
            root.withdraw()

    label_0 = Label(root, text="Registration form", width=20, font=("blue", 30))
    label_0.grid(column=1, row=0)
    label_0.configure(background="light blue")

    label_1 = Label(root, text="FullName", width=20, font=("blue", 15))
    label_1.grid(column=0, row=1)
    label_1.configure(background="light blue")

    entry1 = Entry(root, textvar=Fullname)
    entry1.grid(column=1, row=1)
    entry1.configure(background="light blue")

    label_2 = Label(root, text="Email", width=20, font=("bold", 15))
    label_2.grid(column=0, row=2)
    label_2.configure(background="light blue")

    entry2 = Entry(root, textvar=Email)
    entry2.grid(column=1, row=2)

    label_3 = Label(root, text="Gender", width=20, font=("bold", 15))
    label_3.grid(column=0, row=4)
    label_3.configure(background="light blue")

    Radiobutton(root, text="Male", variable=var, value="Male").grid(column=1, row=4)
    Radiobutton(root, text="Female", variable=var, value="Female").grid(column=1, row=5)

    label_4 = Label(root, text="state", width=20, font=("bold", 15))
    label_4.grid(column=0, row=7)
    label_4.configure(background="light blue")

    list1 = ["Andra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhan", "Karnataka", "Kerala", "MadyaPradesh", "Maharashtra",
             "Manipur",
             "Meghalaya", "Mizoram", "Nagaland", "Orissa", "Punjab", "Rajasthan", "Sikki", "Tamil Nadu", "Telagana",
             "Tripura",
             "Uttaranchal", "Uttar Pradesh", "West Bengal", "Andaman and Nicobar Island", "Chandigarh",
             "Dadar and Nagar Haveli",
             "Daman and Diu", "Delhi", "Lakshadeep", "Pondicherry"]


    droplist = OptionMenu(root, State, *list1)
    droplist.config(width=15)
    State.set('')
    droplist.grid(column=1, row=7)

    label_4 = Label(root, text="Username", width=20, font=("bold", 15))
    label_4.grid(column=0, row=8)
    label_4.configure(background="light blue")
    entry3 = Entry(root, textvar=Username)
    entry3.grid(column=1, row=8)

    label_5 = Label(root, text="Password", width=20, font=("bold", 15))
    label_5.grid(column=0, row=9)
    label_5.configure(background="light blue")
    entry4 = Entry(root, textvar=Password, show='*')
    entry4.grid(column=1, row=9)

    label_6 = Label(root, text="Adhar_no", width=20, font=("bold", 15))
    label_6.grid(column=0, row=10)
    label_6.configure(background="light blue")

    def testVal(inStr, acttyp):
        if acttyp == '1':  # insert
            if not inStr.isdigit():
                return False
        return True

    entry5 = Entry(root, width=20, textvar=Adhar_no, validate="key")
    entry5['validatecommand'] = (entry5.register(testVal), '%P', '%d')
    entry5.grid(column=1, row=10)

    label_4 = Label(root, text="city", width=20, font=("bold", 15))
    label_4.grid(column=0, row=12)
    label_4.configure(background="light blue")

    list2 = ["Ahmadabad", "Ahmadnagar", "Bhuj", "Bhusawal","Chandrapur", "Dalhousie",
             "Dharmshala","Faridabad" , "Firozpur", "Guwahati", "Hamirpur","Jalgaon"
, "Kangra", "Kullu", "Mandi", "Nahan","Nashik","Parbhani", "Pune","Ratnagiri","Shimla", "Thane","Ulhasnagar","VasaiVirar","Wardha", "Yavatmal"]

    droplist = OptionMenu(root, City, *list2)
    droplist.config(width=15)
    City.set('')
    droplist.grid(column=1, row=12)

    label_8 = Label(root, text="Security Question:what is your father middle name?", width=44, font=("bold", 15))
    label_8.grid(row=13, column=0)
    label_8.configure(background="light blue")
    entry6 = Entry(root, textvar=Name)
    entry6.grid(row=13, column=1)

    label_8 = Label(root, text="Security Question:what is your secret code?", width=40, font=("bold", 15))
    label_8.grid(row=14, column=0)
    label_8.configure(background="light blue")
    entry7 = Entry(root, textvar=Name1, show='*')
    entry7.grid(row=14, column=1)

    btn=Button(root, text='Register', width=40, command=database)
    btn.grid(column=1, row=18)




# ==============================VARIABLES======================================
Username = StringVar()
Password = StringVar()

# ==============================FRAMES=========================================
Top = Frame(root, relief=RIDGE)
Top.pack(side=TOP, fill=X)
Form = Frame(root, height=200)
Form.pack(side=TOP, pady=20)
# ==============================LABELS=========================================
lbl_title = Label(Top, text="Login", font=('arial', 15))
lbl_title.pack(anchor=N)
lbl_username = Label(Form, text="Username:", font=('arial', 14))
lbl_username.grid(row=0, sticky="e")
lbl_password = Label(Form, text="Password:", font=('arial', 14))
lbl_password.grid(row=1, sticky="e")
lbl_text = Label(Form)
lbl_text.grid(row=2, columnspan=2)

# ==============================ENTRY WIDGETS==================================
username = Entry(Form, textvariable=Username, font=14)
username.grid(row=0, column=1)
password = Entry(Form, textvariable=Password, show="*", font=14)
password.grid(row=1, column=1)

# ==============================BUTTON WIDGETS=================================
btn_login = Button(Form, text="Login", width=45, command=Login)
btn_login.grid(pady=25, row=3, columnspan=2)
btn_login.bind('<Return>', Login)

btn_Register = Button(Form, text="Register", width=45, command=Register)
btn_Register.grid(pady=25, row=5, columnspan=2)

root.mainloop()
