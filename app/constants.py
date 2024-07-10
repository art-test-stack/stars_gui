## Gravity constants 
eps = 1e-15
# Sun mass
mass_sun = 1.9e30
# Universal gravity constant (kg^-1,m^3,s^-2)
G = 6.67e-11 

# Mass of Earth (kg)
mass_earth = 5.9e24 

# Astronomic unit
au = 149597870700.

# Time diff (s)
dt = 5e7

# Solar planets
from dataclasses import dataclass
from typing import List

@dataclass
class CelestialBodyBase:
    name: str 
    r_i : float
    v_i : List[float]
    mass: float
    color: str

# https://nssdc.gsfc.nasa.gov/planetary/factsheet/

solar_planets = [
    CelestialBodyBase("Sun", eps, 0, mass_sun, "yellow"),
    CelestialBodyBase("Mercury", 0.39 * au, 47367, 3.3011e2, "forest green"),
    CelestialBodyBase("Venus", 0.723 * au, 35025, 0.815 * mass_earth, "lawn green"),
    CelestialBodyBase("Earth", 1. * au, 29783, 1. * mass_earth, "blue"),
    CelestialBodyBase("Mars", 1.524 * au, 24080.2, 0.107 * mass_earth, "red"),
    CelestialBodyBase("Jupiter", 5.202603 * au, 13058, 327.83 * mass_earth, "orange"),
    CelestialBodyBase("Saturn", 9.554909 * au, 9640, 95.16 * mass_earth, "DarkOrange2"),
    CelestialBodyBase("Uranus", 19.21845 * au, 6796.7, 14.54 * mass_earth, "peach puff"),
    CelestialBodyBase("Neptune", 30.11039 * au, 5432.48, .0021 * mass_earth, color="purple"),
]

import numpy as np

random_objects = [
    CelestialBodyBase(
        name=id, 
        r_i=np.random.uniform(.1 * au, 10. * au), 
        v_i=np.random.uniform(500, 1_000),
        mass=np.random.uniform(1e22, 1e24),
        color="yellow"
        )
    for id in range(999)]
