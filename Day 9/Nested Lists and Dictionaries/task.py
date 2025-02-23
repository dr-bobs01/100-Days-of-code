nested_example = {
    1: ["a","b","c"],
    2: ["d","e","f"],
}

# Pause 1
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# # Print lille? incorrect
# print(travel_log["France"[1]])
# Print lille
print(travel_log["France"][1])

# Pause 2
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

# Pause 3
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}
# # attempt 1
# print(travel_log[1][0][2])
# answer
print(travel_log["Germany"]["cities_visited"][2])
