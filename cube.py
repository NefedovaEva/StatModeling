import numpy as np
import matplotlib.pyplot as plt

n_points = 30
dimension = 100
a = 0.5

# Generate random points inside the cube [-0.5, 0.5]^100
points = np.random.uniform(-a, a, size=(n_points, dimension))

# Calculate pairwise distances between points
distances = np.zeros((n_points, n_points))
for i in range(n_points):
    for j in range(n_points):
     distances[i, j] = np.linalg.norm(np.subtract(points[i], points[j]))

# Calculate pairwise angles between vectors from the origin to the points
angles = np.zeros((n_points, n_points))
for i in range(n_points):
    for j in range(n_points):
        if j != i:
         angles[i, j] = np.arccos(np.dot(points[i], points[j]) / (np.linalg.norm(points[i]) * np.linalg.norm(points[j])))

# Plot the points
distance=[]
n_pairs = 0
for i in range(n_points):
    for j in range(i + 1, n_points):
      distance.append(distances[i, j])
      n_pairs += 1
pairs = np.arange(1, n_pairs+1)
plt.scatter(pairs, distance)
plt.grid(True)
plt.xlabel('Pair of points')
plt.ylabel('Distance')
plt.show()

angle=[]
for i in range(n_points):
    for j in range(i + 1, n_points):
      angle.append(angles[i, j])
pairs = np.arange(1, n_pairs+1)
plt.scatter(pairs, angle)
plt.grid(True)
plt.xlabel('Pair of points')
plt.ylabel('Angle')
plt.show()

