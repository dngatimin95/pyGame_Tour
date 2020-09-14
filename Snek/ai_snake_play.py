# Still WIP

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (247, 52, 52)
green = (135, 224, 121)
blue = (74, 127, 212)

width = 1000
height = 800

dis = pygame.display.set_mode((width,height))
pygame.display.set_caption("Now Playing: Snake Game")

size = 10

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("bahnschrift", 40)

def final_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def snake_draw(size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], size, size])

def obs(x1, y1, foodx, foody):
    x = x1
    y = y1

    def loop(x_add, y_add, head_x, head_y):
        head_x += 1
        head_y += 1
        distance = 0
        base_distance = math.sqrt((x_increment ** 2) + (y_increment ** 2))
        food = -1
        body = -1
        wall = -1
    return

def game_loop():
    max_score = 0
    game_over = False
    game_close = False
    changed = False

    x1 = width/2
    y1 = height/2

    x1_change = 0
    y1_change = 0

    snake_List = []
    snake_len = 1
    speed = 10

    foodx = round(random.randint(1, width - size) // 10) * 10
    foody = round(random.randint(1, height - size) // 10) * 10

    while not game_over:
        while game_close == True:
            max_score = max(max_score, snake_len - 1)
            dis.fill(white)
            final_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                game_loop()

        move = random.randint(0,3)
        print(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        if move == 0: #left
            x1_change = -size
            y1_change = 0
        elif move == 2: #right
            x1_change = size
            y1_change = 0
        elif move == 1: #up
            y1_change = -size
            x1_change = 0
        elif move == 3: #down
            y1_change = size
            x1_change = 0

        if x1 >= width:
            x1 = 0
            x1_change = size
        elif x1 < 0:
            x1 = width
            x1_change = -size
        elif y1 >= height:
            y1 = 0
            y1 = size
        elif y1 < 0:
            y1 = height
            y1_change = -size

        x1 += x1_change
        y1 += y1_change

        dis.fill(white)
        pygame.draw.rect(dis, green, [foodx, foody, size, size])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_len:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake_draw(size, snake_List)
        final_score(snake_len - 1)
        pygame.display.update()

        change = random.randint(0,100)
        if changed == False and change%10 == 0:
            foodx = round(random.randint(1, width - size) // 10) * 10
            foody = round(random.randint(1, height - size) // 10) * 10
            changed = True

        if x1 == foodx and y1 == foody:
            foodx = round(random.randint(1, width - size) // 10) * 10
            foody = round(random.randint(1, height - size) // 10) * 10
            snake_len += 1
            changed = False
            speed += 5
        clock.tick(speed)

    pygame.quit()
    quit()

game_loop()
