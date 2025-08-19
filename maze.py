#создай игру "Лабиринт"!
from pygame import *
mixer.init()
font.init()
window = display.set_mode((700,500))
display.set_caption('Лабиринт')


class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if key_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 615:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy_2(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 220:
            self.direction = 'right'
        if self.rect.x >= 400:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed            

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, width, height, wall_x, wall_y):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((width, height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

background = transform.scale(image.load('background.jpg'),(700,500))

player = Player('hero.png',100,300,10)
enemy = Enemy('cyborg.png',500,250,2)
enemy_2 = Enemy_2('cyborg.png',300,100,2)
treasure = GameSprite('treasure.png',575,375,0)
wall_1 = Wall(102, 222, 100, 10, 300, 200, 210)
wall_2 = Wall(102, 222, 100, 400, 10, 200, 80)
wall_3 = Wall(102, 222, 100, 10, 80, 200, 0)
wall_4 = Wall(102, 222, 100, 10, 300, 300, 90)
wall_5 = Wall(102, 222, 100, 10, 300, 400, 210)
wall_6 = Wall(102, 222, 100, 150, 10, 400, 210)


font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (241, 245, 15))
lose = font.render('YOU LOSE', True, (255, 0, 0))


mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

clock = time.Clock()
FPS = 60
game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        enemy_2.update()
        enemy_2.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        treasure.reset()
        if sprite.collide_rect(player, treasure):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, enemy_2) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
    display.update()
    clock.tick(FPS)
