from random import *
import pygame
import sys
from database import get_best,cur,insert_res
from functions import *
import json
import os

GAMERS_DB = get_best()

def drawing_top():
    font_top = pygame.font.SysFont('comicsansms',30)
    font_gamer = pygame.font.SysFont('comicsansms',17)
    text_head = font_top.render('Best tries: ', True, BLACK)
    screen.blit(text_head, (320,2))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index+1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, BLACK)
        screen.blit(text_gamer, (320, 35 + 25 * index))
    


def drawing_interface(score):
    """
    прорисовка интерфейса

    """
    pygame.draw.rect(screen,(222, 184, 135),title_rec)
    font = pygame.font.SysFont('comicsansms', 70)
    font_score = pygame.font.SysFont('comicsansms',55)
    text_score = font_score.render('Score: ', True, BLACK)
    text_score_value = font_score.render(f'{score}', True, BLACK)
    screen.blit(text_score,(15,35))
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

def init_const():
    """
    функция инициализирует константы

    """
    global score,mas
    mas = [[0] * 4 for i in range(4)]

    empty = get_empty_list(mas)
    shuffle(empty)
    num1 = empty.pop()
    num2 = empty.pop()
    x1,y1 = get_ind_from_num(num1)
    mas = two_or_four(mas,x1,y1)
    x2,y2 = get_ind_from_num(num2)
    mas = two_or_four(mas,x2,y2)
    score = 0
USERNAME = None
mas = None
score = None
path = os.getcwd()
if 'data.txt' in os.listdir(path):
    with open('data.txt') as file:
        data = json.load(file)
        USERNAME = data['user']
        mas = data['mas']
        score = data['score']
    full_path = os.path.join(path,'data.txt')
    os.remove(full_path)
else:
    init_const()

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

pygame.init()
screen = pygame.display.set_mode((widht,height))
pygame.display.set_caption('2048')

def save_game():
    """
    функция позволяет сохранить данные в json
    """
    data = {
        'user': USERNAME,
        'mas': mas,
        'score': score
    }
    with open('data.txt','w') as file:
        json.dump(data,file)


def drawing_intro():
    """
    функция обрабатывает заставку игры

    """
    img = pygame.image.load('images.jpg')
    font_welcome = pygame.font.SysFont('comicsansms',40)
    font_name = pygame.font.SysFont('comicsansms',50)
    text_welcome = font_welcome.render('WELCOME!',True,(250,0,0))
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
    global USERNAME,mas,score,GAMERS_DB
    img = pygame.image.load('img.jpg')
    font_game_over = pygame.font.SysFont('comicsansms',40)
    font_score = pygame.font.SysFont('arial',50)
    text_game_over = font_game_over.render('Fucking loser!', True, (220,0,0))
    text_score = font_score.render(f'Your score: {score}', True, (255,255,255))
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = f'New Record'
    else:
        text = f'Record still {best_score}'
    text_record = font_score.render(text,True,(255, 165, 0))
    insert_res(USERNAME,score)
    GAMERS_DB = get_best()    
    desicion = False
    while not desicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    USERNAME = None
                    desicion = True
                    init_const()
                elif event.key == pygame.K_SPACE:
                    desicion = True
                    init_const()

        screen.fill(BLACK)
        screen.blit(text_game_over,(215,80))
        screen.blit(pygame.transform.scale(img,[210,210]),[5,5])
        screen.blit(text_score,(30,250))
        screen.blit(text_record, (30,320))
        pygame.display.update()
    screen.fill(BLACK)
def game_loop():
    """
    функция объединяет в себе весь игровой процесс
    """
    global score,mas
    drawing_interface(score)
    pygame.display.update()
    is_mas_move = False
    while is_zero(mas) and is_can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                count = 0
                if event.key == pygame.K_LEFT:
                    mas,count,is_mas_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas,count,is_mas_move = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas,count,is_mas_move = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas,count,is_mas_move = move_down(mas)
                score += count
                if is_zero(mas) and is_mas_move:
                    empty = get_empty_list(mas)
                    shuffle(empty)
                    num = empty.pop()
                    x,y = get_ind_from_num(num)
                    mas = two_or_four(mas,x,y)
                    drawing_interface(score)
                    is_mas_move = False
                pygame.display.update()
        print(USERNAME)

while True:
    if USERNAME == None:
        drawing_intro()
    game_loop()
    drawing_game_over()



               
               
     


