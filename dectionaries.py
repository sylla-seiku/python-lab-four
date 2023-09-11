# Learning About dictionaries.
customer = {
    "name": "Seiku Sillah",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Beyage Sillah" # this changes the value of name in the dictionary.
customer["birthdate"] = "Aug 5, 1995" # this functions adds a value to the dictionary.

print(customer["name"])
#print(customer["birthplace"]) # because this not exist in our dectionary it returns an error in the terminal.
print(customer.get("birthdate")) # with get it returns "None" instead of an Error.
print(customer.get("birthplace", "Data does not exist")) # in this line i can input a message to show instead of "None".


# practice turn phone number into words
phone = input("Phone: ")
digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "

print(output)
