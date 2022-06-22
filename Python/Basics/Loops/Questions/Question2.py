# Write a program to greet all the names stored in a list which starts with the letter N

names = ["Nim", "Shashank", "Frazer", "Lemon", "Nimmo"]

for i in names:
    if i.lower().startswith("n"): # Checks if the name starts with N
        print(i)