# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
import time
class TrafficLight:
    __color = 'цвет'

    def running(self):
        mode = ['красный', 'желтый', 'зеленый']
        print(f'{self.__color} {mode[0]}')
        time.sleep(7)
        print(f'{self.__color} {mode[1]}')
        time.sleep(2)
        print(f'{self.__color} {mode[2]}')
        time.sleep(10)

a = TrafficLight()
a.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
#вар1.
class Road:

    def __init__(self, _widght, _lenght):
        self.l = _lenght
        self.w = _widght

    def road_array(self):
        try:
            road_weight = int(input('масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см: '))
            road_cm = int(input('число см толщины полотна: '))
            res = self.w * self.l * road_cm * road_weight
        except ValueError:
            print('Вводим только числа')
        try:
            print(f'Необходимая масса асфальта: {self.w} кг * {self.l} кг * {road_cm} см * {road_weight} кг = {res} тонн.')
        except UnboundLocalError:
            print('Невозможно сделать рассчет, данные введены некорректно')
Road(23, 45).road_array()
#вар2.
class Road:
    _lenght = 567
    _widght = 6

    def road_array(self):
        road_weight = int(input('масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см: '))
        road_cm = int(input('число см толщины полотна: '))
        res = self._lenght * self._widght * road_cm * road_weight
        return f'Необходимая масса асфальта: {self._lenght} кг * {self._widght} кг * {road_cm} см * {road_weight} кг = {res} тонн.'

A = Road()
print(A.road_array())

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    name = input('Имя сотрудника: ')
    surname = input('Фамилия сотрудника: ')
    position = input('Должность сотрудника: ')
    wage = int(input('сумма оклада: '))
    bonus = int(input('сумма бонуса: '))
    _income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника на позиции {self.position}: {self.name} {self.surname}'

    def get_total_income(self):
        income = sum(self._income.values())
        return f'Сумма дохода: {income} рублей'

W1 = Position
print(W1.get_full_name(W1))
print(W1.get_total_income(W1))

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'скорость: {self.speed} км/ч, цвет: {self.color}, имя: {self.name}, машина является полицеской: {self.is_police}.')

    def go(self):
        print(f'машина выехала')

    def stop(self):
        print('машина остановилась')

    def turn(self):
        direction = input('куда едет машина?: ')
        print(f'машина едет {direction}')

    def show_speed(self):
        print(f'Текущая скороксть автомобиля {self.speed} км/ч.')


class TownCar(Car):
    def town_car(self):
        print('***Обратите внимание-это машина для города***')

    def show_speed(self):
        if self.speed < 60:
            print(f'Текущая скороксть автомобиля {self.speed} км/ч.')
        else:
            print('Внимание!!!!Скорость превышена!!!!')


class SportCar(Car):
    def sport_car(self):
        print('***Почти молния МакКуин***')


class WorkCar(Car):
    def work_car(self):
        print('***Обратите внимание - на этой машине работают***')

    def show_speed(self):
        if self.speed < 40:
            print(f'Текущая скороксть автомобиля {self.speed} км/ч.')
        else:
            print('Внимание! Скорость превышена!')


class PoliceCar(Car):
    def is_polise(self):
        print(f'!!Включите мигалку!!')


Car1 = Car(45, 'black', 'lexus', False)
Car1.go()
Car1.stop()
Car1.turn()
Car1.show_speed()

Car2 = TownCar(89, 'blue', 'civic', True)
Car2.town_car()
Car2.go()
Car2.stop()
Car2.turn()
Car2.show_speed()

Car3 = PoliceCar(110, 'white', 'audi', False)
Car3.go()
Car3.stop()
Car3.turn()
Car3.show_speed()
Car3.is_polise()

Car4 = SportCar(180, 'red', 'jaguar', False)
Car4.sport_car()
Car4.go()
Car4.stop()
Car4.turn()
Car4.show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = 'название отрисовки: '

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка кистью')


Stationery.draw(Stationery)
print(Stationery.title)
Art1 = Pen
Art1.draw(Art1)
print(Stationery.title)
Art2 = Pencil
Art2.draw(Art2)
print(Stationery.title)
Art3 = Handle
Art3.draw(Art3)
