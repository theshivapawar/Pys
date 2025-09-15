# 7. Reverse a list

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

fruits = ['Apple', 'Banana', 'Mango', 'Orange']

fruits_reversed = []

for i in range(len(fruits) - 1, -1, -1):
    fruits_reversed.append(fruits[i])

print(fruits_reversed)


cities = ['Mumbai', 'Pune', 'Dhule', 'Akola']
cities_reversed = []

for i in range(-1, -len(cities) - 1, -1):
    cities_reversed.append(cities[i])

print(cities_reversed)