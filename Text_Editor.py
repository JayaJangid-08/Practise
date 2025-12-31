import tkinter as tk
from tkinter import filedialog, messagebox
# Function to create a new file
def new_file():
    text.delete(1.0, tk.END) # Clear existing text
# Open a new file dialog
def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
            with open(file_path, 'r') as file:
                text.delete(1.0, tk.END)  # Clear existing text
                text.insert(tk.END, file.read())
# Save the current file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files", "*.txt")])
    if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get(1.0, tk.END))
                messagebox.showinfo("Save File", "File saved successfully!")
# Main application window
root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("800x600")
# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
# File menu commands
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
# Text area
text = tk.Text(root, wrap=tk.WORD, font=("calibri", 12))
text.pack(expand=tk.YES, fill=tk.BOTH)
# Start the main event loop
root.mainloop()