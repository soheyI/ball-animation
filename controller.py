
import random
from constants import CANVAS_W, CANVAS_H, FPS_MS
from ui import UI
from ball import Ball

class Controller:
    def __init__(self, root):
        self.root = root
        self.ui = UI(root, self)
        self.canvas = self.ui.get_canvas()

        # State
        self.balls = []
        self.current_color = "#ff3b30" 
        self.running = False

        # pixel radii for sizes
        self.size_r = {"S": 12, "M": 28, "L": 45}

    # UI callback
    def handle_set_color(self, color_hex):
        self.current_color = color_hex

    def handle_add_ball(self, size_code):
        r = self.size_r[size_code]
        # spawn inside bounds
        x = random.uniform(r + 2, CANVAS_W - r - 2)
        y = random.uniform(r + 2, CANVAS_H - r - 2)
        b = Ball(x, y, r, self.current_color)
        b.draw(self.canvas)
        self.balls.append(b)

    # Run controls
    def start(self):
        if not self.running:
            self.running = True
            self._tick()

    def stop(self):
        self.running = False

    def reset(self):
        self.stop()
        for b in self.balls:
            if b.item_id is not None:
                self.canvas.delete(b.item_id)
        self.balls.clear()

    def speed_up(self):
        for b in self.balls:
            b.speed *= 1.25

    # Animation loop
    def _tick(self):
        if not self.running:
            return
        for b in self.balls:
            b.update(FPS_MS, CANVAS_W, CANVAS_H)
            b.draw(self.canvas)
        self.root.after(FPS_MS, self._tick)