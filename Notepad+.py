from tkinter import *
from tkinter import filedialog, messagebox, font
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from tkinter import font

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad+")
        self.icon_image = Image.open("ico.png")
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)
        self.root.iconphoto(True, self.icon_photo)
        self.root.file_path = None  # Variable to store the file path
        

        # Create a Text widget
        self.text_widget =  Text(self.root, undo=True,cursor=None)
        self.text_widget.pack(expand=True, fill=BOTH)

        # Create a menu bar
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create a File menu
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", accelerator="Ctrl+N", command=self.new_file)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", accelerator="Alt+F4", command=self.exit)

        # Create an Edit menu
        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", command=self.undo)
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", command=self.cut)
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", command=self.copy)
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", command=self.paste)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", accelerator="Ctrl+A", command=self.select_all)

        # Create a Format menu
        self.format_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.change_font)

        # Create a Help menu
        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)

        # Create a right-click context menu
        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Cut", command=self.cut)
        self.context_menu.add_command(label="Copy", command=self.copy)
        self.context_menu.add_command(label="Paste", command=self.paste)

        # Bind keyboard shortcuts
        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-S>", lambda event: self.save_file_as())
        self.root.bind("<Control-z>", lambda event: self.undo())
        self.root.bind("<Control-y>", lambda event: self.redo())
        self.root.bind("<Control-x>", lambda event: self.cut())
        self.root.bind("<Control-c>", lambda event: self.copy())
        self.root.bind("<Control-v>", lambda event: self.paste())
        self.root.bind("<Control-a>", lambda event: self.select_all())
        self.root.bind("<Control-A>", lambda event: self.select_all())

        # Bind right-click context menu
        self.text_widget.bind("<Button-3>", self.show_context_menu)
    def make_link2(self):
      urle="https://github.com/joshckar/Notepad-.git"
      webbrowser.open(urle)

    def make_link(self):
      urle="https://t.me/Notepad3"
      webbrowser.open(urle)

    def make_link1(self):
     url="https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp2cnfDPn-xsEx5OQBb1pMWUhU9lENxvjFvIeAJvVJaNVSGnaVdl7w4duc2X0Uzp6y61DAsD&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1611133315%3A1705222600256261&theme=glif"
     webbrowser.open(url)

    def new_file(self):
        self.text_widget.delete(1.0, END)
        self.file_path = None

    def open_file(self):
        file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.text_widget.delete(1.0, END)
            self.text_widget.insert(1.0, file.read())
            self.file_path = file.name
            file.close()
    
    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w") as file:
                file.write(self.text_widget.get(1.0, END))
        else:
            self.save_file_as()

    def save_file_as(self):
        file = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            file.write(self.text_widget.get(1.0, END))
            self.file_path = file.name
            file.close()

    def exit(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    def undo(self):
        try:
            self.text_widget.edit_undo()
        except TclError:
            pass

    def redo(self):
        try:
            self.text_widget.edit_redo()
        except TclError:
            pass

    def cut(self):
        self.text_widget.event_generate("<<Cut>>")

    def copy(self):
        self.text_widget.event_generate("<<Copy>>")

    def paste(self):
        self.text_widget.event_generate("<<Paste>>")

    def select_all(self):
        self.text_widget.tag_add("sel", "1.0", "end")

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)

    def  about (self):
     win = tk.Tk()
     win.title("About Notepad")
     win.geometry("400x400+300+200")
     lebel = ttk.Label(win,text="About in Notepad+",font="Arial 23")
     lebel.pack()
     lebel1 = ttk.Label(win,text="____________________________________________________",font="Arial 10")
     lebel1.pack()
     win.resizable(False,False)
     lebel_text = ttk.Label(win,text="""Version 01 (Build 7601: Service Pack 1)
Copyright 2024 Ahmadi Company.
All rights reserved. operating system and its user
The interface is protected by trademark and other pings
Intellectual property rights in the Islamic Republic of Iran and 
other cases.

Thank you for using this app from our team ♥

""",font="Arial 10")
     lebel_text.place(x=20 ,y=90)
     lebel_ = ttk.Label(win,text="____________________________________________________",font="Arial 10")
     lebel_.place(x=20,y=240)
     lebel_programmer = ttk.Label(win, text="Programmer  Mohammad Hossein Ahmadi ",font="Arial 10",foreground="#000")
     lebel_programmer.place(x= 20,y=365)
     lebel_email = ttk.Button(win,text="Support email : this.pc.ma@gmail.com",command=self.make_link1)
     lebel_email.place(x=20,y=270)
     lebel_telegram=ttk.Button(win,text="Telegram channel : Notepad+    " ,command=self.make_link)
     lebel_telegram.place(x=20,y=299)
     lebel_telegram=ttk.Button(win,text="Link Github   " ,command=self.make_link2)
     lebel_telegram.place(x=20,y=330)
     win.mainloop()
     win.mainloop()
     

    def change_font(self):
        font_dialog = font.Font(family=self.text_widget["font"].split()[0])
        font_chosen = font_dialog.actual()
        font_chosen = font.families()[0] if not font_chosen else font_chosen["family"]
        size_chosen = font_dialog.actual()["size"]
        size_chosen = 12 if not size_chosen else size_chosen

        def apply_changes():
            font_name = font_var.get()
            font_size = size_var.get()
            self.text_widget.configure(font=(font_name, font_size))

        font_dialog = Toplevel(self.root)
        font_dialog.title("Set Font")
        font_dialog.geometry("300x200")
        font_dialog.resizable(False, False)

        font_label = Label(font_dialog, text="Font:")
        font_label.pack()

        font_var = StringVar(font_dialog)
        font_var.set(font_chosen)
        font_dropdown = ttk.Combobox(font_dialog, textvariable=font_var)
        font_dropdown["values"] = font.families()
        font_dropdown.pack()

        size_label = ttk.Label(font_dialog, text="Size:")
        size_label.place(x=133,y=60)

        size_var = IntVar(font_dialog)
        size_var.set(size_chosen)
        size_dropdown = Scale(font_dialog, from_=8, to=72, orient=HORIZONTAL, variable=size_var)
        size_dropdown.place(x=90,y=80)
        
        apply_button = ttk.Button(font_dialog, text="Apply",command=apply_changes)
        apply_button.place(x=110,y=160)

# Create the main window
root = Tk()



# Create an instance of the Notepad class
notepad = Notepad(root)

# Run the application
root.mainloop()
