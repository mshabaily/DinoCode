from tkinter import Button, Frame, Tk

# EasyObjects are used to keep things simple in the rest of the code
# Functions that have strange names can be redefined here
# Utilities that you think ALL other objects in the code should have can be put here
class EasyObject():
    def height(self):
        return self.winfo_screenheight()
    def width(self):
        return self.winfo_screenwidth()
    def clear(self):
        for child in self.winfo_children():
            child.destroy()

# New "Easy" objects can be made by extending both the root object, and EasyObject
class EasyWindow(Tk, EasyObject):
    pass

class EasyFrame(Frame, EasyObject):
    pass

class EasyButton(Button, EasyObject):
    pass

class Screen(EasyFrame):
    def load(self, screen, *args, **kwargs):
        pass

# Class containing
class File():
    title : str
    code : str
    def __init__(self):
        self.title = ""
        self.code = ""

# Class for containing information about classes found within the code
class ClassInfo():

    title : str
    methods = []
    attributes = []

    def __init__(self, title):
        self.title = title
        self.methods = []
        self.attributes = []
    def addMethod(self, methodName : str):
        self.methods.append(methodName)
    def addAttribute(self, attributeName : str):
        self.attributes.append(attributeName)


# This object is an instance of ClassInfo - just for use in testing that class diagram drawing
testClassObject = ClassInfo("Test Class")
testClassObject.addMethod("Test Method")
testClassObject.addAttribute("Test Attribute")