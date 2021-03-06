# I'm sorry for this game

import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (247, 52, 52)
green = (135, 224, 121)
blue = (74, 127, 212)

width, height = 1000, 800
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Now Playing: Snake Game")
size = 10

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("bahnschrift", 40)

def final_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    win.blit(value, [0, 0])

def snake_draw(size, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, black, [x[0], x[1], size, size])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width//5, height//3])

def second_message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [(width//5)+100, (height//3)-50])

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
            win.fill(white)
            message("You Lost! Press Q to Quit or P to Play Again", red)
            second_message("Highest Score: " + str(max_score), red)
            final_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
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

        win.fill(white)
        pygame.draw.rect(win, green, [foodx, foody, size, size])
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

        # If i'm truly evil then comment the if statement above and uncomment below
        #foodx = round(random.randint(1, width - size) // 10) * 10
        #foody = round(random.randint(1, height - size) // 10) * 10

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
