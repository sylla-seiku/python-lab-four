#learning lists
name = ['Seiku', 'Beyage', 'Ebrahim', 'Ahamadou', 'Kadijatou']
print(name)
print(name[0])
print(name[2])
print(name[2:])

name = ['Seiku', 'Beyage', 'Ebrahim', 'Ahamadou', 'Kadijatou']
name [0] = 'Saikou' #how to change a value in a list.
print(name)

#practice: write a program that gives me the largest number
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number

print(max)