import tkinter as tk


def say_hello():
    name = entry.get()
    if name.strip():
        label.config(text=f"Hello, {name}!")
    else:
        label.config(text="Hello, World!")


# Create the main window
root = tk.Tk()
root.title("Simple Tkinter Example")
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=5)

# Add a text entry field
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Add a button
button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
