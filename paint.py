from tkinter import *
from tkinter import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL
from PIL import ImageGrab as ImageGrab


class Paint:
    def __init__(self, master):
        self.master = master
        self.master.state("zoomed")
        self.master.title("Paint with Seedy & Nega")
        # Variables
        self.pen_color = "black"
        self.eraser_color = "white"
        self.select_color = StringVar(value="black")
        # Create frames
        self.color_frame = LabelFrame(self.master, text="Color", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
        self.color_frame.place(x=0, y=0, width=1500, height=150)

        self.tool_frame = LabelFrame(self.master, text="Tool", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
        self.tool_frame.place(x=200, y=70, width=424, height=60)

        self.pen_size = LabelFrame(self.master, text="Size", relief=RIDGE, bg="white", font=("arial", 15, "bold"))
        self.pen_size.place(x=700, y=70, width=224, height=60)

        # Create canvas
        self.canvas = Canvas(self.master, bg="white", bd=5, relief=GROOVE, height=400, width=1325)
        self.canvas.place(x=10, y=100)

        # Create widgets
        self.color_btn = Button(self.color_frame, bg="black", command=self.select_color)
        self.color_btn.place(x=10, y=10, width=50, height=50)

        self.eraser_btn = Button(self.tool_frame, text="Eraser", command=self.eraser)
        self.eraser_btn.place(x=10, y=10, width=50, height=40)

        self.clear_btn = Button(self.tool_frame, text="Clear", command=self.clear)
        self.clear_btn.place(x=70, y=10, width=50, height=40)

        self.save_btn = Button(self.tool_frame, text="Save", command=self.saved)
        self.save_btn.place(x=130, y=10, width=50, height=40)

        self.pen_size_scale = Scale(self.pen_size, from_=1, to=20, orient=HORIZONTAL)
        self.pen_size_scale.set(5)
        self.pen_size_scale.place(x=10, y=10, width=200)

        self.color_btn = Button(self.color_frame, bg="black", command=self.select_color)

        # Bind events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.window = window
        self.brush_size = 10
        self.brush_color = "black"
        self.canv = Canvas(self.window, bg="white", width=600, height=600)
        self.canv.pack()
    def __str__(self):
        pass
    def canvas_color(self):
        color = colorchooser.askcolor()
        self.canvas.configure(bg=color[1])
        self.eraser_color = color[1]

    def saved(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
        x = self.master.winfo_rootx() + self.canvas.winfo_x()
        y = self.master.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_name)
        messagebox.showinfo("Point Notification", "Image is saved as" + str(file_name))

    def eraser(self):
        self.pen_color = self.eraser_color

    def clear(self):
        self.canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canv.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def set_brush_size(self, size):
        self.brush_size = size

    def set_brush_color(self, color):
        self.brush_color = color

    def select_color(self):
        color = colorchooser.askcolor()
        if color:
            self.pen_color = color[1]
            self.select_color.set(self.pen_color)


if __name__ == '__main__':
    window = Tk()
    window.state("zoomed")
    window.title("Paint with Seedy & Nega")
    paint_app = Paint(window)

    size_frame = Frame(window)
    size_frame.pack(side=LEFT, padx=10)
    brush_size_lbl = Label(size_frame, text="Brush Size")
    brush_size_lbl.pack()
    size_slider = Scale(size_frame, from_=1, to=50, command=paint_app.set_brush_size, orient=VERTICAL)
    size_slider.set(paint_app.brush_size)
    size_slider.pack()

    color_frame = Frame(window)
    color_frame.pack(side=LEFT)
    brush_color_lbl = Label(color_frame, text="Brush Color")
    brush_color_lbl.pack()
    colors = ["black", "red", "blue", "green", "orange", "purple", "yellow"]
    for color in colors:
        color_btn = Button(color_frame, bg=color, width=2, command=lambda c=color: paint_app.set_brush_color(c))
        color_btn.pack(pady=5)

    window.mainloop()
