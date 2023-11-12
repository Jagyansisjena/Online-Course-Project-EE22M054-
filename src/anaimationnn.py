import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function f(x, t)
def f(x, t):
    return 0.5 * (x + t)**2 + 2 * np.sin(10 * (x - t))

# Create a figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)

# Initialize an empty plot
line, = ax.plot(x, f(x, 0))

# Update function for animation
def update(t):
    line.set_ydata(f(x, t))
    ax.set_title(f'Time t = {t:.1f}')
    return line,

# Create an animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), blit=True)

# Display the animation
plt.show()
