import matplotlib.pyplot as plt
import numpy as np

scores = np.random.normal(loc=80, scale=10, size=1000)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=20, color="#38d9a9", edgecolor="#000")

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")

plt.show()