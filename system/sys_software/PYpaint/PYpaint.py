import tkinter as tk

class Paint(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        self.x = None
        self.y = None

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.end_draw)

    def start_draw(self, event):
        self.x = event.x
        self.y = event.y

    def draw(self, event):
        self.canvas.create_line(self.x, self.y, event.x, event.y, width=5)
        self.x = event.x
        self.y = event.y

    def end_draw(self, event):
        self.x = None
        self.y = None

if __name__ == "__main__":
    root = tk.Tk()
    paint = Paint(root)
    paint.pack()
    root.mainloop()