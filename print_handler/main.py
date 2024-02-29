import ctypes
import ftplib
import tkinter as tk
import socket

class Main:
    def __init__(self) -> None:
        self.root = tk.Tk()
        # scale window size to monitor resolution
        user32 = ctypes.windll.user32
        self.screen_size = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
        scale_factor = (1920/800, 1080/600) # Set the scale factor (based on 1920x1080)
        # resize the window
        self.root.wm_geometry(f"{int(self.screen_size[0]/scale_factor[0])}x{int(self.screen_size[1]/scale_factor[1])}")
    
    def scan_network(self) -> list:
        self.port = 8080
        return []
    
    def create_ui(self) -> None:
        
        return None
    
if __name__ == "__main__":
    Main().root.mainloop()