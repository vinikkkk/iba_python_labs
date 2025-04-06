class Tribonacci:
    def __init__(self, length=35):
        self.length = length

    def __iter__(self):
        # Начальные значения для генератора
        a, b, c = 0, 1, 1
        count = 0

        while count < self.length:
            yield a
            a, b, c = b, c, a + b + c
            count += 1


tribonacci_gen = Tribonacci()

for num in tribonacci_gen:
    print(num, end="; ")
