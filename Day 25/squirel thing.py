import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250614.csv")

# print(data)

data_dict = {
    "fur color": ["grey", "cinnamon", "black"],
    "count": [0, 0, 0],
}

for squirrel in data["Primary Fur Color"]:
    if squirrel == "Gray":
        data_dict["count"][0] += 1
    elif squirrel == "Cinnamon":
        data_dict["count"][1] += 1
    elif squirrel == "Black":
        data_dict["count"][2] += 1
    else:
        pass

print(data_dict)

databot = pandas.DataFrame(data_dict)
databot.to_csv("squirrel_data.csv")
