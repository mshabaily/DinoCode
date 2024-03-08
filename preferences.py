import tkinter as tk
from tkinter import ttk

# Create dictionary to store preferences
preferences_states = {}

def save_preferences():
    # Get state of each checkbox and store in dictionary
    preferences_states['Option 1'] = checkbox1_var.get()
    preferences_states['Option 2'] = checkbox2_var.get()
    preferences_states['Option 3'] = checkbox3_var.get()
    preferences_states['Slider'] = slider_var.get()

    print(preferences_states)

def update_slider_label(*args):
    #Update the label text by changing the slider_label variable to "Slider: {the current slider value}"
    slider_label.config(text=f"Slider: {slider_var.get()}")

def create_preferences_page():
    global checkbox1_var, checkbox2_var, checkbox3_var, slider_var, slider_label  # slider_var is the IntVar for the slider and slider_label is the label for the slider which is updated in update_slider_label function above
    preferences_window = tk.Toplevel() # Create a new top level window (aka a pop-up window seperete from the main window, can change this to be part of main window if needed??)
    preferences_window.title("Preferences")

    #Create frame to hold checkboxes
    checkboxes_frame = ttk.Frame(preferences_window, padding="20")
    checkboxes_frame.pack()

    #Create da checkboxes with boolean vars - true=ticked false=not ticked
    checkbox1_var = tk.BooleanVar()
    checkbox1 = ttk.Checkbutton(checkboxes_frame, text="Option 1", variable=checkbox1_var)
    checkbox1.pack()

    checkbox2_var = tk.BooleanVar()
    checkbox2 = ttk.Checkbutton(checkboxes_frame, text="Option 2", variable=checkbox2_var)
    checkbox2.pack()

    checkbox3_var = tk.BooleanVar()
    checkbox3 = ttk.Checkbutton(checkboxes_frame, text="Option 3", variable=checkbox3_var)
    checkbox3.pack()

    #Create da frame to hold da slider
    slider_frame = ttk.Frame(preferences_window, padding="20")
    slider_frame.pack()

    #Create da label for da slider
    slider_label = ttk.Label(slider_frame, text="Slider: 0")
    slider_label.pack(side="left")

    #Create da slider
    slider_var = tk.IntVar()
    slider = ttk.Scale(slider_frame, from_=0, to=100, variable=slider_var, command=update_slider_label)
    slider.pack(side="left")

    #Button to perform save_preferences function
    save_button = ttk.Button(preferences_window, text="Save", command=save_preferences)
    save_button.pack(pady="10")

def create_main_page():
    main_window = tk.Tk()
    main_window.title("DinoCode")

    #Frame to hold the text
    text_frame = ttk.Frame(main_window, padding="20")
    text_frame.pack()

    #Label for the text
    text_label = ttk.Label(text_frame, text="DinoCode", font=("Arial", 24))
    text_label.pack()

    #Create Settings button on main page that performs create_preferences_page function
    settings_button = ttk.Button(main_window, text="Settings", command=create_preferences_page)
    settings_button.pack(anchor="ne", padx="10", pady="10")

    main_window.mainloop()

create_main_page()