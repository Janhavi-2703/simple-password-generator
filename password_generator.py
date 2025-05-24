import random
import string
from tkinter import Tk, Label, Entry, Button, StringVar, IntVar, messagebox, Checkbutton, ttk

def generate_password():
    try:
        length = length_slider.get()
        if length < 6:
            messagebox.showerror("Error", "Password length must be at least 6!")
            return

        # Collect character groups based on user preferences
        char_groups = []
        if include_lowercase.get():
            char_groups.append(string.ascii_lowercase)
        if include_uppercase.get():
            char_groups.append(string.ascii_uppercase)
        if include_digits.get():
            char_groups.append(string.digits)
        if include_special.get():
            char_groups.append(string.punctuation)

        if not char_groups:
            messagebox.showerror("Error", "Select at least one character type!")
            return

        # Ensure balanced distribution of character types
        password = []
        for group in char_groups:
            password.append(random.choice(group))

        # Fill the rest of the password with a random selection from all groups
        all_chars = ''.join(char_groups)
        password += [random.choice(all_chars) for _ in range(length - len(password))]
        random.shuffle(password)  # Shuffle to remove predictable order

        password_var.set(''.join(password))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Main GUI
root = Tk()
root.title("Simple Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# Style
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))

# Password Length
Label(root, text="Password Length:").pack(pady=10)
length_slider = ttk.Scale(root, from_=6, to=32, orient="horizontal", length=300)
length_slider.set(12)
length_slider.pack()

# Character Type Selection
include_lowercase = IntVar(value=1)
include_uppercase = IntVar(value=1)
include_digits = IntVar(value=1)
include_special = IntVar(value=1)

Checkbutton(root, text="Include Lowercase Letters", variable=include_lowercase, font=("Arial", 10)).pack(anchor="w", padx=50)
Checkbutton(root, text="Include Uppercase Letters", variable=include_uppercase, font=("Arial", 10)).pack(anchor="w", padx=50)
Checkbutton(root, text="Include Digits", variable=include_digits, font=("Arial", 10)).pack(anchor="w", padx=50)
Checkbutton(root, text="Include Special Characters", variable=include_special, font=("Arial", 10)).pack(anchor="w", padx=50)

# Generate Password Button
Button(root, text="Generate Password", command=generate_password, bg="#4682b4", fg="white", font=("Arial", 12)).pack(pady=20)

# Display Password
password_var = StringVar()
Label(root, text="Generated Password:").pack(pady=10)
Entry(root, textvariable=password_var, font=("Arial", 12), state="readonly", justify="center").pack(pady=5)

# Copy to Clipboard Button
Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#4682b4", fg="white", font=("Arial", 12)).pack(pady=10)

# Run the application
root.mainloop()
