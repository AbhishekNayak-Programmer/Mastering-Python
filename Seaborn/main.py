import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# print(sns.__version__)
# print(sns.get_dataset_names())

penguins = sns.load_dataset('penguins')
print(penguins.head())
# print(penguins.sample(15))

print(penguins["species"].value_counts())
print(penguins["island"].value_counts())

sns.set_style("ticks") # default
# sns.set_style("dark")
# sns.set_style("whitegrid")
# sns.set_style("darkgrid")

# Adjust sizes
# sns.set_context("poster")
# sns.set_context("paper")
# sns.set_context("poster")
sns.set_context("notebook") # default

# sns.set_palette("Set1") # Darker
# sns.set_palette("Set2") # lighter
# sns.set_palette("Set3") # very light
# sns.set_palette("deep")
sns.set_palette("dark")

# sns.scatterplot(data = penguins, x="flipper_length_mm", y="body_mass_g", hue="island")

# sns.scatterplot(data = penguins, x="species", y="body_mass_g", hue="island", style="sex")

# sns.stripplot(data = penguins, x="species", y="body_mass_g", hue="island", jitter=True, dodge=True)

# sns.swarmplot(data = penguins, x="species", y="body_mass_g", hue="island")

# sns.histplot(data = penguins, x="body_mass_g", hue="sex", multiple="stack")

# sns.regplot(data = penguins, x="body_mass_g", y="flipper_length_mm")

# sns.lineplot(data = penguins, x="body_mass_g", y="flipper_length_mm")

# sns.lineplot(data = penguins, x="body_mass_g", y="flipper_length_mm", hue="island", style="sex")

# sns.jointplot(data = penguins, x = 'body_mass_g', y = "flipper_length_mm", hue="island") 

# sns.jointplot(data = penguins, x = 'body_mass_g', y = "flipper_length_mm", hue="sex") 

# sns.jointplot(data = penguins, x = 'body_mass_g', y = "flipper_length_mm", hue="sex", kind="kde") 

# sns.barplot(data=penguins, x="species", y="body_mass_g", hue="sex", palette=["pink", 'lightgreen'])

# sns.countplot(data=penguins, x='species')

# sns.countplot(data=penguins, x='species', hue="island", palette="Set1")

# sns.boxplot(data = penguins, x = "species", y='body_mass_g', hue="island")
# sns.boxplot(data = penguins, x = "species", y='body_mass_g', hue="sex")

# sns.violinplot(data = penguins, x = "species", y='body_mass_g', hue="sex")

# sns.violinplot(data = penguins, x = "species", y='body_mass_g', hue="sex", split=True)
# sns.swarmplot(data = penguins, x="species", y="body_mass_g", size=3, palette="Set2")


# sns.kdeplot(data = penguins, x = 'body_mass_g', hue="species", fill=True) 

sns.pairplot(data = penguins, hue="sex", palette="Set1")



sns.despine() # Used for removing the lines from top and right side


plt.show()