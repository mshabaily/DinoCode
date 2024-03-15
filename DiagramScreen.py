from tkinter import Label
from LogTools import logger
from Objects import EasyFrame, Screen
from findClasses import findClasses

class DiagramScreen(Screen):
    
    # The code is passed in as a string, stored here
    # Classes are also stored as a list of ClassInfo objects
    code : str
    classes = []
    
    def load(self, root, code : str):
        root.drawNavbar(self)
        root.drawMainBox(self)
        self.code = code
        # The find classes function takes the code string and returns the list of ClassInfo objects
        self.classes = findClasses(code)
        logger.log("drawing diagram screen for code:", self.code)
        for classInstance in self.classes:
            self.drawClass(root, classInstance)

    # This function takes the class info and draws the UML object diagram
    def drawClass(self, root, classInfo):
        diagramFrame = EasyFrame(root.mainBox, width = 500, background = "white")
        # Currently the diagram is just being placed in the corner
        diagramFrame.place(x = 0,y = 0)
        titleLabel = Label(diagramFrame, text=classInfo.title)
        logger.log("drawing new class: ", classInfo.title)
        titleLabel.pack()

        for attribute in classInfo.attributes:
            attributeLabel = Label(diagramFrame, text = attribute)
            attributeLabel.pack()
        for method in classInfo.methods:
            methodLabel = Label(diagramFrame, text = method)
            methodLabel.pack()
