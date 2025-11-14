import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("./data.csv")
height = df["Height"].value_counts()

plt.scatter(height.index, height.values, color="#20c997", edgecolor="#222")

plt.title("Height Chart")
plt.xlabel("Height in m")
plt.ylabel("No. of Pokemon")
plt.tight_layout()
plt.show()