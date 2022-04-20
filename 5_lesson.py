# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
with open(r'new_file.txt', 'w', encoding='utf-8') as f1:
    while True:
        d = input(f'Введите данные: ')
        f1.writelines(f'\n{d}')
        if len(d) == 0:
            break
# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
with open(r'2_task.txt', 'r', encoding='utf-8') as f2:
    li = f2.readlines()
    for i, el in enumerate(li, 1):
        q = len(el)
        print(f'В {i} строчке {q} символов.')

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.

with open(r'3_task.txt', 'r', encoding='utf-8') as f3:
    content3 = f3.readlines()
    answ1 = []
    answ2 = []
    for el in content3:
        i = float(el.split()[1])
        answ2.append(i)
        Answ2 = sum(answ2)/len(content3)
        if i > 20000:
            answ1.append(el.split()[0])
    print(f'Заработная плата больше 20000руб у {answ1}. Средняя величина дохода сотрудников {round(Answ2)} руб.')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
with open(r'4_task.txt', 'r', encoding='utf-8') as f4:
    with open(r'task4_answer.txt', 'w+', encoding='utf-8') as ans_f4:
        content4 = f4.readlines()
        dict4 = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре',  'Five': 'Пять', 'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять'}
        for el in content4:
            for i in dict4.keys():
                if i == el.split()[0]:
                    ans_f4.write(el.replace(i, dict4.get(i)))

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open(r'5_task.txt', 'w+') as f5:
   print(1,8,13,14,45,67,90,123,678,902, file=f5)
with open(r'5_task.txt', 'r+') as f5:
    for el in f5.readlines():
        sum_f5 = 0
        for i in el.split():
            sum_f5 = int(i) + sum_f5
        print(f'Сумма чисел в файле: {sum_f5}')
# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
import re
with open(r'6_task.txt', 'r+', encoding='utf-8') as f6:
    dict_6 = {}
    for el in f6.readlines():
        nums = re.findall(r'\d+', str(el.split()))
        nums = [int(n) for n in nums]
        dict6 = {el.split()[0]: sum(nums)}
        dict_6.update(dict6)
    print(dict_6)
#7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
import json
with open(r'7_task.txt', "r+", encoding='utf-8') as f7:
    li_ebit = []
    li_name = []
    li7_profit = {}
    li7_loss = {}
    for el in f7.readlines():
        ebit7 = int(el.split()[2]) - int(el.split()[3])
        li_ebit.append(ebit7)
        li_name.append(el.split()[0])
        if ebit7 < 0:
            dict_loss = {el.split()[0]:ebit7}
            li7_loss.update(dict_loss)
        else:
            dict_profit = {el.split()[0]: ebit7}
            li7_profit.update(dict_profit)
    dict7_1 = {'average ebit':round(sum(li_ebit)/len(li_name))}
    li7 = [li7_profit, li7_loss, dict7_1]
print(li7)
with open(r'7_task.json', 'w', encoding='utf-8') as f7_json:
    json.dump(li7, f7_json)






