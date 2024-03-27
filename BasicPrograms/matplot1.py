import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]
plt.plot(x, y, marker='o', linestyle='--', color='blue', label='Line Plot')

# Add labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Simple Line Plot')

# Show legend
plt.legend()
plt.show()