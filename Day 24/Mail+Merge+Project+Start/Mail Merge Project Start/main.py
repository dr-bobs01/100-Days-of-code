#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

## get start names
with open("Input/Names/invited_names.txt") as file:
    names = (file.readlines())
# print(names[0])

## get start letter
with open("Input/letters/starting_letter.txt") as file:
    start_letter = file.read()
    # print(start_letter)

new_names = []
for name in names:
    new_name = name.strip()
    new_names.append(new_name)

print(names)
print(new_names)

## make letters
for name in new_names:
    new_letter = start_letter.replace("[name]",name)
    print(new_letter.strip())
    # print("#############")
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        file.write(new_letter.strip())
