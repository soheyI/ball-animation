
import random

class Ball:
    def __init__(self, x, y, r, color, speed=None, dir_x=None, dir_y=None):
        self.x, self.y = x, y
        self.r = r
        self.color = color

        # base speed
        self.speed = speed if speed is not None else 1.5

        # diagonal direction
        self.dir_x = dir_x if dir_x in (-1, 1) else random.choice((-1, 1))
        self.dir_y = dir_y if dir_y in (-1, 1) else random.choice((-1, 1))

        self.item_id = None  # canvas oval 

    def draw(self, canvas):
        if self.item_id is None:
            self.item_id = canvas.create_oval(
                self.x - self.r, self.y - self.r,
                self.x + self.r, self.y + self.r,
                fill=self.color, outline=""
            )
        else:
            canvas.coords(
                self.item_id,
                self.x - self.r, self.y - self.r,
                self.x + self.r, self.y + self.r
            )

    def update(self, dt_ms, bounds_w, bounds_h):
        dt = dt_ms / 1000.0
        step = self.speed * dt * 60.0  # pixels 60fps frame

        self.x += self.dir_x * step
        self.y += self.dir_y * step

        # bounce left right
        if self.x - self.r <= 0 and self.dir_x < 0:
            self.dir_x = 1
            self.x = self.r
        elif self.x + self.r >= bounds_w and self.dir_x > 0:
            self.dir_x = -1
            self.x = bounds_w - self.r

        # bounce top buttom
        if self.y - self.r <= 0 and self.dir_y < 0:
            self.dir_y = 1
            self.y = self.r
        elif self.y + self.r >= bounds_h and self.dir_y > 0:
            self.dir_y = -1
            self.y = bounds_h - self.r