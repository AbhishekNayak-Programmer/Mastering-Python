import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(2,2)
x = np.array([1, 2, 3, 4, 5])
y = x * 2

axes[0,0].bar(x, y, color="#20c997")
axes[0,0].set_title("x*2")

axes[0,1].plot(x, y**4, color="#f59f00")
axes[0,1].set_title("y**4")

axes[1,0].plot(x, y**2, color="#e03131")
axes[1,0].set_title("y**2")

axes[1,1].bar(x, y**3, color="#7048e8")
axes[1,1].set_title("y**3")

# Adjust spacing
plt.subplots_adjust(
    left=0.1,   # space from the left
    right=0.9,  # space from the right
    top=0.9,    # space from the top
    bottom=0.1, # space from the bottom
    wspace=0.4, # horizontal gap between subplots
    hspace=0.4  # vertical gap between subplots
)

plt.show()