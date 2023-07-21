from random import *
from copy import deepcopy
def get_num_from_ind(i,j) -> int:
    """
    функция получает число по индексу массива

    """
    return i * 4 + j+ 1

def get_ind_from_num(num)->int:
    """
    функция получает индекс массива по числу

    """
    num-=1
    x,y = num//4,num%4
    return x,y

def get_empty_list(mas)->list:
    empty = []
    for row in range(4):
        for col in range(4):
            if mas[row][col] == 0:
                num = get_num_from_ind(row,col)
                empty.append(num)
    return empty

def is_zero(mas)->bool:
    """
    функция проверяет есть ли нули в массиве

    """
    for row in mas:
        if 0 in row:
            return True
    return False 

def move_left(mas):
    """
    функция обрабатывает движение влево

    """
    origin = deepcopy(mas)
    count = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                count += mas[i][j]
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas,count,not origin == mas

def move_right(mas):
    """
    функция обрабатывает движение вправо

    """
    origin = deepcopy(mas)
    count = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3,0,-1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] *= 2
                count += mas[i][j]
                mas[i].pop(j-1)
                mas[i].insert(0,0)
    return mas,count,not origin == mas

def move_up(mas):
    """
    функция обрабатывает движение вверх

    """
    origin = deepcopy(mas)
    count = 0
    for j in range(4):
        col = []
        for i in range(4):
            if mas[i][j] != 0:
                col.append(mas[i][j])
        while len(col) != 4:
            col.append(0)
        for i in range(3):
            if col[i] == col[i+1] and col[i] != 0:
                col[i] *=2
                count += col[i]
                col.pop(i+1)
                col.append(0)
        for i in range(4):
            mas[i][j] = col[i]
    return mas,count,not origin == mas

def move_down(mas):
    """
    функция обрабатывает движение вниз

    """
    origin = deepcopy(mas)
    count = 0
    for j in range(4):
        col = []
        for i in range(4):
            if mas[i][j] != 0:
                col.append(mas[i][j])
        while len(col) != 4:
            col.insert(0,0)
        for i in range(3,0,-1):
            if col[i] == col[i-1] and col[i] != 0:
                col[i] *=2
                count += col[i]
                col.pop(i-1)
                col.insert(0,0)
        for i in range(4):
            mas[i][j] = col[i]
    return mas,count,not origin == mas

def is_can_move(mas):
    """
    функция проверяет возможно ли движение
    """
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] or mas[i][j] == mas[i+1][j] or mas[i][j] == mas[i][j-1] or mas[i][j] == mas[i-1][j]:
                return True
    return mas[3][3] == mas[3][2] or mas[3][3]==mas[2][3]

def two_or_four(mas,x,y)->list:
    """
    функция подставляет рандомно 2 или 4
    
    """
    if random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas