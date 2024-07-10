from app.constants import *

from typing import List
from dataclasses import dataclass

import numpy as np


class CelestialBody(CelestialBodyBase):
    def __init__(self, canvas, body_base: CelestialBodyBase) -> None:
        super().__init__(body_base.name, body_base.r_i, body_base.v_i, body_base.mass, body_base.color)
        self.canvas = canvas
        self._random_init_2d()        

    def _random_init_2d(self):
        angle = 2*np.pi # np.random.uniform(0, 2 * np.pi)

        self.x_pos = self.r_i * np.cos(angle)
        self.y_pos = self.r_i * np.sin(angle)
        
        # d_angle_i = np.sqrt(self.v_i ** 2 / self.r_i **2)
        self.v_x = - self.v_i * np.sin(angle)
        self.v_y = self.v_i * np.cos(angle)

        self.ax = .0
        self.ay = .0
    
    def adapt_to_window(self, width, height, max_radius):
        self.width, self.height = width, height 
        self.max_radius = max_radius
        self.x, self.y = self._adapt_pos_to_window(self.x_pos, self.y_pos, translate=True)
        size = 10
        self.body = self.canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill=self.color)

    def _adapt_pos_to_window(self, x, y, translate=False):
        tr = 1 if translate else 0
        x = (x / self.max_radius + tr) * self.height / 2
        y = (y / self.max_radius + tr) * self.width / 2
        return x, y

    def move(self, bodies): 
        self.dynamic(bodies)

        self.v_x += self.ax * dt 
        self.v_y += self.ay * dt

        dx_pos, dy_pos = self.v_x * dt, self.v_y * dt
        dx, dy = self._adapt_pos_to_window(dx_pos, dy_pos)

        self.canvas.move(self.body, dx, dy)
        print('dx, dy:', dx, dy)

        self.x += dx
        self.y += dy

        self.x_pos += dx_pos
        self.y_pos += dy_pos


    def dynamic(self, bodies):
        self.ax, self.ay = .0, .0

        for body in bodies: 
            # if not body.name == self.name:
            #     dist_x = float(body.x_pos-self.x_pos) 
            #     dist_y = float(body.y_pos-self.y_pos)
            #     # print(((dist_x**2 + dist_y**2)**(3/2)) - np.sqrt((dist_x**2 + dist_y**2)**(3))) if not ((dist_x**2 + dist_y**2)**(3/2)) == np.sqrt((dist_x**2 + dist_y**2)**(3)) else None
            #     d_acc = - G * body.mass / np.sqrt((dist_x**2 + dist_y**2)**(3))
            #     self.ax = self.ax + d_acc * dist_x
            #     self.ay = self.ay + d_acc * dist_y
            
            if body.name == "Sun":
                dist_x = float(body.x_pos - self.x_pos) 
                dist_y = float(body.y_pos - self.y_pos)
                print('dist to sun', distance(self._adapt_pos_to_window(dist_x, dist_y)))
                print('on x and y', self._adapt_pos_to_window(dist_x, dist_y))
                # print(((dist_x**2 + dist_y**2)**(3/2)) - np.sqrt((dist_x**2 + dist_y**2)**(3))) if not ((dist_x**2 + dist_y**2)**(3/2)) == np.sqrt((dist_x**2 + dist_y**2)**(3)) else None
                d_acc = - G * body.mass / np.sqrt((dist_x**2 + dist_y**2)**(3))
                self.ax = self.ax + d_acc * dist_x
                self.ay = self.ay + d_acc * dist_y
        print('computed acc', self.ax, self.ay)
        # return self.ax, self.ay

def distance(pos):
    x, y = pos
    return np.sqrt(x**2 + y**2)