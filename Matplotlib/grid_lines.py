import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5, 10, 15, 20, 25])

# When you need grid lines at both x and y axis
plt.grid()
# plt.grid(axis='x', linewidth=2, color="#888", linestyle='dashed')
# plt.grid(axis='y', linewidth=2, color="#888", linestyle='dotted')

plt.plot(x,y)

plt.show()