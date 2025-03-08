import time

# Класс объектов, которые одновременно итерируемые и итераторы
class RangeIterableIterator:
    def __init__(self, size):
        self.x = size

    def __iter__(self):
        return self

    def __next__(self):
        self.x -= 1
        if self.x <= 0:
            raise StopIteration
        return '#' * self.x


# Главная программа
if __name__ == '__main__':
    main_iter = RangeIterableIterator(32)
    for line in main_iter:
        print(line)
        time.sleep(0.25)