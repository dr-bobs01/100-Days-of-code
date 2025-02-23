programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"])

# Add something onto a dictionary
programming_dictionary["loop"] = "The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary = {}
empty_dictionary[1] = "a"

# # Wipe and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "insect"

# Loop through dictionary
for key in programming_dictionary:
    # print(key)
    # print(programming_dictionary[key])
    print(f"{key}: {programming_dictionary[key]}")
