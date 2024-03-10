import tkinter as tk

class RectangleViewer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Rectangle Viewer")

        self.image_path = image_path

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.load_image()

        self.draw_rectangles()

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_path)
        self.canvas.config(width=self.image.width(), height=self.image.height())
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

    def draw_rectangles(self):
        with open("coordinates.txt", "r") as f:
            for line in f:
                coords = eval(line.strip())
                self.canvas.create_rectangle(coords, outline='green', width=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleViewer(root, "img.png")
    root.mainloop()
