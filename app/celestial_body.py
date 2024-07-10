from app.constants import *

from typing import List
from dataclasses import dataclass

import numpy as np


class CelestialBody(CelestialBodyBase):
    def __init__(self, canvas, body_base: CelestialBodyBase) -> None:
        super().__init__(body_base.name, body_base.r_i, body_base.v_i, body_base.mass, body_base.color)
        self.canvas = canvas
        self._random_init_2d()

        self.body = self.canvas.create_oval(0, 0, 0, 0, fill=self.color)
        self.label = canvas.create_text(0, -15, text=self.name, fill="white")

    def delete(self):
        self.canvas.delete(self.body)
        self.canvas.delete(self.label)

    def _random_init_2d(self):
        angle = np.random.uniform(0, 2 * np.pi)

        self.x_pos = self.r_i * np.cos(angle)
        self.y_pos = self.r_i * np.sin(angle)
        
        self.v_x = - self.v_i * np.sin(angle)
        self.v_y = self.v_i * np.cos(angle)

        self.ax = .0
        self.ay = .0
    
    def adapt_to_window(self, width, height, max_radius):
        self.width, self.height = width, height 
        self.max_radius = max_radius
        self.x, self.y = self._adapt_pos_to_window(self.x_pos, self.y_pos, translate=True)
        size = 10 if self.name == "Sun" else 5
        self.body = self.canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill=self.color)

    def _adapt_pos_to_window(self, x, y, translate=False):
        tr = 1 if translate else 0
        dil = 5/4
        x = (x / self.max_radius + dil * tr) * self.height / ((2 * dil)**tr)
        y = (y / self.max_radius + dil * tr) * self.width / ((2 * dil)**tr)
        return x, y

    def move(self, bodies): 
        self.dynamic(bodies)

        self.v_x += self.ax * dt 
        self.v_y += self.ay * dt

        dx_pos, dy_pos = self.v_x * dt, self.v_y * dt
        dx, dy = self._adapt_pos_to_window(dx_pos, dy_pos)

        self.canvas.move(self.body, dx, dy)
        self.canvas.move(self.label, dx, dy)

        self.x += dx
        self.y += dy

        self.x_pos += dx_pos
        self.y_pos += dy_pos


    def dynamic(self, bodies):
        self.ax, self.ay = .0, .0

        for body in bodies: 
            if not body.name == self.name:
                dist_x = float(self.x_pos - body.x_pos) 
                dist_y = float(self.y_pos - body.y_pos)
                d_acc = - G * body.mass / (distance((dist_x, dist_y))**(3))
                self.ax = self.ax + d_acc * dist_x
                self.ay = self.ay + d_acc * dist_y

def distance(pos):
    x, y = pos
    return np.sqrt(x**2 + y**2)