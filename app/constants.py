## Gravity constants 
eps = 1e-15
# Sun mass
Ms = 1.9e30
# Universal gravity constant (kg^-1,m^3,s^-2)
G = 6.67e-11 

# Mass of Earth (kg)
mT = 5.9e24 

# Astronomic unit
au = 149597870700.

# Time diff (s)
dt = 1e5

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

solar_planets = [
    CelestialBodyBase("Sun", eps, 0, Ms, "yellow"),
    CelestialBodyBase("Mercury", 0.39 * au, 47367, 3.3011e2, "forest green"),
    # CelestialBodyBase("Venus", 0.723 * au, 35025, 0.815 * mT, "lawn green"),
    # CelestialBodyBase("Earth", 1.524 * au, 47367, 1. * mT, "blue"),
    # TODO: Check Mars initial cond
    # CelestialBodyBase("Mars", 0.39 * au, 47367, 0.107 * mT, "red"),
    # CelestialBodyBase("Jupiter", 5.202603 * au, 13058, 327.83 * mT, "orange"),
    # CelestialBodyBase("Uranus", 9.554909 * au, 9640, 14.54 * mT),
    CelestialBodyBase("Neptune", 30.11039 * au, 5432.48, .0021 * mT, color="purple"),
]