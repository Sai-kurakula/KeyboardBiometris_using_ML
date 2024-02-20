import tkinter as tk
from tkinter import messagebox

import code1

def validate_password():
    entered_password = password_entry.get()
    print("Entered Password:", entered_password)

    # You can add your password validation logic here
    # For simplicity, let's assume the correct password is "password123"
    correct_password = "password123"

    if entered_password == correct_password:
        messagebox.showinfo("Success", "Password is correct!")
    else:
        messagebox.showerror("Error", "Incorrect password. Please try again.")



# Create the main window
window = tk.Tk()
window.title("Password Entry")

# Create and place the password label and entry field
password_label = tk.Label(window, text="Enter Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(window, show="*")  # The 'show' option hides the entered characters
password_entry.pack(pady=10)

# Create and place the login button
login_button = tk.Button(window, text="Login", command=validate_password)
login_button.pack(pady=10)



# Run the Tkinter event loop
window.mainloop()
