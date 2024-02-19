import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 20, 1000)

# Calculate y values for the first wave
y1 = np.sin(1.732 * x)

# Plot the graph for the first wave
plt.figure(figsize=(10, 6))  # Adjust figure size
plt.plot(x, y1)

# Calculate y values for the second wave
y2 = np.sin(1.9892 * (19.952-x))

# Plot the graph for the second wave
plt.plot(x, y2)

plt.scatter([19.952], [np.sin(1.732 * 19.952)], color='red', zorder=5)
plt.scatter([0], [np.sin(1.732 * 0)], color='blue', zorder=5)

plt.xlabel("x (cm)")
plt.ylabel("y (cm)")
plt.grid(True)


# Annotation and arrow for λ1
arrow_start = (0, -1)
arrow_end = (3.625, -1)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(1.8, -1.1, "$λ_1$", verticalalignment='bottom', horizontalalignment='right', color='purple')  # Adjust text position

# Annotation and arrow for λ2
arrow_start = (19.952, -1)
arrow_end = (19.952-3.157, -1)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(18.4,-1.1, "$λ_2$", verticalalignment='bottom', horizontalalignment='left', color='purple')  # Adjust text position



# Annotation and arrow for V
arrow_start = (0, 1.05)
arrow_end = (7, 1.05)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<-'))
plt.text(3, 0.95, "$V$", verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.text(-0.02, -0.095, "$A$", verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.text(19.9, -0.095, "$B$", verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.show()
