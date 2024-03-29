from tkinter import Frame, Tk

# EasyObjects are used to keep things simple in the rest of the code
# Functions that have strange names can be redefined here
# Utilities that you think ALL other objects in the code should have can be put here
class EasyObject():
    def height(self):
        return self.winfo_screenheight()
    def width(self):
        return self.winfo_screenwidth()

# New "Easy" objects can be made by extending both the root object, and EasyObject
class EasyWindow(Tk, EasyObject):
    pass

class EasyFrame(Frame, EasyObject):
    pass