import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4,5,2,4,3,1])

plt.bar(categories,values, color="#845ef7")
# plt.barh(categories,values, color="#0b7285") # For creating a horizontal bar chart
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()