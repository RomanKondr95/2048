from random import *
import pygame
import sys


mas = [[0] * 4 for i in range(4)]
WHITE = (255,255,255)
SILVER =(192,192,192)

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
    

mas[1][2] = 2
mas[3][0] = 4

pygame.init()
screen = pygame.display.set_mode((widht,height))
pygame.display.set_caption('2048')


while is_zero(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen,WHITE,title_rec)
            for row in range(block):
                for col in range(block):
                    x = col * size_block + (col+1) * margin
                    y = row * size_block + (row+1) * margin + 110
                    pygame.draw.rect(screen,SILVER,(x,y,110,110))
            empty = get_empty_list(mas)
            shuffle(empty)
            num = empty.pop()
            x,y = get_ind_from_num(num)
            mas = two_or_four(mas,x,y)
            pretty_mas(mas)
    pygame.display.update()



               
               
     


