import matplotlib.pyplot as plt

# Simple line plot
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Line Plot')
plt.show()

# Bar chart
categories = ['A', 'B', 'C']
values = [5, 7, 8]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()

# Scatter plot
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()
