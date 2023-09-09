import turtle as trtl
import tkinter as tk

class main():
    
    # get width and height
    def __init__(self):
        while True:
            try:
                self.winWidth = int(input("Please enter the desired window width in pixels: "))
                self.winHeight = int(input("Please enter the desired window height in pixels: "))
                print(f'Launching application with dimensions {self.winWidth}x{self.winHeight}')
                break
            except ValueError:
                print('Non-integer value entered. Please try again.')
            pass
        return None
    
    # create main tkinter canvas
    def rootSetup(self):
        # init canvas
        global canvas
        canvas = tk.Canvas(master=None, width=self.winWidth, height=self.winHeight)
        canvas.pack(side=tk.LEFT)
        
        # set background
        canvas.create_rectangle((-self.winWidth)/2, (-self.winHeight)/2 , self.winWidth, self.winHeight, fill='lightYellow')
        return canvas
    
    # create graph region for a cartesian plane
    def makeCartesian(self):
        # background
        rectWidth = self.winWidth / 2
        rectHeight = self.winHeight / 2
        cartesianCanvas = tk.Canvas(master=None, width=rectWidth, height=rectHeight)
        # init RawTurtle (ALL canvas changes to be made after this)
        draw = trtl.RawTurtle(cartesianCanvas)
        cartesianRect = canvas.create_rectangle((-rectWidth) + 200, (-rectHeight), (rectWidth), (rectHeight) - 200, fill='white')
        
        # axes and lines
        
        return cartesianRect, cartesianCanvas, draw
    
    
    # keep window open
    def persistWindow(self):
        loop = canvas.mainloop()
        return loop
    pass

classObj = main()
classObj.rootSetup()
classObj.makeCartesian()
classObj.persistWindow()