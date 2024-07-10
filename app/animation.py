from app.celestial_body import CelestialBody
from app.constants import CelestialBodyBase, solar_planets

import tkinter as tk
from copy import deepcopy

class CelestialApp(tk.Tk):
    def __init__(self, init_mode: str = "solar_system", width: int = 600, height: int = 600, panel_width: int = 200):
        super().__init__()
        self.title("Celestial Movement Simulator")
        self.geometry(f"{width + panel_width}x{height}")

        self.width, self.height = width, height
        self.canvas = tk.Canvas(self, bg="black", width=width, height=height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.control_frame = tk.Frame(self, width=panel_width)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.create_controls()

        self.bodies = [] if not init_mode=="solar_system" else [CelestialBody(self.canvas, planet) for planet in solar_planets]
        self.scale_objects_to_window()

    def create_controls(self):
        self.create_label_entry("Name", "name")

        self.create_label_entry("Initial Radius", "r_i")
        self.create_label_entry("Initial Velocity", "v_i")
        self.create_label_entry("Mass", "mass")
        
        add_object_button = tk.Button(self.control_frame, text="Add object", command=self.add_object)
        add_object_button.pack(pady=10)
        
        time_speed_label = tk.Label(self.control_frame, text="Time Speed")
        time_speed_label.pack(pady=10)
        
        self.time_speed_var = tk.DoubleVar(value=1.0)
        time_speed_entry = tk.Entry(self.control_frame, textvariable=self.time_speed_var)
        time_speed_entry.pack(pady=10)
        
        start_button = tk.Button(self.control_frame, text="Start Simulation", command=self.start_simulation)
        start_button.pack(pady=10)

        pause_button = tk.Button(self.control_frame, text="Pause Simulation", command=self.pause_simulation)
        pause_button.pack(pady=10)

        restart_button = tk.Button(self.control_frame, text="Restart Simulation", command=self.restart_simulation)
        restart_button.pack(pady=10)

    def create_label_entry(self, label_text, var_name):
        label = tk.Label(self.control_frame, text=label_text)
        label.pack(pady=5)
        
        entry_var = tk.StringVar()
        setattr(self, f"{var_name}_var", entry_var)
        
        entry = tk.Entry(self.control_frame, textvariable=entry_var)
        entry.pack(pady=5)

    def add_object(self):
        try:
            name = float(self.name_var.get())
            r_i = float(self.r_i_var.get())
            v_i = float(self.v_i_var.get())
            mass = float(self.mass_var.get())
            body_base = CelestialBodyBase(name, r_i, v_i, mass, color="white")

            body = CelestialBody(self.canvas, body_base)
            self.bodies.append(body)

            self.scale_objects_to_window()
        except ValueError:
            print("Invalid input, please enter numerical values for positions, size, and velocity.")

    def start_simulation(self):
        self.simulation_running = True

        # self.bodies_copy = deepcopy(self.bodies)

        self.scale_objects_to_window()
        self.animate()
    
    def clear_canvas(self):
        for body in self.bodies:
            body.delete()

    def scale_objects_to_window(self):
        self.clear_canvas()
        max_r_i = max([body.r_i for body in self.bodies])
        for body in self.bodies:
            body.adapt_to_window(self.width, self.height, max_r_i)
        
    def pause_simulation(self):
        self.simulation_running = False

    def restart_simulation(self):
        self.simulation_running = False
        self.start_simulation()

    def animate(self):
        if self.simulation_running:
            for body in self.bodies:
                body.move(self.bodies)

            self.after(int(50 / self.time_speed_var.get()), self.animate)
