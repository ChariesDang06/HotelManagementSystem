from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # pip install pillow
import random
import mysql.connector
from time import strftime
from datetime import datetime
from tkcalendar import Calendar


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Booking")
        self.root.geometry("1295x550+240+240")
        self.root.configure(background="linen")
        root.resizable(width=True, height=True)

        # Variables============
        self.varContact = StringVar()
        self.varCheckIn = StringVar()
        self.varCheckOut = StringVar()
        self.varRoomType = StringVar()
        self.varRoomDescribe = StringVar()
        self.varRoom = StringVar()
        self.varMeal = StringVar()
        self.varNumOfDays = StringVar()
        self.varPaidTax = StringVar()
        self.varSubTotal = StringVar()
        self.varTotalCost = StringVar()

        # titile==============
        lblTitle = Label(
            self.root,
            text="ROOMBOOKING DETAILS",
            font=("Microsoft Sans Serif", 18, "bold"),
            bg="black",
            fg="bisque",
            bd=4,
            relief=RIDGE,
        )
        lblTitle.place(x=0, y=0, width=1295, height=50)

        # details label===================
        labelDetailsFrame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Room booking Details",
            font=("Microsoft Sans Serif", 12, "bold"),
            bg="linen",
            padx=2,
        )
        labelDetailsFrame.place(x=5, y=50, width=425, height=490)

        # lables and entry===============
        # customer contact
        lblCustomerContact = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Customer Contact",
            bg="linen",
        )
        lblCustomerContact.grid(row=0, column=0, sticky=W)

        # vcmd = (self.root.register(validate_input), '%P')
        entryContact = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varContact,
            font=("Microsoft Sans Serif", 12),
            width=17,
            validate="key",
            validatecommand=(self.root.register(self.validate_input), "%P"),
        )
        entryContact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        btnFetchData = Button(
            labelDetailsFrame,
            text="Fetch Data",
            command=self.FetchContact,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnFetchData.place(x=300, y=0)

        # Check_in Date
        checkInDate = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Check-in date",
            bg="linen",
            padx=2,
            pady=4,
        )
        checkInDate.grid(row=1, column=0, sticky=W)
        txtCheckInDate = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varCheckIn,
            font=("Microsoft Sans Serif", 12),
            width=29,
        )
        txtCheckInDate.grid(row=1, column=1)

        # Check_out Date
        checkOutDate = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Check-out date",
            bg="linen",
            padx=2,
            pady=4,
        )
        checkOutDate.grid(row=2, column=0, sticky=W)
        txtCheckOutDate = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varCheckOut,
            font=("Microsoft Sans Serif", 12),
            width=29,
        )
        txtCheckOutDate.grid(row=2, column=1)

        # Room Type
        lblRoomType = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Room Type",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblRoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="130806080525",
            database="hotelmanagementsystem",
        )
        myCursor = conn.cursor()
        myCursor.execute("select room_type from room_manage")
        roomTypeRows = myCursor.fetchall()

        cbbRoomType = ttk.Combobox(
            labelDetailsFrame,
            textvariable=self.varRoomType,
            font=("Microsoft Sans Serif", 12),
            width=27,
            state="readonly",
        )
        cbbRoomType["value"] = roomTypeRows
        cbbRoomType.current(0)
        cbbRoomType.grid(row=3, column=1)

        # Available room
        lblAvailableRoom = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Avialable Room",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblAvailableRoom.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="130806080525",
            database="hotelmanagementsystem",
        )
        myCursor = conn.cursor()
        myCursor.execute("select room_number from room_manage")
        roomNumberRows = myCursor.fetchall()

        cbbRoomNumber = ttk.Combobox(
            labelDetailsFrame,
            textvariable=self.varRoom,
            font=("Microsoft Sans Serif", 12),
            width=27,
            state="readonly",
        )
        cbbRoomNumber["value"] = roomNumberRows
        cbbRoomNumber.current(0)
        cbbRoomNumber.grid(row=4, column=1)

        # Room Describe
        lblRoomDescribe = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Room Describe",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblRoomDescribe.grid(row=5, column=0, sticky=W)

        txtRoomDescribe = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varRoomDescribe,
            font=("Microsoft Sans Serif", 12),
            width=29,
            state="readonly",
        )
        txtRoomDescribe.grid(row=5, column=1)

        # Meal
        lblMeal = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Meal",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblMeal.grid(row=6, column=0, sticky=W)

        cbbMeal = ttk.Combobox(
            labelDetailsFrame,
            textvariable=self.varMeal,
            font=("Microsoft Sans Serif", 12),
            width=27,
            state="readonly",
        )
        cbbMeal["value"] = ("Breakfast", "Lunch", "Dinner")
        cbbMeal.current(0)
        cbbMeal.grid(row=6, column=1)

        # Number of days
        lblNoOfDays = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="No Of Days",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblNoOfDays.grid(row=7, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varNumOfDays,
            font=("Microsoft Sans Serif", 12),
            width=29,
        )
        txtNoOfDays.grid(row=7, column=1)

        # Paid tax
        lblTax = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Paid Tax",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblTax.grid(row=8, column=0, sticky=W)

        txtTax = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varPaidTax,
            font=("Microsoft Sans Serif", 12),
            width=29,
        )
        txtTax.grid(row=8, column=1)

        # Sub Total
        lblSubTotal = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Sub Total",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblSubTotal.grid(row=9, column=0, sticky=W)

        txtSubTotal = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varSubTotal,
            font=("Microsoft Sans Serif", 12),
            width=29,
        )
        txtSubTotal.grid(row=9, column=1)

        # Total Cost
        lblTotalCost = Label(
            labelDetailsFrame,
            font=("Microsoft Sans Serif", 12),
            text="Total Cost",
            bg="linen",
            padx=2,
            pady=6,
        )
        lblTotalCost.grid(row=10, column=0, sticky=W)

        txtTotalCost = ttk.Entry(
            labelDetailsFrame,
            textvariable=self.varTotalCost,
            font=("Microsoft Sans Serif", 12),
            width=29,
        )
        txtTotalCost.grid(row=10, column=1)

        # Buttons
        btnBill = Button(
            labelDetailsFrame,
            text="Bill",
            command=self.Total,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnBill.grid(row=11, column=1, pady=1, sticky=E)

        btnFrame = Frame(labelDetailsFrame, bd=2, relief=RIDGE)
        btnFrame.place(x=0, y=420, width=412, height=40)

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

        # =====Fetch data=====
        exampleRoom = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\room1.png"
        )
        exampleRoom = exampleRoom.resize((520, 300), Image.LANCZOS)
        self.photoExampleRoom = ImageTk.PhotoImage(exampleRoom)

        lblimg1 = Label(self.root, image=self.photoExampleRoom, bd=4, relief=RIDGE)
        lblimg1.place(x=760, y=55, width=520, height=300)

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
        tableFrame.place(x=435, y=280, width=860, height=260)

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
        cbbSearchOptions["value"] = ("Contact", "Room")
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
        detailsTable.place(x=0, y=50, width=845, height=180)

        scrollX = ttk.Scrollbar(detailsTable, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(detailsTable, orient=VERTICAL)

        self.RoomBookingDetailsTable = ttk.Treeview(
            detailsTable,
            columns=(
                "contact",
                "checkIn",
                "checkOut",
                "roomType",
                "roomDescribe",
                "room",
                "meal",
                "numOfDays",
                "paidTax",
                "subTotal",
                "totalCost",
            ),
            xscrollcommand=scrollX.set,
            yscrollcommand=scrollY.set,
        )

        scrollXFrame = ttk.Frame(detailsTable)
        scrollYFrame = ttk.Frame(detailsTable)
        scrollX = ttk.Scrollbar(
            scrollXFrame,
            orient=HORIZONTAL,
            command=self.RoomBookingDetailsTable.xview,
        )
        scrollY = ttk.Scrollbar(
            scrollYFrame,
            orient=VERTICAL,
            command=self.RoomBookingDetailsTable.yview,
        )

        scrollXFrame.pack(side=BOTTOM, fill=X)
        scrollYFrame.pack(side=RIGHT, fill=Y)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        self.RoomBookingDetailsTable.heading("contact", text="Contact")
        self.RoomBookingDetailsTable.heading("checkIn", text="Check-in")
        self.RoomBookingDetailsTable.heading("checkOut", text="Check-out")
        self.RoomBookingDetailsTable.heading("roomType", text="Room Type")
        self.RoomBookingDetailsTable.heading("roomDescribe", text="Room Describe")
        self.RoomBookingDetailsTable.heading("room", text="Room")
        self.RoomBookingDetailsTable.heading("meal", text="Meal")
        self.RoomBookingDetailsTable.heading("numOfDays", text="Num Of Days")
        self.RoomBookingDetailsTable.heading("paidTax", text="Paid Tax")
        self.RoomBookingDetailsTable.heading("subTotal", text="Sub Total")
        self.RoomBookingDetailsTable.heading("totalCost", text="Total Cost")

        self.RoomBookingDetailsTable["show"] = "headings"

        self.RoomBookingDetailsTable.column("contact", width=100)
        self.RoomBookingDetailsTable.column("checkIn", width=100)
        self.RoomBookingDetailsTable.column("checkOut", width=100)
        self.RoomBookingDetailsTable.column("roomType", width=100)
        self.RoomBookingDetailsTable.column("roomDescribe", width=300)
        self.RoomBookingDetailsTable.column("room", width=100)
        self.RoomBookingDetailsTable.column("meal", width=100)
        self.RoomBookingDetailsTable.column("numOfDays", width=100)
        self.RoomBookingDetailsTable.column("paidTax", width=100)
        self.RoomBookingDetailsTable.column("subTotal", width=100)
        self.RoomBookingDetailsTable.column("totalCost", width=100)

        self.RoomBookingDetailsTable.pack(fill=BOTH, expand=1)
        self.RoomBookingDetailsTable.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchData()

    def validate_input(self, P):
        if P == "" or P[0] != "0":
            return False
        if not P[1:].isdigit():
            return False
        return True

    def FetchContact(self):
        if self.varContact.get() == "":
            messagebox.showerror(
                "Error", "Please enter contact number", parent=self.root
            )
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="130806080525",
                database="hotelmanagementsystem",
            )
            myCursor = conn.cursor()
            query = "select firstName from customer where mobile=%s"
            value = (self.varContact.get(),)
            myCursor.execute(query, value)
            row = myCursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "This number has not found", parent=self.root
                )
            else:
                conn.commit()
                conn.close()

                showDataFrame = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=455, y=55, width=300, height=180)

                # Name
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                query = "select firstName from customer where mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblName = Label(
                    showDataFrame, text="Name", font=("Microsoft Sans Serif", 12)
                )
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text=row, font=("Microsoft Sans Serif", 12))
                lbl.place(x=90, y=0)

                # Gender
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                query = "select gender from customer where mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblGender = Label(
                    showDataFrame, text="Gender", font=("Microsoft Sans Serif", 12)
                )
                lblGender.place(x=0, y=30)

                lbl = Label(showDataFrame, text=row, font=("Microsoft Sans Serif", 12))
                lbl.place(x=90, y=30)

                # Email
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                query = "select email from customer where mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblEmail = Label(
                    showDataFrame, text="Email", font=("Microsoft Sans Serif", 12)
                )
                lblEmail.place(x=0, y=60)

                lbl = Label(showDataFrame, text=row, font=("Microsoft Sans Serif", 12))
                lbl.place(x=90, y=60)

                # Nationality
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                query = "select nationality from customer where mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblNationality = Label(
                    showDataFrame, text="Nationality", font=("Microsoft Sans Serif", 12)
                )
                lblNationality.place(x=0, y=90)

                lbl = Label(showDataFrame, text=row, font=("Microsoft Sans Serif", 12))
                lbl.place(x=90, y=90)

                # Address
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                query = "select Address from customer where mobile=%s"
                value = (self.varContact.get(),)
                myCursor.execute(query, value)
                row = myCursor.fetchone()

                lblAddress = Label(
                    showDataFrame, text="Address", font=("Microsoft Sans Serif", 12)
                )
                lblAddress.place(x=0, y=120)

                lbl = Label(showDataFrame, text=row, font=("Microsoft Sans Serif", 12))
                lbl.place(x=90, y=120)

    # Add room booking
    def AddData(self):
        if self.varContact.get() == "" or self.varCheckIn.get() == "":
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
                    "insert into room_booking value(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.varContact.get(),
                        self.varCheckIn.get(),
                        self.varCheckOut.get(),
                        self.varRoomType.get(),
                        self.varRoomDescribe.get(),
                        self.varRoom.get(),
                        self.varMeal.get(),
                        self.varNumOfDays.get(),
                        # self.varPaidTax.get(),
                        # self.varSubTotal.get(),
                        # self.varTotalCost.get(),
                    ),
                )
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo(
                    "success", "booking has been added", parent=self.root
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
        myCursor.execute("select * from room_booking")
        rows = myCursor.fetchall()
        print(rows)
        if len(rows) != 0:
            self.RoomBookingDetailsTable.delete(
                *self.RoomBookingDetailsTable.get_children()
            )
            for i in rows:
                self.RoomBookingDetailsTable.insert("", "end", text=i, values=i)
            conn.commit()
        conn.close()

    def getCursor(self, event=""):
        cursorRow = self.RoomBookingDetailsTable.focus()
        content = self.RoomBookingDetailsTable.item(cursorRow)
        row = content["text"].split(" ")
        self.varContact.set(row[0])
        self.varCheckIn.set(row[1])
        self.varCheckOut.set(row[2])
        self.varRoomType.set(row[3])
        self.varRoomDescribe.set(row[4])
        self.varRoom.set(row[5])
        self.varMeal.set(row[6])
        self.varNumOfDays.set(row[7])

    def Update(self):
        contact = self.varContact.get()
        if contact == "":
            messagebox.showerror(
                "Error", "Please enter a mobile number", parent=self.root
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
                myCursor.execute(
                    "UPDATE room_booking SET check_in=%s, check_out=%s, room_type=%s, room_describe=%s, room=%s, meal=%s, num_of_days=%s WHERE contact=%s",
                    (
                        self.varCheckIn.get(),
                        self.varCheckOut.get(),
                        self.varRoomType.get(),
                        self.varRoomDescribe.get(),
                        self.varRoom.get(),
                        self.varMeal.get(),
                        self.varNumOfDays.get(),
                        self.varContact.get(),
                    ),
                )

                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo(
                    "Update",
                    "Booking details have been updated successfully",
                    parent=self.root,
                )
            except mysql.connector.Error as e:
                messagebox.showerror(
                    "Error", f"Database Error: {str(e)}", parent=self.root
                )

    def Delete(self):
        Delete = messagebox.askyesno(
            "Room Booking", "Do you want to delete this?", parent=self.root
        )
        if Delete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="130806080525",
                database="hotelmanagementsystem",
            )
            myCursor = conn.cursor()
            query = "delete from room_booking where contact=%s"
            value = (self.varContact.get(),)
            myCursor.execute(query, value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetchData()
        conn.close()

    def Reset(self):
        self.varContact.set("")
        self.varCheckIn.set("")
        self.varCheckOut.set("")
        self.varRoomType.set("")
        self.varRoomDescribe.set("")
        self.varRoom.set("")
        self.varMeal.set("")
        self.varNumOfDays.set("")
        self.varPaidTax.set("")
        self.varSubTotal.set("")
        self.varTotalCost.set("")

    # Calculate cost================
    def FormatCost(self, number):
        parts = str(number).split(".")
        integerPart = "{:,}".format(int(parts[0])).replace(",", " ")
        decimalPart = "{:.2f}".format(float("0." + parts[1]))
        formatted_number = f"{integerPart}.{decimalPart[2:]}"
        return formatted_number

    def CalculateCosts(self, mealCost, roomCost):
        q1 = float(mealCost)
        q2 = float(roomCost)
        q3 = float(self.varNumOfDays.get())
        q4 = float(q1 + q2)
        q5 = float(q3 + q4)
        tax = "VND " + self.FormatCost(q5 * 0.09)
        subTotal = "VND " + self.FormatCost(q5)
        total = "VND " + self.FormatCost(q5 + (q5 * 0.09))
        self.varPaidTax.set(tax)
        self.varSubTotal.set(subTotal)
        self.varTotalCost.set(total)

    def Total(self):
        checkInDate = self.varCheckIn.get()
        checkOutDate = self.varCheckOut.get()
        checkInDate = datetime.strptime(checkInDate, "%d/%m/%Y")
        checkOutDate = datetime.strptime(checkOutDate, "%d/%m/%Y")
        self.varNumOfDays.set(abs(checkOutDate - checkInDate).days)

        if self.varMeal.get().lower() == "breakfast":
            mealCost = 300000
        elif self.varMeal.get().lower() == "lunch":
            mealCost = 500000
        if self.varRoomType.get().lower() == "single":
            roomCost = 500000
        if self.varRoomType.get().lower() == "luxury":
            roomCost = 700000
        self.CalculateCosts(mealCost, roomCost)

    # search
    def Search(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="130806080525",
            database="hotelmanagementsystem",
        )
        myCursor = conn.cursor()
        myCursor.execute(
            "select * from room_booking where "
            + str(self.searchVar.get())
            + " LIKE '%"
            + str(self.txtSearch.get())
            + "%'"
        )
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.RoomBookingDetailsTable.delete(
                *self.RoomBookingDetailsTable.get_children()
            )
            for i in rows:
                self.RoomBookingDetailsTable.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
