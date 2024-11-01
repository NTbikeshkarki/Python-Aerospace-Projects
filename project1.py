import numpy as np

v0 = 50  # initial velocity in m/s
theta = 45  # launch angle in degrees
g = 9.8  # gravitational constant in m/s^2

theta = np.radians(theta)  # Convert angle to radians
T = 2 * v0 * np.sin(theta) / g  # total time of flight
t = np.linspace(0, T, num=500)  # time intervals

x = v0 * np.cos(theta) * t  # horizontal distance
y = v0 * np.sin(theta) * t - 0.5 * g * t**2  # vertical distance
import matplotlib.pyplot as plt

plt.plot(x, y)
plt.title("Projectile Motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.ylim(bottom=0)  # Set bottom limit to 0 to keep ground level visible
plt.grid()
plt.show()