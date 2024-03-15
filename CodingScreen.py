from tkinter import Text
from LogTools import logger
from Objects import EasyButton, Screen

class CodingScreen(Screen):

    entryField : Text
    text : str

    def __init__(self, *args):
        super().__init__(*args)
        self.entryField = Text()
        self.text = ""

    # This method is called each time a keypress is registered
    # It gets the text from the Text widget, beginning index 1 and ending at "end-1c"
    # "end-1c" = the end minus the newline character
    def getKeypress(self):
        self.text = self.entryField.get("1.0", "end-1c")

    def load(self, root):
        self.master = root
        logger.log("drawing coding screen...")
        root.drawNavbar(self)
        root.drawMainBox(self)

        self.entryField = Text(root.mainBox, height = 600)

        # If the window already has code saved to it, it will be reloaded here
        if root.currentFile.code:
            self.entryField.insert(1.0,root.currentFile.code)

        # Some tricky pack configuring here, this just makes sure that the Text box fills the whole frame under it
        root.mainBox.pack_configure(fill = "both", expand = True, padx = 50)
        self.entryField.pack(fill="both", expand=True)

        # Here the binding is set to update the text stored by the coding screen when it is typed into
        keypressResponse = lambda event: self.getKeypress()
        self.entryField.bind("<KeyRelease>", keypressResponse)

        self.saveButton = EasyButton(root.navBar, text = "Save")
        self.saveButton.config(command = lambda: self.save(root))
        # Need to find a better way of putting the button in the right corner with place
        self.saveButton.place(x = root.width()-90, y = 0)

    def save(self, root):
        root.currentFile.code = self.text
        logger.log("Code saved:", root.currentFile.code)