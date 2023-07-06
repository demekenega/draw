from tkinter import *
from tkinter import filedialog, messagebox, colorchooser

from PIL import ImageGrab


#Colors


class PaintApp(Tk):

    def __init__(self):
        super().__init__()

        # Initialize variables
        self.pen_color = "black"
        self.eraser_color = "white"
        self.pen_size = 1

        self.state("zoomed")
        self.title("Paint with Seedy & Nega")

        self.colorsTool = ['#FF0000', "#008000", "#FFC0CB", "#FFA500", "#FFFF00", "#008000", "#0000FF", "#A52A2A",
                           "#FFB6C1", "#FF69B4", "#FF1493", "#C71585", "#DB7093", "#FFA07A", "#FF7F50", "#FF6347",
                           "#FF4500", "#FF8C00", "#FFA500", "#FFD700", "#FFFF00", "#FFFFE0", "#FFFACD", "#FAFAD2",
                           "#FFEFD5", "#FFE4B5", "#FFDAB9", "#EEE8AA", "#F0E68C", "#BDB76B", "#E6E6FA", "#D8BFD8",
                           "#DDA0DD", "#EE82EE", "#DA70D6", "#FF00FF", "#FF00FF", "#BA55D3", "#9370DB", "#663399",
                           "#8A2BE2", "#9400D3", "#9932CC", "#8B008B", "#800080", "#4B0082", "#6A5ACD", "#483D8B",
                           "#7B68EE", "#ADFF2F", "#7FFF00", "#7CFC00", "#00FF00", "#32CD32", "#98FB98", "#90EE90",
                           "#00FA9A", "#00FF7F", "#3CB371", "#2E8B57", "#228B22", "#008000", "#006400", "#9ACD32",
                           "#6B8E23", "#808000", "#556B2F", "#66CDAA", "#8FBC8B", "#20B2AA", "#008B8B", "#008080",
                           "#00FFFF", "#00FFFF", "#E0FFFF", "#AFEEEE", "#7FFFD4", "#40E0D0", "#48D1CC", "#00CED1",
                           "#5F9EA0", "#4682B4", "#B0C4DE", "#B0E0E6", "#ADD8E6", "#87CEEB", "#87CEFA", "#00BFFF",
                           "#1E90FF", "#6495ED", "#7B68EE", "#4169E1", "#0000FF", "#0000CD", "#00008B", "#000080",
                           "#191970", "#FFF8DC", "#FFEBCD", "#FFE4C4", "#FFDEAD", "#F5DEB3", '#DEB887', "#D2B48C",
                           "#BC8F8F", "#F4A460", "#DAA520", "#B8860B", "#CD853F", "#D2691E", "#8B4513", "#A0522D",
                           "#A52A2A", "#800000", "#FFFFFF", "#FFFAFA", "#F0FFF0", "#F5FFFA", "#F0FFFF", "#F0F8FF",
                           "#F8F8FF", "#F5F5F5", "#F5F5F5", "#F5F5DC", "#FDF5E6", "#FFFAF0", "#FFFFF0", "#FAEBD7",
                           "#FAF0E6", "#FFF0F5", "#FFE4E1", "#DCDCDC", "#D3D3D3", "#C0C0C0", "#A9A9A9", "#808080",
                           "#696969", "#778899", "#708090", ]

        self.createColorBar()

        # Create the canvas
        self.canvas = Canvas(self, bg="white", bd=5, relief=GROOVE, height=700, width=1515)
        self.canvas.place(x=15, y=100)

        # Create the buttons
        #self.color_button = Button(self, text="Pen Color", bd=3, bg="white", relief=RIDGE, width=8, command=self.select_color)
        self.save_button = Button(self, text="Save", bd=4, bg="white", command=self.save)
        self.eraser_button = Button(self, text="Erase", bd=4, bg="white", command=self.eraser)
        self.clear_button = Button(self, text="Clear", bd=4, bg="white", command=self.clear)

        # Create the pen size scale
        self.pen_size_scale = Scale(self, orient=HORIZONTAL, from_=1, to=100, length=170)
        self.pen_size_scale.set(1)

        # Layout the widgets
        #self.color_button.grid(row=0, column=0, padx=2)
        self.save_button.grid(row=0, column=0, padx=2)
        self.eraser_button.grid(row=0, column=1, padx=2)
        self.clear_button.grid(row=0, column=2, padx=2)
        self.pen_size_scale.grid(row=1, column=0)

        # Bind the mouse events
        self.canvas.bind("<B1-Motion>", self.paint)

    def select_color(self, col):
        # color = colorchooser.askcolor()
        # self.pen_color = color[1]
        self.pen_color = col

    def createColorBar(self):
        i = j = 0
        for color in self.colorsTool:
            Button(self, bd=3, bg=color, relief=RIDGE, width=3,
                   command=lambda col=color: self.select_color(col)).grid(row=j, column=i, padx=1)
            i = i + 1
            if i == 42:
                j = j + 1
                i = 0
                Button(self, bd=3, bg=color, relief=RIDGE, width=3,
                       command=lambda col=color: self.select_color(col)).grid(
                    row=j, column=i, padx=1, rowspan=2)

    def save(self):
        file_name = filedialog.asksaveasfilename(defaultextension=".jpg")
        x = self.winfo_rootx() + self.canvas.winfo_x()
        y = self.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_name)
        messagebox.showinfo("Point Notification", "Image is saved as " + str(file_name))

    def eraser(self):
        self.pen_color = self.eraser_color

    def clear(self):
        self.canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.pen_color, outline=self.pen_color,
                                width=self.pen_size_scale.get())


if __name__ == "__main__":
    app = PaintApp()
    app.mainloop()