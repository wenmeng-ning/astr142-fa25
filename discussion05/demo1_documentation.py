"""
Module: simpleOrbits

This module provides classes and functions 
to compute:

- Escape velocity
- Orbital period

The formulas are based on classical Newtonian physics.

Constants:
    G (float): Gravitational constant in m^3 kg^-1 s^-2.

Example:
    earth = Body(name='Earth', mass=5.972e24, radius=6.371e6)
    escape_velocity = earth.get_escape_velocity()
    orbital_period = earth.get_orbital_period(orbital_radius=4.22e7)  # Geostationary orbit

This is a demo on documentation for modules, class and functions.
This follows the Google-style docstring format, 
but you can choose your preferred format as long as it
contains all the essential information needed.  
"""

import math

G = 6.67430e-11 # Gravitational constant (m^3 kg^-1 s^-2)


class Body:
    """
    This class represents a celestial body with mass 
    and radius and provides methods to calculate escape velocity 
    and orbital period around the body.

    Attributes:
        name (str): Name of the body.
        mass (float): Mass of the body in kilograms.
        radius (float): Radius of the body in meters.

    Methods:
        get_escape_velocity():
            Calculates the escape velocity from the surface of the body.

        get_orbital_period(orbital_radius):
            Calculates the orbital period at a given orbital radius.
    """

    def __init__(self, name, mass, radius):
        """
        Initializes an instance.

        Args:
            name (str): Name of the celestial body.
            mass (float): Mass in kilograms.
            radius (float): Radius in meters.
        """
        self.name = name
        self.mass = mass
        self.radius = radius

    def get_escape_velocity(self):
        """
        Calculates the escape velocity from the surface of 
        the celestial body.

        Uses the formula: v = sqrt(2 * G * M / R)

        Returns:
            float: Escape velocity in meters per second.

        Example:
            earth = CelestialBody('Earth', 5.972e24, 6.371e6)
            earth.get_escape_velocity()
        """
        velocity = math.sqrt(2 * G * self.mass / self.radius)
        return velocity

    def get_orbital_period(self, orbital_radius):
        """
        Calculates the orbital period for a satellite at a 
        given orbital radius.

        Uses the formula: T = 2π * sqrt(r^3 / (G * M))

        Args:
            orbital_radius (float): Distance from the center of the body to the satellite in meters.

        Returns:
            float: Orbital period in seconds.

        Raises:
            ValueError: If orbital_radius is less than the body's radius.

        Example:
            earth = CelestialBody('Earth', 5.972e24, 6.371e6)
            earth.get_orbital_period(4.22e7)
        """
        if orbital_radius <= self.radius:
            raise ValueError("Orbital radius must be greater than the body's radius.")
        period = 2 * math.pi * math.sqrt(orbital_radius ** 3 / (G * self.mass))
        return period
