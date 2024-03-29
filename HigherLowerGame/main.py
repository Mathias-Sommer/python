import tkinter as tk
from tkinter import ttk, messagebox
import form2

def login(event=None):
    username = username_entry.get()
    password = password_entry.get()

    # hardcoded admin:password, here you would query sql database to check if user exists with right credentials.
    if username == "admin" and password == "password":
        root.destroy() 
        game = form2.HigherLowerGame()       
        game.run()

    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create placeholder text in textboxes "username" "password", then removes the placeholder text if focused.
def on_username_entry_click(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, tk.END)
        username_entry.configure(foreground="black")

def on_username_entry_leave(event):
    if not username_entry.get():
        username_entry.insert(0, "Username")
        username_entry.configure(foreground="grey")

def on_password_entry_click(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, tk.END)
        password_entry.configure(show="*", foreground="black")

def on_password_entry_leave(event):
    if not password_entry.get():
        password_entry.insert(0, "Password")
        password_entry.configure(show="", foreground="grey")

root = tk.Tk()
root.title("Login")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Center form to screen
window_width = 250
window_height = 140
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)

style = ttk.Style()
style.configure("TEntry", font=("Arial", 10))
style.configure("TLabel", foreground="blue", font=("Helvetica", 10, "bold"))

username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

username_entry = ttk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)
username_entry.insert(0, "Username")
username_entry.configure(foreground="grey")
username_entry.bind("<FocusIn>", on_username_entry_click)
username_entry.bind("<FocusOut>", on_username_entry_leave)

password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

password_entry = ttk.Entry(root, show="")
password_entry.grid(row=1, column=1, padx=10, pady=5)
password_entry.insert(0, "Password")
password_entry.configure(foreground="grey")
password_entry.bind("<FocusIn>", on_password_entry_click)
password_entry.bind("<FocusOut>", on_password_entry_leave)

# Added onkeypress "enter" to toggle login function
root.bind("<Return>", login)

login_button = ttk.Button(root, text="Login", command=login, style="TButton")
login_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="we")

root.mainloop()