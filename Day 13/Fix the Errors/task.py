try:
    age = int(input("How old are you?"))
except ValueError:
    print("Please only numbers e.g. 7")
    age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
