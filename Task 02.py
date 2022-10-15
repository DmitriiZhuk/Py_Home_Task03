# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

fruitsList = []
clearFruitsList = []

# открываю файл и забираю все в массив без \n
with open("Task02.txt", "r", encoding="utf-8") as file:
    fruitsList = file.read().splitlines()

# в массиве есть пустые элементы, не тяну их в новый массив
for elem in fruitsList:
    if len(elem) > 0:
        clearFruitsList.append(elem)

search_1st_symbol = input("Введите букву:")

for clear_elem in clearFruitsList:
    if clear_elem[0].lower() == search_1st_symbol.lower():
        print(clear_elem, end=", ")

