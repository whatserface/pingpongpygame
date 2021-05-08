from pygame import *
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
clock = time.Clock()
FPS = 60
while state:
    window.fill((255, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            state = 0
    if state == 1:
        l_player.update1()
        r_player.update2()
    l_player.reset()
    r_player.reset()
    display.update()
    clock.tick(FPS)