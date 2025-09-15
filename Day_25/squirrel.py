import pandas

data = pandas.read_csv("./Squirrel_Data.csv")
squirrels_color_data = data["Primary Fur Color"].to_list()

grey = len(data[data['Primary Fur Color'] == "Gray"])
red = len(data[data['Primary Fur Color'] == "Cinnamon"])
black = len(data[data['Primary Fur Color'] == "Black"])

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey, red, black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
