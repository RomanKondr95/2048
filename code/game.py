from random import *
import pygame
import sys

def drawing_interface():
    """
    прорисовка интерфейса

    """
    pygame.draw.rect(screen,WHITE,title_rec)
    font = pygame.font.SysFont('arial', 70)
    pretty_mas(mas)
    for row in range(block):
        for col in range(block):
            value = mas[row][col]
            text = font.render(f'{value}',True, BLACK)
            x = col * size_block + (col+1) * margin
            y = row * size_block + (row+1) * margin + size_block
            pygame.draw.rect(screen,COLORS[value],(x,y,size_block,size_block))
            if value != 0:
                font_w, font_h = text.get_size()
                text_x = x + (size_block - font_w) / 2
                text_y = y + (size_block - font_h) / 2
                screen.blit(text,(text_x,text_y))


mas = [[0] * 4 for i in range(4)]
WHITE = (255,255,255)
SILVER =(192,192,192)
BLACK = (0,0,0)
COLORS = {
    0: (128, 128, 128),
    2: (255,255,255),
    4: (255, 255, 0),
    8: (255, 165, 0),
    16:(255, 69, 0),
    32: (250, 128, 114),
    64: (255, 0, 0),
    128: (139, 0, 0),
    256: (255, 0, 255),
    512: (128, 0, 128),
    1024:(0, 128, 128),
    2048: (0, 0, 128)
}

block = 4
size_block = 110
margin = 10
widht = block * size_block + (block + 1) * margin
height = widht + 110
title_rec = pygame.Rect(0,0,widht,110)


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

def two_or_four(mas,x,y)->list:
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
    фуекция обрабатывает движение влево

    """
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j+1)
                mas[i].append(0)
    return mas

def move_right(mas):
    """
    фуекция обрабатывает движение вправо

    """
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3,0,-1):
            if mas[i][j] == mas[i][j-1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j-1)
                mas[i].insert(0,0)
    return mas
    

mas[1][2] = 2
mas[3][0] = 4

pygame.init()
screen = pygame.display.set_mode((widht,height))
pygame.display.set_caption('2048')

drawing_interface()
pygame.display.update()
while is_zero(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mas = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas = move_right(mas)
            empty = get_empty_list(mas)
            shuffle(empty)
            num = empty.pop()
            x,y = get_ind_from_num(num)
            mas = two_or_four(mas,x,y)
            drawing_interface()
            pygame.display.update()



               
               
     


