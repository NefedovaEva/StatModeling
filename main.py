import numpy as np
import pandas as pd
import scipy as scipy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set the number of points
n_points = 30

# Generate random points inside the cube [-0.5, 0.5]^100
points = np.random.uniform(-1/2, 1/2, size=(n_points, 100))

# Calculate pairwise distances between points
distances = np.linalg.norm(points[:, np.newaxis] - points, axis=2)

# Calculate pairwise angles between vectors from the origin to the points
angles = np.arccos(np.clip(np.dot(points, points.T) / (np.linalg.norm(points) * np.linalg.norm(points)), -1.0, 1.0))

plt.subplot(1, 2, 1)
plt.scatter(distances, angles)
plt.xlabel("Distance")
plt.ylabel("Angle")

plt.subplot(1, 2, 2)
plt.hist(distances)
plt.xlabel("Distance")
plt.ylabel("Frequency")

plt.show()

# Display the calculated distances and angles
print('Pairwise Distances between Points:')
print(distances)
print('\nPairwise Angles between Vectors from the Origin to the Points:')
print(angles)

print(points)
