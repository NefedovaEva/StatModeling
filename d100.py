import numpy as np
import matplotlib.pyplot as plt

n_points = 100
dimension = 100

# Generate random points on the surface of a sphere
random_points = np.random.normal(0, 1, size=(n_points, dimension))
norm_point = np.zeros(n_points)
points = np.zeros((n_points, dimension))
for i in range(n_points):
    norm_point[i] = np.linalg.norm(random_points[i])
for i in range(n_points):
    for j in range(dimension):
      points[i, j] = random_points[i, j]/norm_point[i]

# Calculate pairwise distances between points
distances = np.zeros((n_points, n_points))
for i in range(n_points):
    for j in range(n_points):
     distances[i, j] = np.linalg.norm(np.subtract(points[i], points[j]))
distance = []
for i in range(n_points):
    for j in range(i + 1, n_points):
      distance.append(distances[i, j])
print(points)

# Plotting the histogram
plt.hist(distance, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Distance')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()