class Count():
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def add(self, c):
        sum = self.x + self.y + c
        return sum

    def subtract(self):
        subtract = self.x - self.y
        return subtract

    def product(self):
        product = self.x * self.y
        return product

    def division(self):
        division = self.x / self.y
        return division

if __name__ == '__main__':
    count = Count(6, 3)
    print(count.add(2))
    print(count.subtract())
    print(count.product())
    print(count.division())