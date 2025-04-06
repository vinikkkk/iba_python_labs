# 1. Реализуйте рекурсивную функцию нарезания прямоугольника с заданными
# пользователем сторонами a и b на квадраты с наибольшей возможной на каждом этапе
# стороной. Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.
def cut_rectangle(a, b):
    squares = []
    while a > 0 and b > 0:
        square_side = min(a, b)
        squares.append(square_side)

        # Обновляем размеры прямоугольника
        if a > b:
            a -= square_side
        else:
            b -= square_side

    return squares


# Вводим стороны прямоугольника
a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))

squares = cut_rectangle(a, b)

print(f"Количество квадратов: {len(squares)}")
print("Длины сторон полученных квадратов:", squares)