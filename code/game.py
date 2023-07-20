from random import *
import pygame
import sys
from database import get_best,cur,insert_res

GAMERS_DB = get_best()
USERNAME = None

def drawing_top():
    font_top = pygame.font.SysFont('stxingkai',30)
    font_gamer = pygame.font.SysFont('arial',20)
    text_head = font_top.render('Best tries: ', True, BLACK)
    screen.blit(text_head, (350,5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index+1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, BLACK)
        screen.blit(text_gamer, (350, 33 + 20 * index))
    


def drawing_interface(score):
    """
    прорисовка интерфейса

    """
    pygame.draw.rect(screen,(222, 184, 135),title_rec)
    font = pygame.font.SysFont('arial', 70)
    font_score = pygame.font.SysFont('stxingkai',70)
    text_score = font_score.render('Score: ', True, BLACK)
    text_score_value = font_score.render(f'{score}', True, BLACK)
    screen.blit(text_score,(20,35))
    screen.blit(text_score_value,(200,35))
    pretty_mas(mas)
    drawing_top()
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
score = 0


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
    функция обрабатывает движение влево

    """
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
    return mas,count

def move_right(mas):
    """
    функция обрабатывает движение вправо

    """
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
    return mas,count

def move_up(mas):
    """
    функция обрабатывает движение вверх

    """
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
    return mas,count

def move_down(mas):
    """
    функция обрабатывает движение вниз

    """
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
    return mas,count

def is_can_move(mas):
    """
    функция проверяет возможно ли движение
    """
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j+1] or mas[i][j] == mas[i+1][j] or mas[i][j] == mas[i][j-1] or mas[i][j] == mas[i-1][j]:
                return True
    return False




    

mas[1][2] = 2
mas[3][0] = 4

pygame.init()
screen = pygame.display.set_mode((widht,height))
pygame.display.set_caption('2048')

def drawing_intro():
    """
    функция обрабатывает заставку игры

    """
    img = pygame.image.load('images.jpg')
    font_welcome = pygame.font.SysFont('stxingkai',50)
    font_name = pygame.font.SysFont('arial',50)
    text_welcome = font_welcome.render('WELCOME!',True,(255,0,0))
    name = 'Enter your name'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter your name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break
    

        screen.fill(BLACK)
        text_name = font_name.render(name,True,(255,255,255))
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img,[210,210]),[5,5])
        screen.blit(text_welcome,(230,80))
        screen.blit(text_name,rect_name)
        pygame.display.update()
    screen.fill(BLACK)


def drawing_game_over():
    """
    функция обрабатывает конечную звставку

    """
    img = pygame.image.load('img.jpg')
    font_game_over = pygame.font.SysFont('stxingkai',50)
    font_score = pygame.font.SysFont('arial',50)
    text_game_over = font_game_over.render('Fucking loser!', True, (255,0,0))
    text_score = font_score.render(f'Your score: {score}', True, (255,255,255))
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = f'New Record'
    else:
        text = f'Record still {best_score}'
    text_record = font_score.render(text,True,(255, 165, 0))
    insert_res(USERNAME,score)    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.fill(BLACK)
        screen.blit(text_game_over,(230,80))
        screen.blit(pygame.transform.scale(img,[210,210]),[5,5])
        screen.blit(text_score,(30,250))
        screen.blit(text_record, (30,300))
        pygame.display.update()


drawing_intro()
drawing_interface(score)
pygame.display.update()
while is_zero(mas) and is_can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            count = 0
            if event.key == pygame.K_LEFT:
                mas,count = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas,count = move_right(mas)
            elif event.key == pygame.K_UP:
                mas,count = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas,count = move_down(mas)
            score += count
            if is_zero(mas):
                empty = get_empty_list(mas)
                shuffle(empty)
                num = empty.pop()
                x,y = get_ind_from_num(num)
                mas = two_or_four(mas,x,y)
                drawing_interface(score)
            pygame.display.update()
    print(USERNAME)

drawing_game_over()



               
               
     


