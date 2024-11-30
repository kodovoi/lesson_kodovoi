import random  # Импортируем модуль random для генерации случайных чисел

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        new_z = self._cords[2] + dz * self.speed  # Вычисляем новое значение координаты z
        if new_z < 0:
            print("Слишком глубоко, я не могу нырнуть :(")  # Если новое значение координаты z меньше 0, выводим сообщение
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
        eggs_count = random.randint(1, 4)  # Генерируем случайное число яиц (от 1 до 4)
        print(f"Вот {eggs_count} яйца для тебя")  # Выводим сообщение о количестве яиц

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Изменяем степень опасности на 3

    def __init__(self, speed):
        super().__init__(speed)  # Вызываем конструктор родительского класса

    def dive_in(self, dz):
        new_z = self._cords[2] - abs(dz) * (self.speed / 2)  # Вычисляем новое значение координаты z для ныряния
        if new_z < 0:
            print("Здесь слишком глубоко, я не могу нырнуть :(")  # Если новое значение координаты z меньше 0, выводим сообщение
        else:
            self._cords[2] = new_z  # Обновляем координату z

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Изменяем степень опасности на 8

    def __init__(self, speed):
        super().__init__(speed)  # Вызываем конструктор родительского класса

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"  # Атрибут класса, указывающий звук, который издает утконос

    def __init__(self, speed):
        super().__init__(speed)  # Вызываем конструктор родительского класса

# Создание объекта класса Duckbill
db = Duckbill(10)  # Создаем объект класса Duckbill с начальной скоростью 10

# Пример работы программы
print(db.live)  # Выводим значение атрибута live (True)
print(db.beak)  # Выводим значение атрибута beak (True)

db.speak()  # Выводим звук, который издает утконос ("Click-click-click")
db.attack()  # Выводим сообщение в зависимости от степени опасности ("Будь осторожен, я атакую тебя 0_0")

db.move(1, 2, 3)  # Изменяем координаты утконоса на (10, 20, 30)
db.get_cords()  # Выводим текущие координаты утконоса

db.dive_in(6)  # Изменяем координату z утконоса на 0
db.get_cords()  # Выводим текущие координаты утконоса

db.lay_eggs()  # Выводим сообщение о количестве яиц, которые отложил утконос


