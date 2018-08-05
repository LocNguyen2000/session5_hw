import pygame
from random import  randint

# 1. Initilize

pygame.init()

# 2. Set up game window

SIZE = (600,600)

BG_COLOR = (10, 44, 168)

canvas = pygame.display.set_mode(SIZE)

pygame.display.set_caption('Pong Game')

clock = pygame.time.Clock()

paddle_image = pygame.image.load('assets/paddle.png')
ball_image = pygame.image.load('assets/ball.png')

loop = True

a = randint(-5,5)
b = randint(-3,3)
if a == 0 or b == 0 :
    a = randint(-3,3)
    b = randint(-5,-5)


x1 = 0
y1 = 100

x2 = 570
y2 = 400

ball_x = 300
ball_y = 300

w_press = False
s_press = False

up_press = False
down_press = False

p_press = False

ball_v_x = a
ball_v_y = b

while loop:
    # poolong
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            loop = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                w_press = True
            elif e.key == pygame.K_s:
                s_press = True
            elif e.key == pygame.K_UP:
                up_press = True
            elif e.key == pygame.K_DOWN:
                down_press = True
            elif e.key == pygame.K_p:
                p_press = True


        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                w_press = False
            elif e.key == pygame.K_s:
                s_press = False
            elif e.key == pygame.K_UP:
                up_press = False
            elif e.key == pygame.K_DOWN:
                down_press = False

    if w_press:
        y1 -= 3
    if s_press:
        y1 += 3
    if up_press:
        y2 -= 3
    if down_press:
        y2 += 3

    if p_press:
        ball_x += ball_v_x
        ball_y += ball_v_y

    if ball_x >= 600 or ball_x <= 20:
            ball_v_x = -ball_v_x
    if ball_y >= 635 or ball_y <= 60:
            ball_v_y = -ball_v_y

    canvas.fill(BG_COLOR)
# action = thoat game
    canvas.blit(paddle_image,(x1, y1))
    canvas.blit(ball_image, (ball_x - 30/2 ,ball_y - 120/2))
    canvas.blit(paddle_image,(x2, y2))
    clock.tick(60)

    pygame.display.flip()



