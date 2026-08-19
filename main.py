import tkinter as tk
import sys
import os as o
#needed global functions
def resource_path(main,relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = o.path.dirname(o.path.abspath(__file__))    
    return o.path.join(base_path, relative_path)
#constant vairables
STARTING_SIZE_WIDTH = 1000
STARTING_SIZE_HEIGHT = 1000
#game class full only
class Cafe:
    def __init__(cafe, root):
        cafe.root = root

window = tk.Tk()
game = Cafe(window)
window.geometry(f"{STARTING_SIZE_WIDTH}x{STARTING_SIZE_HEIGHT}")
window.title("Cat Café")
window.mainloop()