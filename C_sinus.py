import time
import math

# Класс итерируемых объектов с генератором
class SinusIterableWithGenerator:
    def __init__(self, steps, width):
        self.steps = steps
        self.width = width

    def __iter__(self):
        x = 0.0
        while True:
            x += math.pi * 2 / self.steps
            length = self.width / 2 + self.width / 2 * math.sin(x) + 1
            yield '#' * int(length)


# Главная программа
if __name__ == '__main__':
    main_iter = SinusIterableWithGenerator(64, 32)
    for line in main_iter:
        print(line)
        time.sleep(0.25)