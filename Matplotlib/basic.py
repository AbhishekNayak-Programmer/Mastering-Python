import matplotlib.pyplot as plt
import numpy as np
# print(matplotlib.__version__)

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

plt.plot(x,y, 
         marker="o", 
         markersize=20, 
         markerfacecolor="black", 
         markeredgecolor="black", 
         linestyle="dashed",
         linewidth=2)
plt.show()

time = np.array(["Day1", "Day2", "Day3", "Day4", "Day5"])
robot_temprature = np.array([41, 46, 56, 78, 23])

plt.plot(time, robot_temprature,
        marker="v",
        markersize=10, 
        markerfacecolor="#63e6be", 
        markeredgecolor="#63e6be", 
        linestyle="solid",
        # linestyle="dotted",
        # linestyle="dashdot",
        # linestyle="None",
        linewidth=2, 
        color="#7048e8")
        
plt.show()