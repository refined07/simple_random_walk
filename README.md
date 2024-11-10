# 2D Random Walk Simulation

This code simulates and visualizes a **2D Random Walk Process** and is designed to model the behavior of multiple "walker" objects over a large number of steps. Each walker begins at the origin point \((0, 0)\) and randomly moves in one of four possible directions (up, down, left, or right) on each step, accumulating to an overall movement path.

## Code Structure and Key Elements

### Walker Class
This class encapsulates the behavior of a single walker, allowing each to "step" in a random direction and "walk" a specified number of steps. Using an object-oriented approach here allows for easy scaling to multiple walkers and keeps the code organized.

### Walker Generator
The generator function produces the specified number of walker objects, facilitating the simulation of multiple, independent random walks.

### Simulation of the Random Walk
The `walk()` method of each walker simulates its movement over a fixed number of steps, returning the final position of each walker after all steps.

### Visualization
The code uses `matplotlib` to plot the final positions of all walkers on a 2D plane. Additionally, a red circle, centered at the origin with a radius proportional to $\sqrt{N}$ (where \(N\) is the number of steps), provides a visual reference for the expected distance from the origin. This is based on the theoretical result that the average distance from the starting point in a 2D random walk grows with $\sqrt{N}$.

### Analysis of Walkers' Distribution
After plotting, the code calculates the percentage of walkers who end up within the red circle (the expected radius), providing insights into the spatial distribution of the walkers after a large number of steps.

### Additional Experiments
Feel free to experiment with additional directions, number of steps, number of walkers etc.
