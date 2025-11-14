import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("./data.csv")
type_count = df["Type1"].value_counts(ascending=True)

plt.barh(type_count.index, type_count.values, color="#20c997", edgecolor="#222")

plt.title("No. of Pokemon")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()

plt.show()