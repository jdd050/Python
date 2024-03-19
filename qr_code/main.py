import os
from PIL import ImageTk, Image
import qrcode
import tkinter as tk

class Main(tk.Tk):
    # create the root window
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)
        self.organize_content()
        self.ui()
        self.mainloop()
    
    # create a layout for the window content
    def organize_content(self) -> None:
        # define the top area
        self.top_rectangle = tk.Frame(self.master, background="red", width=800, height=75)
        self.top_rectangle.grid(column=0, row=0, columnspan=2, rowspan=1, padx=0, pady=0)
        # define middle left
        self.left = tk.Frame(self.master, background="Gray", width=400, height=450)
        self.left.grid(column=0, row=1, columnspan=1, rowspan=1, padx=0, pady=0)
        # define middle right
        self.right = tk.Frame(self.master, background="black", width=400, height=450)
        self.right.grid(column=1, row=1, columnspan=1, rowspan=1, padx=0, pady=0)
        # define bottom
        self.bottom_rectangle = tk.Frame(self.master, background="blue", width=800, height=75)
        self.bottom_rectangle.grid(column=0, row=2, columnspan=2, rowspan=1, padx=0, pady=0)
        return None
    
    # function responsible for creating and managing the user interface
    def ui(self) -> None:
        ### TOP ###
        # create the title for the app
        title = tk.Label(self.top_rectangle, text="Python QR Code Generator", font=("Helvetica bold", 26, "bold"))
        title.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ### MID-LEFT ###
        left_header = tk.Label(self.left, text="Options", font=("Helvetica bold", 13))
        left_header.place(relx=0.5, rely=0.05, anchor="n")
        ### MID-RIGHT ###
        # area where the QR code will be
        #self.image1 = Image.open("qr_code\\qr_code.png")
        #self.image1.resize((250, 250))
        #self.test =  ImageTk.PhotoImage(self.image1)
        #label1 = tk.Label(self.right, image=self.test, width=250, height=250)
        #label1.pack(padx=0.1, pady=0.1, fill="none")
        return None

instance = Main()


'''
# Encode the data using make()
img = qrcode.make(data)

# Save as a PNG file
img.save("qr_code.png")
'''