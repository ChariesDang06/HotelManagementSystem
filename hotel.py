from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from customer import CustomerWindow
from room import RoomManage
from booking import RoomBooking


class HotelManagementSystem:
    # main frame - root
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.root.configure(background="linen")
        root.resizable(width=True, height=True)

        # ==============sologan img ================
        slogan = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\sologan.png"
        )  # Creating a photoimage object to use image
        slogan = slogan.resize((1320, 140), Image.LANCZOS)
        self.photoSlogan = ImageTk.PhotoImage(slogan)

        lblimg = Label(self.root, image=self.photoSlogan, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1320, height=140)
        lblimg.grid(column=1, row=0)

        # ==============logo img====================
        logo = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\logo.png"
        )
        # resize the image and apply a high-quality down sampling filter
        logo = logo.resize((230, 140), Image.LANCZOS)
        self.photoLogo = ImageTk.PhotoImage(logo)

        lblimg = Label(self.root, image=self.photoLogo, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
        lblimg.grid(column=0, row=0)

        # ===============title====================
        lblTitle = Label(
            self.root,
            text="HOTEL MANAGEMENT SYSTEM",
            font=("Microsoft Sans Serif", 30, "bold"),
            bg="black",
            fg="bisque",
            bd=4,  # border - pixels
            relief=RIDGE,  # 3-D effect
        )
        lblTitle.place(x=0, y=152, width=1550, height=50)

        # =================main frame===============
        mainFrame = Frame(self.root, bd=4, relief=RIDGE)
        mainFrame.place(x=0, y=202, width=1550, height=610)

        # ==================Menu====================
        # lblMenu = Label(
        #     mainFrame,
        #     text="MENU",
        #     font=("Microsoft Sans Serif", 20, "bold"),
        #     bg="black",
        #     fg="bisque",
        #     bd=4,
        #     relief=RIDGE,
        # )
        # lblMenu.place(x=0, y=0, width=230)

        # =================btn Frame==============
        btnFrame = Frame(mainFrame, bd=4, relief=RIDGE)
        btnFrame.place(x=-1, y=-1, width=234, height=163)
        btnFrame.grid(row=0, column=0)

        customBtn = Button(
            btnFrame,
            width=13,
            text="CUSTOMER",
            command=self.CustomerDetails,
            font=("Microsoft Sans Serif", 20, "bold"),
            bg="black",
            fg="bisque",
            bd=0,
            cursor="hand1",
        )
        customBtn.grid(row=0, column=0, pady=1)

        customBtn = Button(
            btnFrame,
            width=13,
            text="BOOKING",
            command=self.RoomBooking,
            font=("Microsoft Sans Serif", 20, "bold"),
            bg="black",
            fg="bisque",
            bd=0,
            cursor="hand1",
        )
        customBtn.grid(row=1, column=0, pady=1)

        customBtn = Button(
            btnFrame,
            width=13,
            text="ROOM",
            command=self.RoomManage,
            font=("Microsoft Sans Serif", 20, "bold"),
            bg="black",
            fg="bisque",
            bd=0,
            cursor="hand1",
        )
        customBtn.grid(row=2, column=0, pady=1)

        # ========================down image==============
        hotelImg1 = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\hotel2.png"
        )
        hotelImg1 = hotelImg1.resize((227, 210), Image.LANCZOS)
        self.photoHotel1 = ImageTk.PhotoImage(hotelImg1)

        lblimg1 = Label(mainFrame, image=self.photoHotel1, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=227, height=210)
        lblimg1.grid(row=1, column=0)

        hotelImg2 = Image.open(
            r"C:\Users\Admin\OneDrive\Desktop\Hotel_Management_System\images\hotel3.png"
        )
        hotelImg2 = hotelImg2.resize((227, 210), Image.LANCZOS)
        self.photoHotel2 = ImageTk.PhotoImage(hotelImg2)

        lblimg1 = Label(mainFrame, image=self.photoHotel2, bd=4, relief=RIDGE)
        lblimg1.place(x=435, y=0, width=227, height=210)
        lblimg1.grid(row=2, column=0)

        # ==============
        self.test = StringVar()
        entryContact = Entry(
            root,
            textvariable=self.test,
            font=("Microsoft Sans Serif", 12),
            width=17,
            # validate="key",
            # validatecommand=(self.root.register(self.validate_input), "%P"),
        )
        entryContact.place(x=500, y=300, width=300, height=50)
        self.test.set("0123215")

    def CustomerDetails(self):
        self.newWindow = Toplevel(self.root)
        self.app = CustomerWindow(self.newWindow)

    def RoomBooking(self):
        self.newWindow = Toplevel(self.root)
        self.app = RoomBooking(self.newWindow)

    def RoomManage(self):
        self.newWindow = Toplevel(self.root)
        self.app = RoomManage(self.newWindow)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
