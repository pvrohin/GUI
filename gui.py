import tkinter as tk

class RectangleDrawer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Rectangle Drawer")

        self.image_path = image_path

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.rectangles = []

        self.load_image()

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_path)
        self.canvas.config(width=self.image.width(), height=self.image.height())
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline='red')

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_button_release(self, event):
        self.end_x = event.x
        self.end_y = event.y

        self.rectangles.append((self.start_x, self.start_y, self.end_x, self.end_y))

    def save_coordinates(self):
        with open("coordinates.txt", "w") as f:
            for rect in self.rectangles:
                f.write(f"{rect}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleDrawer(root, "img.png")
    root.mainloop()
    app.save_coordinates()
