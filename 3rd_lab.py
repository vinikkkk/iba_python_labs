def dog_to_human (dog_years):
    if dog_years == 1:
        return 14
    elif dog_years == 2:
        return 22
    else:
        return 22 + (dog_years - 2) * 5
#
# # Пример
dog_years = 5
human_years = dog_to_human(dog_years)
print(str(dog_years)+ " года(лет) собаки соответствует " + str (human_years)+ " человеческим годам.")


#1 task
def square(x):
    return x**2
items = [1, 2, 3, 4, 5]

squared= list(map(square, items))
print(squared)

#2 task
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)

#4
x = [1, 2, 3]
y = [4, 5, 6]
res = list(zip(x, y))
print (res)

#5
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

for hero, real_name in zip(name_hero, name_real):
    print(hero, '-', real_name)

#6

numbers = [1, 2, 4, 5, 7, 8, 10, 11]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(numbers)
print(odd_numbers)