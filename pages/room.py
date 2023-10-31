from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk  # pip install pillow
import random
import mysql.connector
from time import strftime
from datetime import datetime


class RoomManage:
    def __init__(self, root):
        self.root = root
        self.root.title("Room Management")
        self.root.geometry("1295x550+240+240")
        self.root.configure(background="linen")
        root.resizable(width=True, height=True)

        self.varFloor = StringVar()
        self.varRoomNumber = StringVar()
        self.varRoomDescribe = StringVar()
        self.varRoomType = StringVar()

        lblTitle = Label(
            self.root,
            text="ROOM MANAGEMENT",
            font=("Microsoft Sans Serif", 18, "bold"),
            bg="black",
            fg="bisque",
            bd=4,
            relief=RIDGE,
        )
        lblTitle.place(x=0, y=0, width=1295, height=50)

        # details label===================
        labelRoomPicture = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            # text="Add New Rooms",
            font=("Microsoft Sans Serif", 12, "bold"),
            bg="linen",
            padx=2,
        )
        labelRoomPicture.place(x=5, y=50, width=610, height=490)

        room1 = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\room1.png"
        )
        room1 = room1.resize((520, 300), Image.LANCZOS)
        self.photoRoom1 = ImageTk.PhotoImage(room1)

        lblimg1 = Label(labelRoomPicture, image=self.photoRoom1, bd=4, relief=RIDGE)
        lblimg1.place(x=5, y=5, width=290, height=230)

        room2 = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\room2.png"
        )
        room2 = room2.resize((520, 300), Image.LANCZOS)
        self.photoRoom2 = ImageTk.PhotoImage(room2)

        lblimg2 = Label(labelRoomPicture, image=self.photoRoom2, bd=4, relief=RIDGE)
        lblimg2.place(x=305, y=5, width=290, height=230)

        Room3 = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\room3.png"
        )
        Room3 = Room3.resize((520, 300), Image.LANCZOS)
        self.photoRoom3 = ImageTk.PhotoImage(Room3)

        lblimg3 = Label(labelRoomPicture, image=self.photoRoom3, bd=4, relief=RIDGE)
        lblimg3.place(x=5, y=250, width=290, height=230)

        room4 = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\room4.png"
        )
        room4 = room4.resize((520, 300), Image.LANCZOS)
        self.photoRoom4 = ImageTk.PhotoImage(room4)

        lblimg4 = Label(labelRoomPicture, image=self.photoRoom4, bd=4, relief=RIDGE)
        lblimg4.place(x=305, y=250, width=290, height=230)

        labelRoomManageFrame = LabelFrame(
            self.root,
            bd=2,
            relief=RIDGE,
            text="Add New Rooms",
            font=("Microsoft Sans Serif", 12, "bold"),
            bg="linen",
            padx=2,
        )
        labelRoomManageFrame.place(x=610, y=50, width=670, height=490)

        # room input=========
        roomInputFrame = LabelFrame(
            labelRoomManageFrame,
            bd=2,
            relief=RIDGE,
            font=("Microsoft Sans Serif", 12, "bold"),
            padx=2,
            bg="linen",
        )
        roomInputFrame.place(x=5, y=5, width=655, height=190)

        lblFloor = Label(
            roomInputFrame,
            text="Floor",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblFloor.grid(row=0, column=0, sticky=W)

        entryFloor = ttk.Entry(
            roomInputFrame,
            textvariable=self.varFloor,
            width=20,
            font=("Microsoft Sans Serif", 12),
        )
        entryFloor.grid(row=0, column=1, sticky=W)

        lblRoomNumber = Label(
            roomInputFrame,
            text="Room Number",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblRoomNumber.grid(row=1, column=0, sticky=W)

        entryRoomNumber = ttk.Entry(
            roomInputFrame,
            textvariable=self.varRoomNumber,
            width=20,
            font=("Microsoft Sans Serif", 12),
        )
        entryRoomNumber.grid(row=1, column=1, sticky=W)

        lblRoomDescribe = Label(
            roomInputFrame,
            text="Room Describe",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblRoomDescribe.grid(row=3, column=0, sticky=W)

        entryRoomDescribe = ttk.Entry(
            roomInputFrame,
            textvariable=self.varRoomDescribe,
            width=55,
            font=("Microsoft Sans Serif", 12),
        )
        entryRoomDescribe.grid(row=3, column=1, sticky=W)

        lblRoomType = Label(
            roomInputFrame,
            text="Room Type",
            font=("Microsoft Sans Serif", 12),
            padx=2,
            pady=6,
            bg="linen",
        )
        lblRoomType.grid(row=2, column=0, sticky=W)

        cbxRoomType = ttk.Combobox(
            roomInputFrame,
            textvariable=self.varRoomType,
            width=20,
            font=("Microsoft Sans Serif", 12),
            state="readonly",
        )
        cbxRoomType["value"] = ("Single", "Duplex", "Luxury")
        cbxRoomType.current(0)
        cbxRoomType.grid(row=2, column=1, sticky=W)

        # button
        btnFrame = Frame(roomInputFrame, bd=2, bg="linen", relief=RIDGE)
        btnFrame.place(x=5, y=145, width=640, height=40)

        btnAdd = Button(
            btnFrame,
            text="Add",
            command=self.AddData,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnAdd.grid(row=0, column=0, padx=27)

        btnUpdate = Button(
            btnFrame,
            text="Update",
            command=self.Update,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnUpdate.grid(row=0, column=1, padx=27)

        btnDelete = Button(
            btnFrame,
            text="Delete",
            command=self.Delete,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnDelete.grid(row=0, column=2, padx=27)

        btnReset = Button(
            btnFrame,
            text="Reset",
            command=self.Reset,
            font=("Microsoft Sans Serif", 12),
            bg="linen",
            width=10,
        )
        btnReset.grid(row=0, column=3, padx=27)

        # =================show data table=========================

        detailsTable = Frame(labelRoomManageFrame, bd=2, relief=RIDGE)
        detailsTable.place(x=0, y=200, width=655, height=260)

        scrollX = ttk.Scrollbar(detailsTable, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(detailsTable, orient=VERTICAL)

        self.RoomDetailsTable = ttk.Treeview(
            detailsTable,
            columns=(
                "floor",
                "room_number",
                "room_type",
                "room_describe",
            ),
            xscrollcommand=scrollX.set,
            yscrollcommand=scrollY.set,
        )

        scrollXFrame = ttk.Frame(detailsTable)
        scrollYFrame = ttk.Frame(detailsTable)
        scrollX = ttk.Scrollbar(
            scrollXFrame,
            orient=HORIZONTAL,
            command=self.RoomDetailsTable.xview,
        )
        scrollY = ttk.Scrollbar(
            scrollYFrame,
            orient=VERTICAL,
            command=self.RoomDetailsTable.yview,
        )

        scrollXFrame.pack(side=BOTTOM, fill=X)
        scrollYFrame.pack(side=RIGHT, fill=Y)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)

        self.RoomDetailsTable.heading("floor", text="Floor")
        self.RoomDetailsTable.heading("room_number", text="Room Number")
        self.RoomDetailsTable.heading("room_type", text="Room Type")
        self.RoomDetailsTable.heading("room_describe", text="Room Describe")

        self.RoomDetailsTable["show"] = "headings"

        self.RoomDetailsTable.column("floor", width=100)
        self.RoomDetailsTable.column("room_number", width=100)
        self.RoomDetailsTable.column("room_type", width=100)
        self.RoomDetailsTable.column("room_describe", width=300)

        self.RoomDetailsTable.pack(fill=BOTH, expand=1)
        self.RoomDetailsTable.bind("<ButtonRelease-1>", self.getCursor)
        self.fetchData()

    def fetchData(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="130806080525",
            database="hotelmanagementsystem",
        )
        myCursor = conn.cursor()
        myCursor.execute("select * from room_manage")
        rows = myCursor.fetchall()
        if len(rows) != 0:
            self.RoomDetailsTable.delete(*self.RoomDetailsTable.get_children())
            for i in rows:
                self.RoomDetailsTable.insert("", END, values=i)
            conn.commit()
        conn.close()

    def getCursor(self, event=""):
        cursorRow = self.RoomDetailsTable.focus()
        content = self.RoomDetailsTable.item(cursorRow)
        row = content["values"]

        self.varFloor.set(row[0])
        self.varRoomNumber.set(row[1])
        self.varRoomType.set(row[2])
        self.varRoomDescribe.set(row[3])

    # Add room
    def AddData(self):
        if self.varRoomNumber.get() == "" or self.varRoomNumber == "":
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
                    "insert into room_manage value(%s,%s,%s,%s)",
                    (
                        self.varFloor.get(),
                        self.varRoomNumber.get(),
                        self.varRoomType.get(),
                        self.varRoomDescribe.get(),
                    ),
                )
                conn.commit()
                self.fetchData()
                conn.close()
                messagebox.showinfo("success", "room has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "waring", f"Some thing went wrong:{str(es)}", parent=self.root
                )

    # Update room
    def Update(self):
        if self.varRoomNumber.get() == "":
            messagebox.showerror("Error", "Please enter room number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="130806080525",
                    database="hotelmanagementsystem",
                )
                myCursor = conn.cursor()
                update_query = "UPDATE room_manage SET floor=%s,room_type=%s,room_describe=%s WHERE room_number=%s"

                update_data = (
                    self.varFloor.get(),
                    self.varRoomType.get(),
                    self.varRoomDescribe.get(),
                    self.varRoomNumber.get(),
                )

                myCursor.execute(update_query, update_data)
                conn.commit()

                self.fetchData()
                conn.close()
                messagebox.showinfo(
                    "Update",
                    "Room details have been updated successfully",
                    parent=self.root,
                )
            except Exception as e:
                messagebox.showerror(
                    "Error", f"An error occurred: {str(e)}", parent=self.root
                )

    def Delete(self):
        Delete = messagebox.askyesno(
            "Room Manage", "Do you want to delete this?", parent=self.root
        )
        if Delete > 0:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="130806080525",
                database="hotelmanagementsystem",
            )
            myCursor = conn.cursor()
            query = "delete from room_manage where room_number=%s"
            value = (self.varRoomNumber.get(),)
            myCursor.execute(query, value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetchData()
        conn.close()

    def Reset(self):
        self.varFloor.set("")
        self.varRoomNumber.set("")
        self.varRoomType.set("")
        self.varRoomDescribe.set("")


if __name__ == "__main__":
    root = Tk()
    obj = RoomManage(root)
    root.mainloop()
