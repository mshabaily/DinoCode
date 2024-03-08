from tkinter import Tk
from LogTools import logger
from Objects import EasyFrame, EasyWindow

# This class is the main root of the system
# It contains reusable functions for drawing UI components
# All loading of screens should be done through the load() function of this class

class Window(EasyWindow):

    navBar : EasyFrame
    mainBox : EasyFrame

    def __init__(self, title : str, width : int, height : int ):
        super().__init__()
        self.geometry(str(width) + "x" + str(height))
        self.title(title)
        logger.log("opening new window...")

        # In order for these widgets to be accessed elsewhere, they need to be initialised alongside the window
        # They are later redefined with attributes in the appropriate "draw" functions
        self.navBar = EasyFrame()
        self.mainBox = EasyFrame()

    # This function takes any screen with a defined load() function and opens it on the window
    # This approach allows screens to be opened on multiple windows easily
    def load(self,Screen):
        logger.log("loading new screen...")
        try:
            screen = Screen()
            screen.load(self)
        except:
            logger.throw("SCREEN LOADING FAILED")
        finally:
            screen.pack()

    def drawNavbar(self,screen):
        navBarWidth = self.width()
        navBarHeight = self.height() / 10
        logger.log("drawing navbar... width = ", navBarWidth, " height = ", navBarHeight)
        self.navBar = EasyFrame(screen, width = navBarWidth, height = navBarHeight)
        self.navBar.config(background = "#4caf50")
        self.navBar.pack(anchor = "n")

    def drawMainBox(self,screen):
        boxWidth = int(self.width() * 0.9)
        boxHeight = int(self.height() * 0.9)
        logger.log("drawing main box... width = ", boxWidth, " height = ", boxHeight)
        self.mainBox = EasyFrame(screen, width = boxWidth, height = boxHeight)
        self.mainBox.config(background = "gray", border = 0)
        self.mainBox.pack(anchor = "center", expand = True, pady = 50)

mainWindow = Window(title = "DinoCode", width = 1900, height = 1200)