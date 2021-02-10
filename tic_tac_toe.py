import os
import random

def who_is_first():
    print('Кто будет ходить первым?\n1 - Вы, 2 - компьтер')
    while True:
        a = input().strip()
        if a not in ['1', '2']:
            print('Введены некорректные данные. Повторите ввод:')
            continue
        return 1 if a == '1' else -1


def print_field():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('', 0, 1, 2, sep='\t')
    for i in range(3):
        print(i, end='\t')
        for j in range(3):
            if table[i][j] * fl == 1:
                print('X', end='\t')
            elif table[i][j] * fl == -1:
                print('O', end='\t')
            else:
                print('-', end='\t')
        print('')


def take_coord():
    x = 'крестик' if fl == 1 else 'нолик'
    try:
        coord = list(map(int, input(
            f'Выберите, куда поставить {x}(введите через пробел 2 цифры: номер строки и номер столбца):\n').split()))
    except ValueError:
        print('Введенными данными должны быть целые числа')
        return
    if len(coord) != 2:
        print('Должно быть 2 целых числа')
        return
    if any([coord[0] < 0,
            coord[0] > 2,
            coord[1] < 0,
            coord[1] > 2]):
        print('Введены некорректные координаты')
        return
    return coord


def change_table(coord):
    i, j = coord
    if table[i][j] == 0:
        table[i][j] = 1
        table_list.remove((i, j))
        return True
    else:
        print('Выбранная ячейка уже занята')
        return False


def comp_move():
    dict_analis = {('j', j): 0 for j in range(3)}
    dict_analis[('ij', 0)] = dict_analis[('ij', 1)] = 0
    for i in range(3):
        dict_analis[('i', i)] = sum(table[i], 0)
        dict_analis[('j', 0)] += table[i][0]
        dict_analis[('j', 1)] += table[i][1]
        dict_analis[('j', 2)] += table[i][2]
        dict_analis[('ij', 0)] += table[i][i]
        dict_analis[('ij', 1)] += table[i][2 - i]
    for i in dict_analis.values():
        if i == 3:
            print_field()
            print('Вы выиграли')
            return True
    for key, value in dict_analis.items():
        if value == -2:
            comp_vin_no_lose(key)
            print_field()
            print('Вы проиграли')
            return True
    for key, value in dict_analis.items():
        if value == 2:
            comp_vin_no_lose(key)
            return
    comp_move_random()


def comp_vin_no_lose(line):
    if line[0] == 'i':
        for j in range(3):
            if table[line[1]][j] == 0:
                table[line[1]][j] = -1
                table_list.remove((line[1], j))
                return
    elif line[0] == 'j':
        for i in range(3):
            if table[i][line[1]] == 0:
                table[i][line[1]] = -1
                table_list.remove((i, line[1]))
                return
    elif line[1] == 0:
        for i in range(3):
            if table[i][i] == 0:
                table[i][i] = -1
                table_list.remove((i, i))
                return
    else:
        for i in range(3):
            if table[2 - i][i] == 0:
                table[2 - i][i] = -1
                table_list.remove((2 - i, i))
                return


def comp_move_random():
    i, j = random.choice(table_list)
    table[i][j] = -1
    table_list.remove((i, j))
    return


table = [[0 for i in range(3)] for j in range(3)]
table_list = [(i, j) for i in range(3) for j in range(3)]
os.system('cls' if os.name == 'nt' else 'clear')
fl = who_is_first()
if fl == -1:
    comp_move()
print_field()
while True:
    if not table_list:
        print('Ничья')
        break
    coord = take_coord()
    if not coord:
        continue
    if not change_table(coord):
        continue
    if not table_list:
        print_field()
        print('Ничья')
        break
    if comp_move():
        break
    print_field()