class Car:
    def __init__(self, color, wheel, type, price):
        self.color = color
        self.wheel = wheel
        self.type = type
        self.price = price
bmw = Car("black", 4, "sedan", 50000)

print(bmw.color)
print(bmw.wheel)
print(bmw.type)
print(bmw.price)