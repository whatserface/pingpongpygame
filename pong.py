from pygame import *
from random import randint
import time as t
init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
win_w = 700
win_h = 500
window = display.set_mode((win_w, win_h))
display.set_caption("Pong Ping")
state = 1
l_player = Player(r'D:\Soft\PROGRAMMING\python projects\stuff\pingpongpygame-main\racket.png', 30, 200, 4, 50, 150)
r_player = Player(r'D:\Soft\PROGRAMMING\python projects\stuff\pingpongpygame-main\racket.png', 620, 200, 4, 50, 150)
ball = GameSprite(r'D:\Soft\PROGRAMMING\python projects\stuff\pingpongpygame-main\ball.png', win_w/2-25, win_h/2-25, 3, 50, 50)
ball.speed_x, ball.speed_y = 3, 3
clock = time.Clock()
FPS = 60
f0nt = font.SysFont(None, 50)
l_won = f0nt.render('Left Player Won', True, (0, 0, 224))
r_won = f0nt.render('Right Player Won', True, (0, 0, 224))
restart_sign = f0nt.render('Press SPACE to start new game', True, (245, 37, 78))
background_color = (255, 255, 255)
breakpoint_time = float('inf')
rand_object, kostil = GameSprite(r'D:\Soft\PROGRAMMING\python projects\stuff\pingpongpygame-main\racket.png', randint(150, 550), randint(50, 450), 0, 25, 75), False
while state:
    window.fill(background_color)
    if state == 1:
        l_player.update1()
        r_player.update2()
        ball.reset()
        if ball.rect.y > win_h-50 or ball.rect.y < 20:
            ball.speed_y *= -1
        if ball.rect.x < 20:
            state = 2
        if ball.rect.x > win_w-50:
            state = 3
        if (r_player.rect.colliderect(ball.rect) or l_player.rect.colliderect(ball.rect)) and abs(t.time()-breakpoint_time) > 0.3:
            breakpoint_time = t.time()
            ball.speed_x *= -1
            background_color = (randint(10, 240), randint(10, 240), randint(10, 240))
            while background_color == (245, 37, 78) or background_color == (0, 0, 224):
                background_color = (randint(10, 240), randint(10, 240), randint(10, 240))
            kostil = not kostil
            rand_object.rect.x, rand_object.rect.y = randint(150, 550), randint(50, 450)
        if kostil:
            rand_object.reset()
        if kostil and ball.rect.colliderect(rand_object.rect):
            ball.speed_x *= -1
            kostil = False
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
    if state == 2:
        window.blit(r_won, (win_w/2-125, win_h/2-75))
    if state == 3:
        window.blit(l_won, (win_w/2-125, win_h/2-75))
    if state >= 2:
        window.blit(restart_sign, (win_w/2-250, win_h/2-25))
    l_player.reset()
    r_player.reset()
    for e in event.get():
        if e.type == QUIT:
            state = 0
        if state >= 2 and e.type == KEYDOWN:
            if e.key == K_SPACE:
                background_color, l_player.rect.x, l_player.rect.y, r_player.rect.x, r_player.rect.y, ball.rect.y, ball.rect.x = (255, 255, 255), 30, 200, 620, 200, win_w/2-25, win_h/2-25
                state = 1
    clock.tick(FPS)
    display.update()
