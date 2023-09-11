#learning 2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = [20]
print(matrix[0][1])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)



'''
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
'''