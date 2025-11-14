import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026, 2027])
y1 = np.array([78, 25, 30, 68, 100])
y2 = np.array([20, 47, 3, 89, 110])
y3 = np.array([40, 70, 45, 99, 120])

# Setting the title for chart
font_style = dict(fontsize=20, family="DejaVu Sans", fontweight="bold")

plt.title("Abhishek Chart", **font_style, color="#fd7e14")
plt.xlabel("Year", **font_style, color="#364fc7")
plt.ylabel("Progress",**font_style, color="#862e9c")

# Store all common keys inside a dictionary
line_style = dict(markersize=10,
        markerfacecolor='black',
        markeredgecolor="black",
        linestyle="dashed",linewidth=2)

# Creating multiple lines using x and diffrent y axis 
plt.plot(x, y1, marker="s",**line_style, color="#f06595")
plt.plot(x, y2, marker="v",**line_style, color="#5c940d")
plt.plot(x, y3, marker="o",**line_style, color="#4263eb")

# Giving color to each and every points in the x and y axis 
plt.tick_params(axis="x", colors="#364fc7")
plt.tick_params(axis="y", colors="#862e9c")

plt.xticks(x) # Only show the passed x axis value in the array in x axis

plt.show()