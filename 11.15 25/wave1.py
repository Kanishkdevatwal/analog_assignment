import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 20, 1000)

# Calculate y values
y = np.sin(1.732 * x)

# Plot the graph
plt.plot(x, y)
plt.title("Graph of SONAR wave")
plt.xlabel("x(cm)")
plt.ylabel("y(cm)")
plt.grid(True)

arrow_start = (0, -1)
arrow_end = (3.625, -1)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(1.8, -1.1,"$λ$", verticalalignment='bottom', horizontalalignment='right', color='purple')

arrow_start = (0, 0)
arrow_end = (0, 1)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<->'))
plt.text(0, 0.5,"$A$", verticalalignment='bottom', horizontalalignment='right', color='purple')

arrow_start = (0, 1.05)
arrow_end = (7, 1.05)
plt.annotate('', xy=arrow_start, xytext=arrow_end,
             arrowprops=dict(facecolor='purple', arrowstyle='<-'))
plt.text(3, 0.95,"$V$", verticalalignment='bottom', horizontalalignment='right', color='purple')

plt.show()