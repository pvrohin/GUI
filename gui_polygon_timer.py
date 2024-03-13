import tkinter as tk
import time

class ShapeDrawer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Custom Shape Drawer")

        self.image_path = image_path

        self.canvas = tk.Canvas(root)
        self.canvas.pack()

        self.shapes = []

        self.load_image()

        self.canvas.bind("<Button-1>", self.on_button_click)
        self.canvas.bind("<B1-Motion>", self.on_button_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        # Add a label to display the timer
        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 16))
        self.timer_label.pack()

        # Start the timer
        self.start_time = time.time()
        self.update_timer()

        # Add an "OK" button to close the window
        self.ok_button = tk.Button(root, text="OK", command=self.close_window)
        self.ok_button.pack()

    def load_image(self):
        self.image = tk.PhotoImage(file=self.image_path)
        self.canvas.config(width=self.image.width(), height=self.image.height())
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

    def on_button_click(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.current_shape = []

    def on_button_drag(self, event):
        x, y = event.x, event.y
        self.canvas.create_line(self.start_x, self.start_y, x, y)
        self.current_shape.extend([x, y])

    def on_button_release(self, event):
        self.end_x = event.x
        self.end_y = event.y

        self.shapes.append(self.current_shape)

    def save_shapes(self):
        with open("shapes.txt", "w") as f:
            for shape in self.shapes:
                f.write(f"{shape}\n")

    def update_timer(self):
        current_time = time.strftime("%H:%M:%S", time.gmtime(time.time() - self.start_time))
        self.timer_label.config(text=current_time)
        self.root.after(1000, self.update_timer)  # Update timer label every second

    def close_window(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root, "img.png")
    root.mainloop()
    app.save_shapes()
