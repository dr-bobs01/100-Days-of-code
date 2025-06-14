# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     # print(file)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

## pandas data library ##

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print("\n")
# print(data["temp"])

# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# ## figure out the average
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
#
# ## "max" value in csv
# print(data["temp"].max())
#
# ## get data in columns
# print(data["condition"])
# print(data.condition)

# ## Get data in row
# ## first get column then say which row it is by using an example
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

## get the temperature from monday then turn it to Celsius
monday = data[data.day == "Monday"]
print((monday.temp[0] * 9/5) + 32)

## Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
databot = pandas.DataFrame(data_dict)
databot.to_csv("new_data.csv")

