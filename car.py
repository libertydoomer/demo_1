class Car:
    def __init__(self, brand, year, mileage=0):
        self.brand = brand
        self.year = year
        self.mileage = mileage

    def start(self):
        print(f"Машина {self.brand}, {self.year} завелась.")

    def drive(self, x):
        if x < 0:
            print("Пробег не может уменьшаться!")
        else:
            self.mileage += x

    def refuel(self, liters):
        if liters < 0:
            print("Заправка не может быть отрицательной!")
        else:
            self.mileage += liters * 10

    def get_mileage(self):
        print(f"Пробег машины: {self.mileage}")

    def __str__(self):
        return f"{self.brand}, пробег: {self.mileage} км, год выпуска: {self.year} \n"

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.mileage == other.mileage
        return False


my_car = Car("Приора", "2007")
my_car.start()
my_car.drive(100)
my_car.refuel(10)
my_car.get_mileage()
print(my_car)

another_car = Car("Мицуга", "2011")
another_car.start()
another_car.drive(100)
another_car.refuel(10)
another_car.get_mileage()
print(another_car)

print(my_car == another_car)
