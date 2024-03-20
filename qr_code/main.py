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
        left_header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        '''
        doesnt work because .grid() doesnt want to exist (idk tbh)
        
        # filler for formatting
        filler_one = tk.Label(self.left)
        filler_one.grid(row=0, column=0)
        # section title
        left_header = tk.Label(self.left, text="Options", font=("Helvetica bold", 13))
        left_header.grid(row=0, column=1)
        # filler for formatting
        filler_two = tk.Label(self.left)
        filler_two.grid(row=0, column=2)
        '''
        ### MID-RIGHT ###
        # the qr code
        self.generate_qr_code()
        return None
    
    # placeholder for now
    def generate_qr_code(self) -> None:
        self.qr_code_img = Image.open(r"qr_code\granny.png")
        self.qr_code_photo = ImageTk.PhotoImage(self.qr_code_img.resize((250, 300)))
        label = tk.Label(self.right, image=self.qr_code_photo, width=250, height=300)
        label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

instance = Main()


'''
# Encode the data using make()
img = qrcode.make(data)

# Save as a PNG file
img.save("qr_code.png")
'''