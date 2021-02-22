# импортируем функции из библиотеки math для рассчёта расстояния
from math import radians, sin, cos, acos

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    # считаем расстояние между двумя точками в км
    def distance(self, other):
        cos_d = sin(self.latitude) * sin(other.latitude) + cos(self.latitude) * cos(other.latitude) * cos(
        self.longitude - other.longitude)
        return 6371 * acos(cos_d)

class City(Point):
    def __init__(self, latitude, longitude, name, population):
        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self):
        print(f"Город {self.name}, население {self.population} чел.")

class Mountain(Point):
    def __init__(self, latitude, longitude, name, height):
        super().__init__(latitude, longitude)
        self.name = name
        self.height = height
    
    def show(self):
        print(f"Высота горы {self.name} - {self.height} м.")

city = City(55,37,'Moscow',12000000)
mountain = Mountain(28,87,"Everest",8848)
print(city.distance(mountain))
