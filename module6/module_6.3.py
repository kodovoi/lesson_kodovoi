import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("Слишком глубоко, я не могу нырнуть :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] = new_z

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Извините, я мирный :)")
        else:
            print("Будь осторожен, я атакую тебя 0_0")

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        eggs_count = random.randint(1, 4)
        print(f"Вот {eggs_count} яйца для тебя")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        new_z = self._cords[2] - abs(dz) * (self.speed / 2)
        if new_z < 0:
            print("Здесь слишком глубоко, я не могу нырнуть :(")
        else:
            self._cords[2] = new_z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

# Создание объекта класса Duckbill
db = Duckbill(10)


print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()

db.dive_in(6)
db.get_cords()

db.lay_eggs()


