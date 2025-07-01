import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")  # Title of the window

# Function to center the window on the screen
def centerIt(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")  # Set window size and position

# Center the root window with 300x200 size
centerIt(root, 300, 200)

# Label to instruct the user
label = tk.Label(root, text="Please enter the time in seconds:")
label.pack(pady=20)  # Add vertical padding

# Entry widget to input time
entry = tk.Entry(root)
entry.pack()

# Start button click handler
def startTimer():
    user_input = entry.get()

    # Input validation: must not be empty or contain letters
    if user_input.strip() == "" or not user_input.isdigit():
        messagebox.showwarning("Warning", "Please enter a valid number!")
    else:
        duration = int(user_input)
        countdown(duration)  # Start countdown

# Recursive countdown function using after()
def countdown(seconds_left):
    hours = seconds_left // 3600
    minutes = (seconds_left % 3600) // 60
    seconds = seconds_left % 60

    # Update the label to show current countdown
    label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")

    if seconds_left > 0:
        # Call countdown again after 1 second
        root.after(1000, countdown, seconds_left - 1)
    else:
        # When countdown finishes
        messagebox.showinfo("Done", "Countdown completed!")

# Button to start the timer
button = tk.Button(root, text="Start", command=startTimer)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
