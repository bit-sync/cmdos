import tkinter as tk
import tkinter.filedialog

class Notepad:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PYpad")

        self.text = tk.Text(self.root)
        self.text.pack()

        self.file_menu = tk.Menu(self.root)
        self.root.config(menu=self.file_menu)

        self.new_file_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="New", menu=self.new_file_menu)
        self.new_file_menu.add_command(label="New File", command=self.new_file)

        self.open_file_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Open", menu=self.open_file_menu)
        self.open_file_menu.add_command(label="Open File", command=self.open_file)

        self.save_file_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Save", menu=self.save_file_menu)
        self.save_file_menu.add_command(label="Save File", command=self.save_file)

        self.quit_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Quit", menu=self.quit_menu)
        self.quit_menu.add_command(label="Quit", command=self.quit)

    def new_file(self):
        self.text.delete("1.0", tk.END)

    def open_file(self):
        file = tk.filedialog.askopenfile(parent=self.root, title="Open File")
        if file:
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", file.read())

    def save_file(self):
        file = tk.filedialog.asksaveasfile(parent=self.root, title="Save File")
        if file:
            file.write(self.text.get("1.0", tk.END))

    def quit(self):
        self.root.destroy()

if __name__ == "__main__":
    notepad = Notepad()
    notepad.root.mainloop()

