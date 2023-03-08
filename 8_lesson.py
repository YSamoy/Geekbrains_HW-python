# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# © geekbrains.ru 16
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    def __init__(self, li):
        self.l = li
    @classmethod
    def get_data(cls, li):
        cls.li = li
        n_el = ''
        for el in li.l:
            n_el = ''.join([n_el, (el if el in '1234567890' else ' ')])
        day = int(n_el.split()[0])
        month = int(n_el.split()[1])
        year = int(n_el.split()[2])
        li = day, month, year
        return li

    @staticmethod
    def date_valid(obj):
        day, month, year = obj.get_data(obj)
        if day >=1 and day <= 31:
            print(f'{day}')
        else:
            print('день введен некорректно')
        if month >=1 and month <= 12:
                print(f'{month}')
        else:
            print('месяц введен некорректно')
        if year >= 0 and day <= 2022:
            print(f'{year}')
        else:
            print('год введен некорректно')

d1 = Data('01-13-2016')
print(d1.get_data(d1))
d1.get_data(d1)
d1.date_valid(d1)


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroD(Exception):
    def __int__(self, txt):
        self.t = txt
while True:
    try:
        num1 = int(input('Введите числитель '))
        num2 = int(input('Введите знаменатель '))

        if num2 == 0:
            raise ZeroD('на ноль делить нельзя')

    except ValueError:
        print('вводим только числа')
    except ZeroD as err:
        print(err)
    else:
        res = num1 / num2
        print(f'частное: {res}')
        break

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.

class OnlyN(Exception):
    def __int__(self, txt):
        self.t = txt
total = []
while True:
    try:
        num = input('Введите список из чисел: ')
        for el in range(0, len(num)):
            if num[el] in '0123456789':
                total.append(num[el])
            else:
                raise OnlyN('В списке могут быть только числа. Для прекращения работы введите stop')
    except OnlyN as err:
       print(err)
       if num == 'stop':
           print(total)
           break

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.
#
class CompN:

    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def __add__(self, other):
        return f'{self.n1+other.n1} + {self.n2+other.n2}*i'

    def __mul__(self, other):
        r1 = (self.n1 * other.n1) - (self.n2 * other.n2)
        r2 = (self.n1*other.n2) + (other.n1*self.n2)
        return f'{r1} + i*{r2}'

a = CompN(1, 3)
b = CompN(4, 8)

print(a+b)
print(a*b)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
class Shopping_mall:
    def __init__(self):
        self.capacity = 100
        self.name = 'Цветочная поляна'

    @staticmethod
    def order_valid(obg):
        if obg.units <= obg.capacity:
            return f'Заказ оформлен'

class Cut_flowers(Shopping_mall):
    def __init__(self, f_name, units):
        Shopping_mall.__init__(self)
        self.f_name = f_name
        self.units = units

    def __add__(self, other):
        res = self.units + other.units
        return Cut_flowers(self.f_name + 'и' + other.f_name, res)


r = Shopping_mall()
print(r.name)
rq1 = Cut_flowers('Гербера', 3)
rq2 = Cut_flowers('Розы', 7)
rq3 = Cut_flowers('Пион', 12)

z1 = (rq1+rq2+rq3)
print(Shopping_mall.order_valid(z1))
print((rq1+rq2+rq3).f_name)


