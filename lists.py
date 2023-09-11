#Learning About Unpacking.
#unpacking can be used in both tuples and list
coordinates = (1, 2, 3) 
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x, y, z = coordinates #This is a short hand version of the above code.
print(x)
print(y)
print(z)
print(x * z)

'''
#Learning Tuples
numbers = (1, 2, 3) # in tuples we can not chanche the values in the brakets.
print (numbers[0])

#if one wants to use a list that is not going to change in the program it is best to use Tuples.



#Learning list methods
numbers = [5, 2, 1, 7, 4]
numbers.append(13) # adds item to the end of list
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.insert(0, 10) #inserts item to the position you want in a list.
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.remove(7) #removes the item selected in a list
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.clear() #clears the list
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers.pop() #removes last item in list.
print(numbers)

numbers = [5, 2, 1, 7, 4]
print(numbers.index(2))# checks position of item in a list.

numbers = [5, 2, 1, 7, 4]
print(7 in numbers) # this checks position of item in a list and gives us a boolean value.

numbers = [5, 2, 1, 5, 7, 4]
print(numbers.count(5)) # this counts occurrences of item in list.

numbers = [5, 2, 1, 5, 7, 4]
print(numbers.sort()) # this sorts the list. but when we print we wont see the list

numbers = [5, 2, 1, 5, 7, 4]
numbers.sort() #but in this example we sorted the list and then print it after. 
print(numbers)

numbers = [5, 2, 1, 5, 7, 4]
numbers.sort()
numbers.reverse() # this will reverse the order of the list
print(numbers)

numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)


#practice remove duplicates from list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)




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