import os
from PIL import ImageTk, Image
import qrcode
import tkinter
from tkinter import filedialog

class Main(tkinter.Tk):
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
        self.top_rectangle = tkinter.Frame(self.master, background="red", width=800, height=75)
        self.top_rectangle.grid(column=0, row=0, columnspan=2, rowspan=1, padx=0, pady=0)
        # define middle left
        self.left = tkinter.Frame(self.master, background="Gray", width=400, height=525)
        self.left.grid(column=0, row=1, columnspan=1, rowspan=1, padx=0, pady=0)
        # define middle right
        self.right = tkinter.Frame(self.master, background="black", width=400, height=525)
        self.right.grid(column=1, row=1, columnspan=1, rowspan=1, padx=0, pady=0)
        return None
    
    # function for opening images in the image entry
    def open_image(self) -> None:
        image_filename = filedialog.askopenfilename()
        print(image_filename)
        self.image_file = Image.open(image_filename)
        return None
        
    # function responsible for creating and managing the user interface
    def ui(self) -> None:
        ### TOP ###
        # create the title for the app
        title = tkinter.Label(self.top_rectangle, text="Python QR Code Generator", font=("Helvetica bold", 26, "bold"))
        title.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        
        ### MID-LEFT ###
        left_header = tkinter.Label(self.left, text="Options", font=("Helvetica bold", 13))
        left_header.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        # text data entry
        self.text_var = tkinter.StringVar()
        text_data = tkinter.Entry(self.left, textvariable=self.text_var, width=50)
        text_data.place(relx=0.55, rely=0.2, anchor=tkinter.CENTER)
        text_label = tkinter.Label(self.left, text="Text:", font=("Helvetica bold", 13, "bold"), bg="black", fg="white")
        text_label.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
        # image entry
        image_button = tkinter.Button(self.left, text="Choose an Image", command=self.open_image)
        image_button.place(relx=0.35, rely=0.3, anchor=tkinter.CENTER)
        image_label = tkinter.Label(self.left, text="Image:", font=("Helvetica bold", 13, "bold"), bg="black", fg="white")
        image_label.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
        # link entry
        self.link_var = tkinter.StringVar()
        link_data = tkinter.Entry(self.left, textvariable=self.link_var, width=50)
        link_data.place(relx=0.55, rely=0.4, anchor=tkinter.CENTER)
        link_label = tkinter.Label(self.left, text="Link:", font=("Helvetica bold", 13, "bold"), bg="black", fg="white")
        link_label.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)
        # generate button
        generate_button = tkinter.Button(self.left, text="Generate QR Code", command=lambda:print("generate button pressed"))
        generate_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        
        ### MID-RIGHT ###
        # the qr code
        self.generate_qr_code()
        # save button
        save_button = tkinter.Button(self.right, text="Save QR Code", command=lambda:print("save button pressed"))
        save_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        return None
    
    # placeholder for now
    def generate_qr_code(self) -> None:
        self.qr_code_img = Image.open(r"qr_code\granny.png")
        self.qr_code_photo = ImageTk.PhotoImage(self.qr_code_img.resize((250, 300)))
        label = tkinter.Label(self.right, image=self.qr_code_photo, width=250, height=300)
        label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        

instance = Main()


'''
# Encode the data using make()
img = qrcode.make(data)

# Save as a PNG file
img.save("qr_code.png")
'''