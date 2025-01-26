import io
import numpy

# главная программа:
# создание итерируемого объекта - строк файла
if __name__ == '__main__':
    load_iter = io.open('food2.csv', encoding='ANSI')
lines = []
isFood = []
for line in load_iter:
    cells = line.strip().split(';')
    lines.append(cells[0])
    isFood.append(cells[1])

main_iter = numpy.random.permutation(len(lines))

print("Игра \"Съедобное-несъедобное\".")

print("Введите 0, если предмет несъедобный, и 1, если съедобный.")
input("Нажмите Enter, чтобы начать...")
score = 0
for idx in main_iter:
    print(lines[idx])
    inbuf = input()
    if inbuf and inbuf[0] == isFood[idx][0]:
        print("Правильно!")
        score += 1
    else:
        print("Неправильно!")
print(f"Вы набрали {score} очков.")
print("КОНЕЦ.")