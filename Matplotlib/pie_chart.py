import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([300, 250, 275, 225])
colors = ["#22b8cf", "#82c91e", "#9775fa", "#adb5bd"]

plt.pie(values, labels=categories,
        autopct="%1.1f%%", 
        colors=colors, 
        explode=[0,0,0,0.2], 
        shadow=True,
        startangle=90)
plt.title("Web Coder Abhishek College")
# plt.xlabel("Food")
# plt.ylabel("Quantity")

plt.show()