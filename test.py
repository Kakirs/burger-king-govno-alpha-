from pygame import *
from random import *
window = display.set_mode((1100, 600))
display.set_caption("Доgонялки")
background = transform.scale(image.load("burgerking.jpg"), (1100, 600))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 1100 - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600 - 80:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 600:
            self.rect.x = randint(80, 1100 - 80)
            self.rect.y = 0
            lost = lost + 1

lost=0
game = True
KOLA = Player('burgerkiing.jpg', 350,450,11,150,150)
#wall1 = GameSprite('kamen.jpg', 100,0,5,50,250)
monsters = sprite.Group()
for i in range(3, 8):
    monster = Enemy('naggets.png', randint(80, 1100 - 80), -40,randint(1, 4), 100,100 )
    monsters.add(monster)
while game:

    window.blit(background,(0, 0))
    KOLA.reset()
    KOLA.update()
    monsters.update()
    monsters.draw(window)
    #wall1.reset()

    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()


