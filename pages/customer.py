from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # pip install pillow
import random
import mysql.connector


class CustomerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Information")
        self.root.geometry("1295x550+240+240")
        self.root.configure(background="linen")
        root.resizable(width=True, height=True)
        # ===============variables================
        self.varID = StringVar()
        x = random.randint(1000, 9999)
        self.varID.set(str(x))

        self.varFirstName = StringVar()
        self.varLastName = StringVar()
        self.varGender = StringVar()
        self.varPostcode = StringVar()
        self.varPhone = StringVar()
        self.varEmail = StringVar()
        self.varNationality = StringVar()
        self.varIDProof = StringVar()
        self.varIDNumber = StringVar()
        self.varAddress = StringVar()

        # ===============title====================
        lblTitle = Label(
            self.root,
            text="ADD CUSTOMER DETAILS",
            font=("Microsoft Sans Serif", 20, "bold"),
            bg="black",
            fg="bisque",
            bd=4,
            relief=RIDGE,
        )
        lblTitle.place(x=0, y=0, width=1295, height=50)

        # ================Label Frame=============
        customerInfoInputFrame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Customer Details",
            font=("Microsoft Sans Serif", 12, "bold"),
            padx=2,
            bg="linen",
        )
        customerInfoInputFrame.place(x=5, y=50, width=420, height=490)

        # ==============input details==============
        # ID

        lblCustomerID = Label(
            customerInfoInputFrame,
            text="Customer ID",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblCustomerID.grid(row=0, column=0, sticky=W)

        entryCustomerID = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varID,
            width=30,
            font=("Microsoft Sans Serif", 12),
            state="readonly",
        )
        entryCustomerID.grid(row=0, column=1)

        # FirstName
        lblFirstName = Label(
            customerInfoInputFrame,
            text="First Name",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblFirstName.grid(row=1, column=0, sticky=W)

        entryFirstName = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varFirstName,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryFirstName.grid(row=1, column=1)

        # Last Name
        lblLastName = Label(
            customerInfoInputFrame,
            text="Last Name",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblLastName.grid(row=2, column=0, sticky=W)

        entryLastName = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varLastName,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryLastName.grid(row=2, column=1)

        # Gender
        lblGender = Label(
            customerInfoInputFrame,
            text="Gender",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblGender.grid(row=3, column=0, sticky=W)

        cbxGender = ttk.Combobox(
            customerInfoInputFrame,
            textvariable=self.varGender,
            width=28,
            font=("Microsoft Sans Serif", 12),
            state="readonly",
        )
        cbxGender["value"] = ("Male", "Female", "Other")
        cbxGender.current(0)
        cbxGender.grid(row=3, column=1)

        # Postcode
        lblPostcode = Label(
            customerInfoInputFrame,
            text="Postcode",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblPostcode.grid(row=4, column=0, sticky=W)

        entryPostcode = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varPostcode,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryPostcode.grid(row=4, column=1)

        # Mobile
        lblMobile = Label(
            customerInfoInputFrame,
            text="Mobile",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblMobile.grid(row=5, column=0, sticky=W)

        entryMobile = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varPhone,
            width=30,
            font=("Microsoft Sans Serif", 12),
            validate="key",
            validatecommand=(root.register(self.validate_input), "%P"),
        )
        entryMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(
            customerInfoInputFrame,
            text="Email",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblEmail.grid(row=6, column=0, sticky=W)

        entryEmail = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varEmail,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(
            customerInfoInputFrame,
            text="Nationality",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblNationality.grid(row=7, column=0, sticky=W)

        entryNationality = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varNationality,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryNationality.grid(row=7, column=1)

        # ID Proof Type
        lblIDProofType = Label(
            customerInfoInputFrame,
            text="ID Proof Type",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblIDProofType.grid(row=8, column=0, sticky=W)

        cbxIDProofType = ttk.Combobox(
            customerInfoInputFrame,
            textvariable=self.varIDProof,
            width=28,
            font=("Microsoft Sans Serif", 12),
        )
        cbxIDProofType["value"] = ("CitizenID", "Passport", "Other")
        cbxIDProofType.current(0)
        cbxIDProofType.grid(row=8, column=1)

        # ID Number
        lblIDNumber = Label(
            customerInfoInputFrame,
            text="ID Number",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblIDNumber.grid(row=9, column=0, sticky=W)

        entryIDNumber = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varIDNumber,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryIDNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(
            customerInfoInputFrame,
            text="Address",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblAddress.grid(row=10, column=0, sticky=W)

        entryAddress = ttk.Entry(
            customerInfoInputFrame,
            textvariable=self.varAddress,
            width=30,
            font=("Microsoft Sans Serif", 12),
        )
        entryAddress.grid(row=10, column=1)

        # =================Buttons funcs================
        btnFrame = Frame(customerInfoInputFrame, bd=2, relief=RIDGE)
        btnFrame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(
            btnFrame,
            text="Add",
            command=self.AddData,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(
            btnFrame,
            text="Update",
            command=self.Update,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(
            btnFrame,
            text="Delete",
            command=self.Delete,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(
            btnFrame,
            text="Reset",
            command=self.Reset,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnReset.grid(row=0, column=3, padx=1)
        # =================table frame searching=========================
        tableFrame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="View Details And Search",
            font=("Microsoft Sans Serif", 12, "bold"),
            padx=2,
            bg="linen",
        )
        tableFrame.place(x=435, y=50, width=860, height=490)

        lblSearch = Label(
            tableFrame, font=("Microsoft Sans Serif", 12), text="Search By:", bg="linen"
        )
        lblSearch.grid(row=0, column=0, sticky=W, padx=2)

        self.searchVar = StringVar()
        cbbSearchOptions = ttk.Combobox(
            tableFrame,
            textvariable=self.searchVar,
            font=("Microsoft Sans Serif", 12),
            width=24,
            state="readonly",
        )
        cbbSearchOptions["value"] = ("Mobile", "customerID")
        cbbSearchOptions.current(0)
        cbbSearchOptions.grid(row=0, column=1, padx=2)

        self.txtSearch = StringVar()
        txtSearch = ttk.Entry(
            tableFrame,
            textvariable=self.txtSearch,
            font=("Microsoft Sans Serif", 12),
            width=32,
        )
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(
            tableFrame,
            command=self.Search,
            font=("Microsoft Sans Serif", 12),
            text="Search",
            bg="linen",
            width=10,
        )
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(
            tableFrame,
            command=self.fetchData,
            font=("Microsoft Sans Serif", 12),
            text="Show All",
            bg="linen",
            width=10,
        )
        btnShowAll.grid(row=0, column=4, padx=2)

        # =================show data table=========================

        detailsTable = Frame(tableFrame, bd=2, relief=RIDGE)
        detailsTable.place(x=0, y=50, width=845, height=350)

        scrollX = ttk.Scrollbar(detailsTable, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(detailsTable, orient=VERTICAL)

        self.CustomerDetailsTable = ttk.Treeview(
            detailsTable,
            columns=(
                "id",
                "firstName",
                "lastName",
                "gender",
                "postcode",
                "phone",
                "email",
                "nationality",
                "idProof",
                "idNumber",
                "address",
            ),
            xscrollcommand=scrollX.set,
            yscrollcommand=scrollY.set,
        )

        scrollXFrame = ttk.Frame(detailsTable)
        scrollYFrame = ttk.Frame(detailsTable)
        scrollX = ttk.Scrollbar(
            scrollXFrame,
            orient=HORIZONTAL,
            command=self.CustomerDetailsTable.xview,
        )
        scrollY = ttk.Scrollbar(
            scrollYFrame,
            orient=VERTICAL,
            command=self.CustomerDetailsTable.yview,
        )

        scrollXFrame.pack(side=BOTTOM, fill=X)
        scrollYFrame.pack(side=RIGHT, fill=Y)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        self.CustomerDetailsTable.heading("id", text="ID")
        self.CustomerDetailsTable.heading("firstName", text="FirstName")
        self.CustomerDetailsTable.heading("lastName", text="LastName")
        self.CustomerDetailsTable.heading("gender", text="Gender")
        self.CustomerDetailsTable.heading("postcode", text="Postcode")
        self.CustomerDetailsTable.heading("phone", text="Phone")
        self.CustomerDetailsTable.heading("email", text="Email")
        self.CustomerDetailsTable.heading("nationality", text="Nationality")
        self.CustomerDetailsTable.heading("idProof", text="IDProof")
        self.CustomerDetailsTable.heading("idNumber", text="IDNumber")
        self.CustomerDetailsTable.heading("address", text="Address")

        self.CustomerDetailsTable["show"] = "headings"

        self.CustomerDetailsTable.column("id", width=100)
        self.CustomerDetailsTable.column("firstName", width=100)
        self.CustomerDetailsTable.column("lastName", width=100)
        self.CustomerDetailsTable.column("gender", width=100)
        self.CustomerDetailsTable.column("postcode", width=100)
        self.CustomerDetailsTable.column("phone", width=100)
        self.CustomerDetailsTable.column("email", width=100)
        self.CustomerDetailsTable.column("nationality", width=100)
        self.CustomerDetailsTable.column("idProof", width=100)
        self.CustomerDetailsTable.column("idNumber", width=100)
        self.CustomerDetailsTable.column("address", width=100)

        self.CustomerDetailsTable.pack(fill=BOTH, expand=1)
        self.CustomerDetailsTable.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchData()

    def validate_input(self, new_value):
        return new_value.isdigit() and not new_value.startswith("00")
        # =======================Database connecton===============

    def AddData(self):
        if self.varPhone.get() == "" or self.varLastName.get() == "":
            messagebox.showerror("Error")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                myCursor.execute(
                    "insert into customer value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.varID.get(),
                        self.varFirstName.get(),
                        self.varLastName.get(),
                        self.varGender.get(),
                        self.varPostcode.get(),
                        self.varPhone.get(),
                        self.varEmail.get(),
                        self.varNationality.get(),
                        self.varIDProof.get(),
                        self.varIDNumber.get(),
                        self.varAddress.get(),
                    ),
                )
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo(
                    "success", "customer has been added", parent=self.root
                )
            except Exception as es:
                messagebox.showwarning(
                    "waring", f"Some thing went wrong:{str(es)}", parent=self.root
                )

    def fetchData(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="130806080525",
            database="hotelmanagementsystem",
        )
        myCursor = conn.cursor()
        myCursor.execute("select * from customer")
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.CustomerDetailsTable.delete(*self.CustomerDetailsTable.get_children())
            for i in rows:
                self.CustomerDetailsTable.insert("", END, text=i, values=i)
            conn.commit()
        conn.close()

        # =========get cursor on the info lines==================

    def getCursor(self, event=""):
        cursorRow = self.CustomerDetailsTable.focus()
        content = self.CustomerDetailsTable.item(cursorRow)
        row = content["text"].split(" ")

        self.varID.set(row[0]),
        self.varFirstName.set(row[1]),
        self.varLastName.set(row[2]),
        self.varGender.set(row[3]),
        self.varPostcode.set(row[4]),
        self.varPhone.set(row[5]),
        self.varEmail.set(row[6]),
        self.varNationality.set(row[7]),
        self.varIDProof.set(row[8]),
        self.varIDNumber.set(row[9]),
        self.varAddress.set(row[10])

    def Update(self):
        if self.varPhone.get() == "":
            messagebox.showerror(
                "Error", "Please enter mobile number", parent=self.root
            )
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                update_query = """
                UPDATE customer
                SET firstName=%s, lastName=%s, gender=%s, postcode=%s, mobile=%s, email=%s,
                nationality=%s, IDProofType=%s, IDNumber=%s, Address=%s
                WHERE customerID=%s
            """

                update_data = (
                    self.varFirstName.get(),
                    self.varLastName.get(),
                    self.varGender.get(),
                    self.varPostcode.get(),
                    self.varPhone.get(),
                    self.varEmail.get(),
                    self.varNationality.get(),
                    self.varIDProof.get(),
                    self.varIDNumber.get(),
                    self.varAddress.get(),
                    self.varID.get(),
                )

                myCursor.execute(update_query, update_data)
                conn.commit()

                self.fetchData()
                conn.close()
                messagebox.showinfo(
                    "Update",
                    "Customer details have been updated successfully",
                    parent=self.root,
                )
            except Exception as e:
                messagebox.showerror(
                    "Error", f"An error occurred: {str(e)}", parent=self.root
                )

    def Delete(self):
        Delete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this?", parent=self.root
        )
        if Delete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="130806080525",
                database="hotelmanagementsystem",
            )
            myCursor = conn.cursor()
            query = "delete from customer where customerID=%s"
            value = (self.varID.get(),)
            myCursor.execute(query, value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetchData()
        conn.close()

    def Reset(self):
        # self.varID.set(""),
        x = random.randint(1000, 9999)
        self.varID.set(str(x)),
        self.varFirstName.set(""),
        self.varLastName.set(""),
        # self.varGender.set(""),
        self.varPostcode.set(""),
        self.varPhone.set(""),
        self.varEmail.set(""),
        self.varNationality.set(""),
        # self.varIDProof.set(""),
        self.varIDNumber.set(""),
        self.varAddress.set("")

    def Search(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="130806080525",
            database="hotelmanagementsystem",
        )
        myCursor = conn.cursor()
        myCursor.execute(
            "select * from customer where "
            + str(self.searchVar.get())
            + " LIKE '%"
            + str(self.txtSearch.get())
            + "%'"
        )
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.CustomerDetailsTable.delete(*self.CustomerDetailsTable.get_children())
            for i in rows:
                self.CustomerDetailsTable.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CustomerWindow(root)
    root.mainloop()
