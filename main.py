import random
import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Circle

class Walker:
    """Class representing a randomly walking object."""

    def __init__(self, position: tuple[int, int] = (0, 0)):
        self.position = list(position)
        # Possible movement directions in the form [x, y]
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def step(self) -> list[int]:
        """Moves the object one step in a random direction."""
        direction = random.choice(self.directions)
        # Update position based on the chosen direction
        self.position[0] += direction[0]
        self.position[1] += direction[1]
        return self.position

    def walk(self, n_steps: int) -> list[int]:
        """Performs a random walk for a specified number of steps."""
        for _ in range(n_steps):
            self.step()
        return self.position

def walker_generator(n_walkers: int):
    """Generates a specified number of walkers."""
    for _ in range(n_walkers):
        yield Walker()

# Simulation parameters
n_steps = 10_000  # Number of steps per walker
n_walkers = 1_000  # Number of walkers to simulate

# Run the simulation and record the final positions of all walkers
end_positions = [walker.walk(n_steps) for walker in walker_generator(n_walkers)]

# Extract x and y coordinates for plotting
x_coords = [pos[0] for pos in end_positions]
y_coords = [pos[1] for pos in end_positions]

# Plotting the final positions of the walkers
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, color='blue', marker='o', s=2, alpha=0.5)
# In a 2D random walk, the expected distance R from the starting point after N steps is approximately sqrt(N)
expected_radius = math.sqrt(n_steps)
circle = Circle(xy=(0, 0), radius=expected_radius, linewidth=2, edgecolor='red', facecolor='none')
plt.gca().add_patch(circle)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Final Positions of Random Walkers')
plt.grid(True)
plt.axis('equal')
plt.show()

# Calculate the percentage of walkers within the expected radius
inner_points_count = sum(
    1 for pos in end_positions if math.sqrt(pos[0]**2 + pos[1]**2) <= expected_radius
)
percentage_inside_circle = (inner_points_count / n_walkers) * 100
print(f'Percentage of walkers inside the red circle: {percentage_inside_circle:.2f}%')
