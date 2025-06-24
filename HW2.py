from itertools import count

arr1 = [1, 5, 6, 23, 12, 67, 33, 42]
arr2 = [-2, -14, -7, -9, -13, -17, -50, -4]
sum1 = 0
sum2 = 0
#Task 1 Подсчет среднего арифметического значений массивов.
for i in arr1:
    sum1 += i
midsum1 = sum1 / len(arr1)
print(f"Сред.Ар1:{midsum1}")
for v in arr2:
    sum2 += v
midsum2 = sum2 / len(arr2)
print(f"Сред.Ар2:{midsum2}")
#Task 2 ахождение минимальных значений элементов в каждом из массивов
mini1 = arr1[0]
mini2 = arr2[0]
for i in range(len(arr1)):
    if arr1[i] < mini1:
        mini1 = arr1[i]
    if arr2[i] < mini2:
        mini2 = arr2[i]
print(f"Минимум1: {mini1}")
print(f"Минимум2: {mini2}")
#Task 3 Сложение значений элементов с одинаковыми индексами
arr3 = []
for i in range(len(arr1)):
    arr3.append(arr1[i] + arr2[i])
print(f"Сумма значений: {arr3}")
#Task 4
word = "синхрофазотрон"
# import re
# _finds = re.findall(r'[йёуяыаеоиэю]', word) #Нахождение совпадений с заданными символами в строке(Тут гласные)
# print(_finds)
# __finds = re.findall(r'[цфвчкспмрнгтьблшщджзхъ]', word) # То же самое для согласных и "ь" и "ъ"
# print(__finds) Это можно использовать для поиска совпадений, но по заданию надо через цикл.
vows = "йёуяыаеоиэю"
cons = "цфвчкспмрнгтьблшщджзхъ"
vowsFounds = []
for i in word:
    if i in vows:
        vowsFounds.append(i)
print(vowsFounds)
consFounds = []
count = 0
for con in word:
    if con in cons:
        count += 1
print(f"Количество согласных: {count}")
# Task 5
sumOfInds = 0
for i, char in enumerate(word):
    if char in vows:
        sumOfInds += i
print(f"Сумма индексов: {sumOfInds}")
# Task 6 Coffee
drinks = ['Espresso', 'Kappuchino', 'Latte', 'Ice latte', 'Moccachino']
prices = [150, 160, 185, 190, 210]
toppings = ['Orange', 'Mint', 'Menthol', 'Nut']
toppPrice = [30, 40, 65, 70]
portions = ['little', 'middle', 'big']
volumeOfPortions = [0.8, 1, 1.3]
print("Выберите напиток:")
for i, drink in enumerate(drinks, 1):
    print(f"{i} - {drink}")
drink_choice = int(input("Введите номер напитка: ")) - 1

print("\nВыберите порцию:")
for i, portion in enumerate(portions, 1):
    print(f"{i} - {portion}")
portion_choice = int(input("Введите номер порции: ")) - 1

print("\nВыберите топпинг:")
for i, topping in enumerate(toppings, 1):
    print(f"{i} - {topping}")
topping_choice = int(input("Введите номер топпинга: ")) - 1

total_price = volumeOfPortions[portion_choice] * prices[drink_choice] + toppPrice[topping_choice] # Расчет цены

print("\nВы выбрали:")
print(f"Напиток: {drinks[drink_choice]}")
print(f"Порция: {portions[portion_choice]}")
print(f"Топпинг: {toppings[topping_choice]}")
print(f"Итоговая цена: {total_price:} руб.")