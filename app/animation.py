from app.celestial_body import CelestialBody
from app.constants import CelestialBodyBase, solar_planets

import tkinter as tk
from copy import deepcopy

class CelestialApp(tk.Tk):
    def __init__(self, init_mode: str = "solar_system", width: int = 600, height: int = 600, panel_width: int = 200):
        super().__init__()
        self.title("Celestial Movement Simulator")
        self.geometry(f"{width + panel_width}x{height}")

        # Create the main canvas
        self.width, self.height = width, height
        self.canvas = tk.Canvas(self, bg="black", width=width, height=height)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Right frame for controls
        self.control_frame = tk.Frame(self, width=panel_width)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add control options
        self.create_controls()

        # List to store celestial bodies
        self.bodies = [] if not init_mode=="solar_system" else [CelestialBody(self.canvas, planet) for planet in solar_planets]

    def create_controls(self):
        self.create_label_entry("Name", "name")

        self.create_label_entry("Initial Radius", "r_i")
        self.create_label_entry("Initial Velocity", "v_i")
        self.create_label_entry("Mass", "mass")
        
        # Button to add a new planet
        add_planet_button = tk.Button(self.control_frame, text="Add Planet", command=self.add_planet)
        add_planet_button.pack(pady=10)
        
        # Label and entry for time speed
        time_speed_label = tk.Label(self.control_frame, text="Time Speed")
        time_speed_label.pack(pady=10)
        
        self.time_speed_var = tk.DoubleVar(value=1.0)
        time_speed_entry = tk.Entry(self.control_frame, textvariable=self.time_speed_var)
        time_speed_entry.pack(pady=10)
        
        # Button to start simulation
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

    def add_planet(self):
        try:
            # Get parameters from entries
            name = float(self.name_var.get())
            r_i = float(self.r_i_var.get())
            v_i = float(self.v_i_var.get())
            mass = float(self.mass_var.get())
            body_base = CelestialBodyBase(name, r_i, v_i, mass, color="white")

            body = CelestialBody(self.canvas, body_base)
            self.bodies.append(body)
        except ValueError:
            # Handle invalid input
            print("Invalid input, please enter numerical values for positions, size, and velocity.")

    def start_simulation(self):
        self.simulation_running = True

        # self.bodies_copy = deepcopy(self.bodies)

        max_r_i = max([body.r_i for body in self.bodies])
        for body in self.bodies:
            body.adapt_to_window(self.width, self.height, max_r_i)
        
        self.animate()
    
    def pause_simulation(self):
        self.simulation_running = False

    def restart_simulation(self):
        self.simulation_running = False
        # self.bodies = self.bodies_copy
        self.start_simulation()

    def animate(self):
        if self.simulation_running:
            for body in self.bodies:
                print("\n\n")
                print("Name:", body.name)
                print("x, y:", body.x, body.y)
                print("pos x, y:", body.x_pos, body.y_pos)
                print("vx, vy:", body.v_x, body.v_y)
                if not body.name=="Sun":
                    body.move(self.bodies)
                
                print("ax, ay:", body.ax, body.ay)


            self.after(int(50 / self.time_speed_var.get()), self.animate)
