import io

# Главная программа
if __name__ == '__main__':
    main_iter = io.open('C:/Users/user/Downloads/iters_and_gens_data/food.csv', encoding='ANSI')

    print("Игра \"Съедобное-несъедобное\".")

    print("Введите 0, если предмет несъедобный, и 1, если съедобный.")
    input("Нажмите Enter, чтобы начать...")

    score = 0
    for line in main_iter:
        cells = line.strip().split(';')
        print(cells[0])
        inbuf = input()
        if inbuf and inbuf[0] == cells[1][0]:
            print("Правильно!")
            score += 1
        else:
            print("Неправильно!")
    print(f"Вы набрали {score} очков.")
    print("КОНЕЦ.")