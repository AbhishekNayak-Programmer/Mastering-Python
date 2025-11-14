import pandas as pd

# reading a csv file
df = pd.read_csv("data.csv", index_col="Name")
print(df)
# print(df.to_string()) # print all the data

# reading a json file
df_json = pd.read_json("data.json")
print(df_json)

# Selection by column
# print(df['Name'])
# print(df['Name'].to_string())
print(df["Height"])

# Getting multiple columns at once
print(df[["Height", "Weight"]]) 

# Selection based on names as we set index_col is Name
print(df.loc["Pikachu"])
print(df.loc["Charizard"])
print(df.loc["Mewtwo", ["Height", "Weight", "Legendary"]])

# Selection all between two names
print(df.loc["Charizard":"Blastoise",  ["Height", "Weight"]])

# Get first 10 rows
print(df.iloc[0:11:2])
print(df.iloc[0:11:2, 0:3]) # Selecting number of columns

# pokemon = input("Enter a Pokemon name: ")
# try : 
#     print(df.loc[pokemon])
# except :
#     print(f"{pokemon} does not found in csv file")
# else :
#     print("You can run to try more pokemon")

# Filtering using pandas
tall_pokemon = df[df["Height"] >= 2]
print(tall_pokemon)

heavy_pokemon = df[df["Weight"] >= 100]
print(heavy_pokemon)

legendary_pokemon = df[df["Legendary"] == 1]
print(legendary_pokemon)

water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)

fire_flying_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
print(fire_flying_pokemon)

# Aggregate Functions whole DataFrame
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

# Aggregate function for single column
print(df["Height"].mean())
print(df["Height"].sum())
print(df["Height"].max())
print(df["Height"].min())
print(df["Height"].count())

# Aggregate function Groupby 
group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
print(group["Height"].min())
print(group["Height"].count())

# Data Cleaning 
# 1. Drop irrelevant columns
df = df.drop(columns=["No"]) 
# df = df.drop(columns=["No", "Legendary"]) # you can also pass multiple column names as well
# print(df)

# 2. Handle missing data in the row where that column data is not available
df = df.dropna(subset=["Type2"])
print(df.to_string())

# 3. Reassign the not available values
df = df.fillna({"Type2" : "None"})
print(df.to_string())

# 4. Fix inconsistent values
df["Type1"] = df["Type1"].replace({"Grass" : "GRASS", "Fire" : "FIRE", "Water" : "WATER"})
print(df.to_string())

# 5. Standardize text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 6. Change the type of the data stored inside this column
df["Legendary"] = df["Legendary"].astype(bool)
print(df.to_string())


# 7. Drop Duplicates from Data frame
df = df.drop_duplicates()
print(df.to_string())