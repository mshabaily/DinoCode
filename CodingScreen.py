from tkinter import Button, Frame, Text
from LogTools import logger
from Objects import Screen

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

        # Some trickery pack configuring here, this just makes sure that the Text box fills the whole frame under it
        self.entryField = Text(root.mainBox, height = 600)
        root.mainBox.pack_configure(fill = "both", expand = True, padx = 50)
        self.entryField.pack(fill="both", expand=True)
        keypressResponse = lambda event: self.getKeypress()
        self.entryField.bind("<KeyRelease>", keypressResponse)

        self.saveButton = Button(root.navBar, text = "Save")
        self.saveButton.config(command = self.save)
        self.saveButton.place(x = 0, y = 0)

    def save(self):
        self.winfo_toplevel().currentFile.text = self.text