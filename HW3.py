# Task 1
def stringer(word):
    letters = set() # игнор повторяющихся букв
    new = []

    for letter in word:
        if letter.isalpha() and letter.lower() not in letters:
            letters.add(letter.lower())
            last = 'z' if letter.islower() else 'Z' # Привязываем регистр последующих букв к регистру исходной буквы
            strn = "".join(chr(c) for c in range(ord(letter), ord(last) + 1)) # Генерируем последовательность букв
            # по их коду от первого символа до последнего+1, чтобы он был включен в список.
            new.append(strn)

    return "".join(new) # Возвращаем в виде строки результат
print(stringer("pen"))
print(stringer("Doom"))

# Task 2
def places(arr):
    big = []
    rights = -float('inf') # Задаем последнее значение массива как минус бесконечность -float('inf'). Для того, чтобы
    # гарантированно вернуть последнее значение массива. Так как любое число больше чем минус бесконечность

    for num in reversed(arr): # перебираем массив справа налево
        if num > rights:
            big.append(num)
            rights = num #записываем результаты , соответствующие условию, последовательно

    return big[::-1] # переворачиваем обратно массив, чтобы создать верный порядок вывода
print(places([2, 0, 11, 14, 6, 9, 12, 3, 8, 4]))