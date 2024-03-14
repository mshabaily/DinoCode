import tkinter as tk
from tkinter import ttk
import json

#TODO - create class "PreferenceScreen" to contain all this shite
# Then head to Main.py and create a simple button (can be shit for now) and have the button call upon the create_preferences_page in this class, need to get rid of create_main_page method (at the bottom) and instead rely on matts CodingScreen

#Create dictionary to store preferences
current_preferences_states = {}
preset_preference_names = []

def save_preferences():
    #Get state of each checkbox and store in dictionary
    #bottom 3 are currently placeholders as they have no selection boxes etc

    #Save preferences to a JSON file
    current_preferences_states['show-line-numbers'] = checkbox1_var.get()
    current_preferences_states['auto-save'] = checkbox2_var.get()
    current_preferences_states['Option 3'] = checkbox3_var.get()
    current_preferences_states['Slider'] = slider_var.get()
    #TODO add rest of preferences here as they are added as dropdowns/options else they arent saved correctly when no preset is selected
    with open('preferences.json', 'w') as file:
        json.dump(current_preferences_states, file)

    print(current_preferences_states)

def update_current_preferences_to_selected_preset(selected_preset):
    with open('preset-preferences.json', 'r') as file:
        preset_preferences = json.load(file)
        # update the current_preferences_states to the selected preset using the name of the preset as the key to get the values from the dictionary
        for preset in preset_preferences:
            if preset['name'] == selected_preset:
                # Update the current_preferences_states to the selected preset
                current_preferences_states.update(preset['settings'])
                #add the rest of the custom options
                current_preferences_states['show-line-numbers'] = checkbox1_var.get()
                current_preferences_states['auto-save'] = checkbox2_var.get()
                current_preferences_states['Option 3'] = checkbox3_var.get()
                current_preferences_states['Slider'] = slider_var.get()
                print(current_preferences_states)
                break

def update_slider_label(*args): # *args accept any number of arguments and ignore them cos we don't need them 
    #as we get the slider value from the slider_var global var
    #Update the label text by changing the slider_label variable to "Slider: {the current slider value}"
    slider_label.config(text=f"Slider: {slider_var.get()}")

def create_preferences_page():
    global checkbox1_var, checkbox2_var, checkbox3_var, slider_var, slider_label 
    # slider_var is the IntVar for the slider and slider_label is the 
    # label for the slider which is updated in update_slider_label function above

    preferences_window = tk.Toplevel()  # Create a new top level window (aka a pop-up window seperete from the main window
    #can change this to be part of main window if needed??)
    preferences_window.title("Preferences")

    #Load preferences from preferences.json file and store in dictionary
    with open('preferences.json', 'r') as file:
        current_preferences_states = json.load(file)

    with open('preset-preferences.json', 'r') as file:
        preset_preferences = json.load(file)
        #get the names of the presets from the list of dictionaries and store them in a list
        preset_preference_names = [preset['name'] for preset in preset_preferences]

    #Create frame to hold checkboxes
    checkboxes_frame = ttk.Frame(preferences_window, padding="20")
    checkboxes_frame.pack()

    #Create da checkboxes with boolean vars - true=ticked false=not ticked
    checkbox1_var = tk.BooleanVar(value=current_preferences_states['show-line-numbers'])
    checkbox1 = ttk.Checkbutton(checkboxes_frame, text="Show line numbers", variable=checkbox1_var)
    checkbox1.pack()

    checkbox2_var = tk.BooleanVar(value=current_preferences_states['auto-save'])
    checkbox2 = ttk.Checkbutton(checkboxes_frame, text="Auto-save", variable=checkbox2_var)
    checkbox2.pack()

    checkbox3_var = tk.BooleanVar(value=current_preferences_states['Option 3'])
    checkbox3 = ttk.Checkbutton(checkboxes_frame, text="Option 3", variable=checkbox3_var)

    checkbox3.pack()

    def on_dropdown_selection(event):
        selected_preset = dropdown.get()
        print(selected_preset)
        update_current_preferences_to_selected_preset(selected_preset)

    dropdown = ttk.Combobox(checkboxes_frame, values=preset_preference_names)
    dropdown.current(0)
    dropdown.pack()

    dropdown.bind("<<ComboboxSelected>>", on_dropdown_selection)

    #Create da frame to hold da slider
    slider_frame = ttk.Frame(preferences_window, padding="20")
    slider_frame.pack()

    #Create da label for da slider
    slider_label = ttk.Label(slider_frame, text=f"Slider: {current_preferences_states['Slider']}")
    slider_label.pack(side="left")

    #Create da slider
    slider_var = tk.IntVar(value=current_preferences_states['Slider'])
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