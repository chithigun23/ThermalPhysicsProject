import os
import subprocess
import tkinter as tk

# Get the path to the directory this script is in
script_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to your applications
apps = {
    "Fermi Levels": os.path.join(script_dir, "..", "Fermi Levels", "v1.1 - Fermi ground state tkinter.py"),
    "Gas Mixing": os.path.join(script_dir, "..", "Gas Mixing", "v1.2.py"),
    "Ferromagnets": os.path.join(script_dir, "..", "Ferromagnets", "v1.2 - Tkinter.py"),
    "Paramagnets": os.path.join(script_dir, "..", "Paramagnets", "v4.1 - combined graphs.py"),
    # Add additional applications here
}

def run_app(path):
    """Run an application, then destroy the root window to close the menu"""
    root.destroy()
    subprocess.Popen(["python", path]) 

# Create the main window
root = tk.Tk()
root.title("Thermal Physics Apps")

# Create a title label
title_label = tk.Label(root, text="Thermal Physics Apps", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create a button for each application
for app, path in apps.items():
    button = tk.Button(button_frame, text=app, command=lambda path=path: run_app(path), width=30)
    button.pack(pady=5)

# Create a label for the author information
author_label = tk.Label(root, text="By: Chithi Gunatilake")
author_label.pack(pady=10)

root.mainloop()
