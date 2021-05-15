from pygame import *
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
l_player = Player('racket.jpg', 30, 200, 4, 50, 150)
r_player = Player('racket.jpg', 620, 200, 4, 50, 150)
ball = GameSprite('ball.jpg', win_w/2-25, win_h/2-25, 3, 50, 50)
ball.speed_x, ball.speed_y = 3, 3
clock = time.Clock()
FPS = 60
f0nt = font.SysFont(None, 50)
l_won = f0nt.render('Left Player Won', True, (141, 173, 224))
r_won = f0nt.render('Right Player Won', True, (141, 173, 224))
restart_sign = f0nt.render('Press SPACE to start new game', True, (245, 37, 78))
def restart():
    l_player.rect.x, l_player.rect.y, r_player.rect.x, r_player.rect.y = 30, 200, 620, 200
    state = 1
while state:
    window.fill((255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            state = 0
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
        if r_player.rect.colliderect(ball.rect) or l_player.rect.colliderect(ball.rect):
            ball.speed_x *= -1
            ball.speed_y *= -1
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
    if state == 2:
        window.blit(r_won, (win_w/2-75, win_h/2-75))
    if state == 3:
        window.blit(l_won, (win_w/2-75, win_h/2-75))
    if state >= 2:
        window.blit(restart_sign, (win_w/2-275, win_h/2-25))
    l_player.reset()
    r_player.reset()
    display.update()
    for e in event.get():
        if state >= 2 and e.type == KEYDOWN:
            if e.key == K_SPACE:
                restart()
    clock.tick(FPS)
