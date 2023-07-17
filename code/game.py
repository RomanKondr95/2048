from random import random
mas = [[0] * 4 for i in range(4)]

def pretty_mas(mas)->list:
    print('-'*10)
    for row in mas:
        print(*row)
    print('-'*10)

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

def two_or_four(mas,x,y):
    """
    функция подставляет рандомно 2 или 4
    
    """
    if random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas

     
def get_empty_list(mas)->list:
        empty = []
        for row in range(4):
             for col in range(4):
                  if mas[row][col] == 0:
                       num = get_num_from_ind(row,col)
                       empty.append(num)
        return empty


mas[1][2] = 2
mas[3][0] = 4
# print(pretty_mas(mas))
# print(get_empty_list(mas))