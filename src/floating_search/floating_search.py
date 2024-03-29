import tkinter as tk
import keyboard
import pyautogui

def show_window():
    root.deiconify()
    root.attributes('-topmost', True)  # Make the window pop to the front
    root.attributes('-topmost', False)  # Allow other windows to be in front

def hide_window(event=None):
    root.withdraw()

def hotkey_pressed(event):
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('alt') and keyboard.is_pressed('+'):
        show_window()

def move_window(event):
    pyautogui.move(10, 10)  # Adjust as needed

root = tk.Tk()
root.geometry('300x200')
root.title('Background Service with Hotkey')

# Hide the window initially
root.withdraw()

# Listen for the hotkey combination
keyboard.on_press(hotkey_pressed)

# Bind Ctrl+Q to hide the window
root.bind('<Control-q>', hide_window)

# Bind Ctrl+M to move the window
root.bind('<Control-m>', move_window)

# Create a label in the window
label = tk.Label(root, text='Hotkey combination pressed!')
label.pack(padx=20, pady=50)

root.mainloop()
