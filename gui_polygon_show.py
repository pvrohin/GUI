import tkinter as tk

class ShapeViewer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Custom Shape Viewer")

        self.image_path = image_path

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.load_image()
        self.load_shapes()

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_path)
        self.canvas.config(width=self.image.width(), height=self.image.height())
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

    def load_shapes(self):
        with open("shapes.txt", "r") as f:
            for line in f:
                coords = eval(line.strip())
                self.canvas.create_polygon(coords, fill="green", outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeViewer(root, "img.png")
    root.mainloop()
