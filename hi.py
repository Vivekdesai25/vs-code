import matplotlib
matplotlib.use('Agg') # Use non-GUI backend

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [5, 10, 15, 20, 30, 35, 45]

plt.figure(figsize=(8, 10))
plt.plot(x, y, marker='o')
plt.xlabel("vivek")
plt.ylabel("desai")
plt.title("trial")
plt.grid(True)

# Save the plot as an image file
plt.savefig("my_plot.png")
plt.show()
