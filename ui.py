 
import tkinter as tk
from constants import CANVAS_W, CANVAS_H, BG_COLOR

class UI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.size_r = {"S": 12, "M": 28, "L": 45}

        # drawing area
        self.canvas = tk.Canvas(root, width=CANVAS_W, height=CANVAS_H, bg=BG_COLOR, highlightthickness=0)
        self.canvas.pack(side=tk.TOP, fill=tk.NONE)

        # controls area
        controls = tk.Frame(root, bg="#f2f2f2")
        controls.pack(side=tk.BOTTOM, fill=tk.X, anchor="w")

        # Row 1: size buttons
        size_row = tk.Frame(controls, bg="#f2f2f2")
        size_row.pack(pady=(10, 5), anchor="w")
        tk.Label(size_row, text="Size:", bg="#f2f2f2").pack(side=tk.LEFT, padx=(10, 6))

        # circle buttons
        for code in ["S", "M", "L"]:
            r = self.size_r[code]
            diameter = r * 2

            c = tk.Canvas(
                size_row,
                width=diameter + 6,
                height=diameter + 6,
                bg="#f2f2f2",
                highlightthickness=0,
            )
            c.pack(side=tk.LEFT, padx=10)

            c.create_oval(
                3, 3,
                diameter + 3, diameter + 3,
                fill="#bfbfbf",
                outline="#969696"
            )

            c.bind("<Button-1>", lambda e, code=code: self.controller.handle_add_ball(code))

        # Row 2: color buttons
        color_row = tk.Frame(controls, bg="#f2f2f2")
        color_row.pack(pady=5, anchor="w")
        tk.Label(color_row, text="Color:", bg="#f2f2f2").pack(side=tk.LEFT, padx=(10, 6))

        # color buttons row
        def make_color_square(parent, color_hex):
            size = 24  
            c = tk.Canvas(
                parent,
                width=size,
                height=size,
                bg="#000000",
                highlightthickness=0,
                cursor="hand2"
            )
            c.pack(side=tk.LEFT, padx=15)
            # draw a square
            c.create_rectangle(2, 2, size-2, size-2, fill=color_hex, outline=color_hex)
            # click 
            c.bind("<Button-1>", lambda e: self.controller.handle_set_color(color_hex))

        # color square button
        make_color_square(color_row, "#ff3b30")  # red
        make_color_square(color_row, "#007aff")  # blue
        make_color_square(color_row, "#fff04d")  # yellow

        # Row 3: kontrol buttons
        run_row = tk.Frame(controls, bg="#f2f2f2")
        run_row.pack(pady=(5, 12), anchor="w")

        tk.Button(run_row, text="START",  command=self.controller.start).pack(side=tk.LEFT, padx=6)
        tk.Button(run_row, text="STOP",   command=self.controller.stop).pack(side=tk.LEFT, padx=6)
        tk.Button(run_row, text="RESET",  command=self.controller.reset).pack(side=tk.LEFT, padx=6)
        tk.Button(run_row, text="Speed Up", command=self.controller.speed_up).pack(side=tk.LEFT, padx=20)

    

    # Accessor of controller
    def get_canvas(self):
        return self.canvas