from tkinter import Label
from LogTools import logger
from Objects import EasyFrame, Screen
from findClasses import findClasses

class DiagramScreen(Screen):
    
    code : str
    classes = []
    
    def load(self, root, code : str):
        root.drawNavbar(self)
        root.drawMainBox(self)
        self.code = code
        self.classes = findClasses(code)
        logger.log("drawing diagram screen for code:", self.code)
        for classInstance in self.classes:
            self.drawClass(root, classInstance)

    def drawClass(self, root, classInfo):
        diagramFrame = EasyFrame(root.mainBox, width = 500, background = "white")
        diagramFrame.place(x = 0,y = 0)
        titleLabel = Label(diagramFrame, text=classInfo.title)
        titleLabel.pack()
        for attribute in classInfo.attributes:
            attributeLabel = Label(diagramFrame, text = attribute)
            attributeLabel.pack()
        for method in classInfo.methods:
            methodLabel = Label(diagramFrame, text = method)
            methodLabel.pack()
