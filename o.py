import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Create some data
x = [1, 2, 3]
y = [2, 4, 6]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(x, y, 'o')

# Add circles around the points
for xi, yi in zip(x, y):
    ax.add_patch(Circle((xi, yi), radius=0.5, fill=False))

# Show the plot
plt.show()