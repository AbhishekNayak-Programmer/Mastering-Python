import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0,1,2,3,4,5,6,7,8,9,11,12])
y1 = np.array([55,58,62,68,77,70,79,80,88,89,92,99])

x2 = np.array([0,1,2,3,4,5,6,7,8,9,9])
y2 = np.array([52,54,59,62,72,78,75,82,88,91,94])

plt.scatter(x1,y1, color="#5f3dc4", alpha=0.8, s=200, label="Class A") # alpha is like opacity and s is size of circle
plt.scatter(x2,y2, color="#1098ad", alpha=0.8, s=200, label="Class B")

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()

plt.show()