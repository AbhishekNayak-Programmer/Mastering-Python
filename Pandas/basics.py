import pandas as pd

print(pd.__version__)

# Series in Pandas
data1 = [101.1, 102.2, 104.3]
data2 = [101, 102, 104]
data3 = ["Abhishek", "Nayak"]
data4 = [True, False, True, True, True]

series1 = pd.Series(data1)
series2 = pd.Series(data2)
series3 = pd.Series(data3)
series4 = pd.Series(data4)
print(series1, series2, series3, series4)

series = pd.Series(data2, index=["a", "b", "c"])
print(series)

print(series.loc["a"])
print(series.loc["b"])
series.loc["c"] = 200
print(series.loc["c"])

print(series.iloc[0])
print(series.iloc[1])
print(series.iloc[2])

print(series[series < 200])

calories = {"Day1" : 1750, "Day2" : 2100, "Day3":1700}
series = pd.Series(calories)
print(series)
print(series.loc["Day1"])
print(series.loc["Day2"])
print(series.loc["Day3"])

series.loc["Day3"] += 500
print(series.loc["Day3"])

print(series[series >= 2000])
print(series[series < 2000])

# Dataframes in Pandas
data = {
    "Name" : ["Abhishek", "Adarsh", "Swadhin"],
    "Age" : [24, 17, 18]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index = ["Emp1", "Emp2", "Emp3"])
print(df)

print(df.loc["Emp1"])
print(df.loc["Emp3"])
print(df.iloc[0])
print(df.iloc[1])

# Add a new column in dataframe
df["Job"] = ["Software Engineer", "Student", "Student"]
print(df)

# Add a new row in dataframe
new_row = pd.DataFrame([
    {
        "Name" : "Williams",
        "Age" : 28,
        "Job" : "Engineer"
    },
      {
        "Name" : "Rahul",
        "Age" : 29,
        "Job" : "Doctor"
    },
    {
        "Name" : "Vishal",
        "Age" : 19,
        "Job" : "Scientist"
    },
], index = ["Emp4", "Emp5", "Emp6"]
)
df = pd.concat([df, new_row])
print(df)