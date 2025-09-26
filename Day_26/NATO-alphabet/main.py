import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('./nato_phonetic_alphabet.csv')
# print(data)
formatted_data = {row["letter"]:row["code"] for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word : ").upper()
formated_list = [value for (key, value) in formatted_data.items() if key in word]
print(formated_list)