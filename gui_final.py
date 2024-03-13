import tkinter as tk
from PIL import Image, ImageTk
import time

class ShapeDrawer:
    def __init__(self, root, image_path):
        self.root = root
        self.root.title("Custom Shape Drawer")

        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set root window geometry to fill the entire screen
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Load and resize the image while maintaining aspect ratio
        self.image = Image.open(image_path)
        self.image.thumbnail((screen_width, screen_height))

        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.place(x=0, y=0)  # Place canvas at (0, 0)

        # Convert the resized image to Tkinter PhotoImage
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        self.shapes = []

        self.canvas.bind("<Button-1>", self.on_button_click)
        self.canvas.bind("<B1-Motion>", self.on_button_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

        # Add a label to display the timer with increased font size
        self.timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))  # Increase font size to 24
        self.timer_label.place(x=10, y=10)  # Place timer label at (10, 10)

        # Add an "OK" button to close the window
        self.ok_button = tk.Button(root, text="OK", command=self.close_and_show_shapes)
        self.ok_button.place(x=10, y=50)  # Place OK button below the timer label

        # Start the timer
        self.start_time = time.time()
        self.update_timer()

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

    def close_and_show_shapes(self):
        self.save_shapes()
        self.root.destroy()
        show_shapes(self.start_time)

class ShapeViewer:
    def __init__(self, root, image_path, time_taken):
        self.root = root
        self.root.title("Custom Shape Viewer")

        # Get the screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Set root window geometry to fill the entire screen
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Load and resize the image while maintaining aspect ratio
        self.image = Image.open(image_path)
        self.image.thumbnail((screen_width, screen_height))

        self.canvas = tk.Canvas(root, width=self.image.width, height=self.image.height)
        self.canvas.place(x=0, y=0)  # Place canvas at (0, 0)

        # Convert the resized image to Tkinter PhotoImage
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo_image)

        self.time_taken = time_taken

        self.load_shapes()
        self.display_time_taken()

    def load_shapes(self):
        with open("shapes.txt", "r") as f:
            for line in f:
                coords = eval(line.strip())
                self.canvas.create_polygon(coords, fill="green", outline="black")

    def display_time_taken(self):
        time_label = tk.Label(self.root, text=f"Time taken: {self.format_time(self.time_taken)}", font=("Helvetica", 24))  # Increase font size to 24
        time_label.place(x=10, y=10)  # Place time label at (10, 10)

    def format_time(self, seconds):
        return time.strftime("%H:%M:%S", time.gmtime(seconds))

def show_shapes(start_time):
    root = tk.Tk()
    app = ShapeViewer(root, "img_real.png", time.time() - start_time)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root, "img_real.png")
    root.mainloop()
