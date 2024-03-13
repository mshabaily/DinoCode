from LogTools import logger
from Objects import File, Screen

class DiagramScreen(Screen):
    
    def load(self, root, file : File):
        root.drawMainBox(self)
        root.drawNavbar(self)
        logger.log("drawing diagram screen...")