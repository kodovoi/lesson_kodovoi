class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.filled = False
        # Проверка количества сторон и инициализация сторон
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        # Проверка корректности значений цвета
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        # Установка нового цвета, если значения корректны
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        # Проверка корректности новых сторон
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides  # Возвращает текущие стороны

    def __len__(self):
        return sum(self.__sides)  # Возвращает периметр фигуры

    def set_sides(self, *new_sides):
        # Установка новых сторон, если они корректны
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1  # Количество сторон круга

    def __init__(self, color, *sides):
        super().__init__(color, *sides)  # Вызов конструктора родительского класса
        self.__radius = self._Figure__sides[0] / (2 * 3.141592653589793)  # Расчет радиуса

    def get_square(self):
        # Возвращает площадь круга
        return 3.141592653589793 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3  # Количество сторон треугольника

    def get_square(self):
        a, b, c = self.get_sides()  # Получение сторон треугольника
        s = (a + b + c) / 2  # Полупериметр
        # Возвращает площадь треугольника по формуле Герона
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12  # Количество сторон куба

    def __init__(self, color, *sides):
        # Если передана одна сторона, дублируем её 12 раз
        if len(sides) == 1:
            sides = sides * 12
        super().__init__(color, *sides)  # Вызов конструктора родительского класса

    def get_volume(self):
        side = self._Figure__sides[0]  # Получение одной стороны куба
        return side ** 3  # Возвращает объём куба


# Код для проверки:

circle1 = Circle((200, 200, 100), 10)  # Создание круга с цветом и стороной
cube1 = Cube((222, 35, 130), 6)  # Создание куба с цветом и стороной

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # Вывод нового цвета круга

cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # Вывод старого цвета куба

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # Вывод старых сторон куба

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # Вывод новой стороны круга

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Вывод периметра круга

# Проверка объёма (куба):
print(cube1.get_volume())  # Вывод объёма куба
