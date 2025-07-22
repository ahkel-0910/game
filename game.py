import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                    filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"Notepad - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                    filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"Notepad - {file_path}")

def exit_app():
    if messagebox.askokcancel("Exit", "Do you want to quit?"):
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Notepad")
root.geometry("800x600")

# Create text area
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=1)

# Create menu
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add menu to window
root.config(menu=menu_bar)

# Run the application
root.mainloop()
