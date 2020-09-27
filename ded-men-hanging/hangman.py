# Based on Tech with Tim's tutorial, but slightly modified

from random_word import RandomWords
import pygame
import random
import math

pygame.init()

width, height = 800, 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Now Playing: Hangman")

radius = 20
gap = 15
letters = []
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 400
A = 65
randWord = RandomWords()

for i in range(26):
    x = startx + (gap * 2) + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i), True])

letter_font = pygame.font.SysFont("comicsans", 40)
word_font = pygame.font.SysFont("comicsans", 60)
title_font = pygame.font.SysFont("comicsans", 70)

images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

hangman_status = 0
word = randWord.get_random_word().upper()
guessed = []

white = (255, 255, 255)
black = (0, 0, 0)

def draw():
    win.fill(white)
    text = title_font.render("Hangman", 1, black)
    win.blit(text, (width//2 - text.get_width()//2, 20))

    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = word_font.render(display_word, 1, black)
    win.blit(text, (400,200))

    for letter in letters:
        x, y, ltr, vis = letter
        if vis:
            pygame.draw.circle(win, black, (x,y), radius, 3)
            text = letter_font.render(ltr, 1, black)
            win.blit(text, (x - text.get_width()//2,y - text.get_height()//2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_msg(message):
    pygame.time.delay(500)
    win.fill(white)
    text = word_font.render(message, 1, black)
    win.blit(text, (width/2 - text.get_width()//2, height//2 - text.get_height()//2))
    pygame.display.update()
    pygame.time.delay(2000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, vis = letter
                    if vis:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < radius:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_msg("Congratulations! You won!")
            break
        if hangman_status == 6:
            display_msg("Aww man, you Lost!")
            break

main()
pygame.quit()
